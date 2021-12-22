import pymongo
from mongokit.database import Database

# code copied and adapted from mongokit (3-clause BSD license)

class CallableMixin(object):
    """
    brings the callable method to a Document. usefull for the connection's
    register method
    """
    def __call__(self, doc=None, gen_skel=True, lang='en', fallback_lang='en'):
        return self._obj_class(doc=doc, gen_skel=gen_skel,
                               collection=self.collection,
                               lang=lang, fallback_lang=fallback_lang)


_iterables = (list, tuple, set, frozenset)


class ReplicaSetConnection(pymongo.ReplicaSetConnection):
    # class to get replset features from pymongo and document from mongokit

    def __init__(self, *args, **kwargs):
        self._databases = {}
        self._registered_documents = {}
        super(ReplicaSetConnection, self).__init__(*args, **kwargs)

    def register(self, obj_list):
        decorator = None
        if not isinstance(obj_list, _iterables):
            # we assume that the user used this as a decorator
            # using @register syntax or using conn.register(SomeDoc)
            # we stock the class object in order to return it later
            decorator = obj_list
            obj_list = [obj_list]
        # cleanup
        for dbname, db in self._databases.items():
            for colname, col in db._collections.items():
                for docname, doc in col._documents.items():
                    del col._documents[docname]
                for obj_name in [obj.__name__ for obj in obj_list]:
                    if obj_name in col._registered_documents:
                        del col._registered_documents[obj_name]
        # register
        for obj in obj_list:
            CallableDocument = type(
              "Callable%s" % obj.__name__,
              (obj, CallableMixin),
              {"_obj_class": obj, "__repr__": object.__repr__}
            )
            self._registered_documents[obj.__name__] = CallableDocument
        # if the class object is stored, it means the user used a decorator and
        # we must return the class object
        if decorator is not None:
            return decorator

    def __getattr__(self, key):
        if key in self._registered_documents:
            document = self._registered_documents[key]
            try:
                return getattr(self[document.__database__][document.__collection__], key)
            except AttributeError:
                raise AttributeError("%s: __collection__ attribute not found. "
                  "You cannot specify the `__database__` attribute without "
                  "the `__collection__` attribute" % key)
        else:
            if key not in self._databases:
                self._databases[key] = Database(self, key)
            return self._databases[key]