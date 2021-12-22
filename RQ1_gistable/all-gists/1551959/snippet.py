def get_and_update_or_create(model, unique, update):
    """
    Given a model, a dictionary of lookup arguments, and a dictionary of update
    arguments, this convenience function gets an object and updates it in the
    database if necessary.

    Returns a tuple (object, int) where int is 0 if the object was not updated,
    1 if the object was created, and 2 if the object was updated in the
    database.

    >>> resp = get_and_update_or_create(User, {'username': 'example'}, {'email': 'example@example.com'})
    >>> resp
    (<User: example>, 1)
    >>> resp[0].email
    'example@example.com'
    >>> resp = get_and_update_or_create(User, {'username': 'example'}, {'email': 'example@example.com'})
    >>> resp
    (<User: example>, 0)
    >>> resp[0].email
    'example@example.com'
    >>> resp = get_and_update_or_create(User, {'username': 'example'}, {'email': 'another@example.com'})
    >>> resp
    (<User: example>, 2)
    >>> resp[0].email
    'another@example.com'
    """
    obj, created = model.objects.get_or_create(dict(unique, default=update))

    # If we just created it, then the defaults kicked in and we're good to go
    if created:
        return obj, 1

    # Iterate over all of the fields to update, updating if needed, and keeping
    # track of whether any field ever actually changed
    modified = False
    for name, val in update.iteritems():
        if getattr(obj, name) != val:
            modified = True
            setattr(obj, name, val)
    
    # If a field did change, update the object in the database and return
    if modified:
        obj.save(force_update=True)
        return obj, 2
    
    # Otherwise the object in the database is up to date
    return obj, 0