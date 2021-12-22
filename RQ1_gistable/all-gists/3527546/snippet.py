#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<17175297.hk@gmail.com>
#         http://binux.me
# Created on 2012-08-30 17:43:49

import logging
logger = logging.getLogger()

class BaseDB:
    '''
    BaseDB

    dbcur should be overwirte
    '''
    @property
    def dbcur(self):
        raise Exception("NOT IMPL")

    def _execute(self, sql_query, values=[]):
        return self.dbcur.execute(sql_query, values)
    
    def _select(self, tablename, what="*", where="", offset=0, limit=None):
        sql_query = "SELECT %s FROM %s" % (what, tablename)
        if where: sql_query += " WHERE %s" % where
        if limit: sql_query += " LIMIT %d, %d" % (offset, limit)
        logger.debug("<sql: %s>" % sql_query)

        return self._execute(sql_query)

    def _select2dic(self, tablename, what="*", where="", offset=0, limit=None):
        sql_query = "SELECT %s FROM %s" % (what, tablename)
        if where: sql_query += " WHERE %s" % where
        if limit: sql_query += " LIMIT %d, %d" % (offset, limit)
        logger.debug("<sql: %s>" % sql_query)

        dbcur = self._execute(sql_query)
        fields = [f[0] for f in dbcur.description]
        return [dict(zip(fields, row)) for row in dbcur.fetchall()]
 
    def _replace(self, tablename, **values):
        if values:
            _keys = ", ".join(("`%s`" % k for k in values.iterkeys()))
            _values = ", ".join(["?", ] * len(values))
            sql_query = "REPLACE INTO `%s` (%s) VALUES (%s)" % (tablename, _keys, _values)
        else:
            sql_query = "REPLACE INTO %s DEFAULT VALUES" % tablename
        logger.debug("<sql: %s>" % sql_query)
        
        if values:
            dbcur = self._execute(sql_query, values.values())
        else:
            dbcur = self._execute(sql_query)
        return dbcur.lastrowid
 
    def _insert(self, tablename, **values):
        if values:
            _keys = ", ".join(("`%s`" % k for k in values.iterkeys()))
            _values = ", ".join(["?", ] * len(values))
            sql_query = "INSERT INTO `%s` (%s) VALUES (%s)" % (tablename, _keys, _values)
        else:
            sql_query = "INSERT INTO %s DEFAULT VALUES" % tablename
        logger.debug("<sql: %s>" % sql_query)
        
        if values:
            dbcur = self._execute(sql_query, values.values())
        else:
            dbcur = self._execute(sql_query)
        return dbcur.lastrowid

    def _update(self, tablename, where, **values):
        _key_values = ", ".join(["`%s` = ?" % k for k in values.iterkeys()]) 
        sql_query = "UPDATE %s SET %s WHERE %s" % (tablename, _key_values, where)
        logger.debug("<sql: %s>" % sql_query)
        
        return self._execute(sql_query, values.values())
    
    def _delete(self, tablename, where):
        sql_query = "DELETE FROM %s" % tablename
        if where: sql_query += " WHERE %s" % where
        logger.debug("<sql: %s>" % sql_query)

        return self._execute(sql_query)

if __name__ == "__main__":
    import sqlite3
    class DB(BaseDB):
        __tablename__ = "test"
        def __init__(self):
            self.conn = sqlite3.connect(":memory:")
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE `%s` (id INTEGER PRIMARY KEY AUTOINCREMENT, name, age)'''
                    % self.__tablename__)
              
        @property
        def dbcur(self):
            return self.conn.cursor()

    db = DB()
    assert db._insert(db.__tablename__, name="binux", age=23) == 1
    assert db._select(db.__tablename__, "name, age").fetchone() == ("binux", 23)
    assert db._select2dic(db.__tablename__, "name, age")[0]["name"] == "binux"
    assert db._select2dic(db.__tablename__, "name, age")[0]["age"] == 23
    db._replace(db.__tablename__, id=1, age=24)
    assert db._select(db.__tablename__, "name, age").fetchone() == (None, 24)
    db._update(db.__tablename__, "id = 1", age=16)
    assert db._select(db.__tablename__, "name, age").fetchone() == (None, 16)
    db._delete(db.__tablename__, "id = 1")
    assert db._select(db.__tablename__).fetchall() == []
