#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        test.py
#created:        2010-12-18 22:42
import re
import pycurl
import json
import urllib
import StringIO
import time
import sys

#DEBUG=True
DEBUG=False

'''force utf-8 encoding system'''
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)

sys.setdefaultencoding(default_encoding)



class Api:
    api_base="api.fanfou.com"
#extention="xml" #json, xml, rss
    extension='json' if not DEBUG else 'xml'

    api={
        'public_timeline':'statuses/public_timeline',
        'friends_timeline':'statuses/friends_timeline',
        'exists':'friendships/exists',
        "replies": "statuses/replies",
        "mentions":"statuses/mentions",
        "show": "statuses/show",
        "test": "help/test",
        "user_timeline": "statuses/user_timeline",
        "update": "statuses/update",
        "destroy":"statuses/destroy",
    #photo related
        "photos_upload":"photos/upload",
    #search
        "search_public_timeline": "search/public_timeline",
        "trends":"trends",
        "users_friends":"users/friends",
        "users_followers":"users/followers",
        "users_show": "users/show",
    #private msg
        "direct_messages": "direct_messages",
        "direct_messages_sent": "direct_messages/sent",
        "direct_messages_new": "direct_messages/new",
        "direct_messages_destroy": "direct_messages/destroy",
    #favorites related
        "favorites":"favorites",
        "favorites_create_id":"favorites/create/id",
        "favorites_destroy": "favorites/destroy/id",
    #friends
        "friendships_create": "friendships/create",
        "friendships_destroy":"friendships/destroy",
        "friendships_exists":"friendships/exists",
        'friends_ids':'friends/ids',
        'followers_ids':'followers/ids',
    #notification
        'notifications_follow':"notifications/follow",
        'notifications_leave':"notifications/leave",
    #Blacklist
        'blocks_create':'blocks/create',
        'blocks_destroy':'blocks/destroy',
    #account
        'account_verify_credentials':'account/verify_credentials',
    #search
        'saved_searches':'saved_searches',
        'saved_searches_show_id':'saved_searches/show/id',
        'saved_searches_create':'saved_searches/create',
        'saved_searches_destroy':'saved_searches/destroy/id',
    }

    def __init__(self, api_type, id=""):
        self.api_type=api_type
        self.id=id

    def __str__(self):
        if self.api_type in self.api.keys():
            api=self.api[self.api_type]
            if api[-2:]=='id' and self.id:
                url = "http://"+self.api_base+"/"+api[:-2]+self.id+"."+self.extension
            else:
                url = "http://"+self.api_base+"/"+api+"."+self.extension
            if DEBUG:
                print url
            return url
        else:
            return ""

class Fanfou:
#config:
    source='shenliutang'

    def __init__(self, id="", sn=""):
        self.id=id
        self.sn=sn
        self.output = StringIO.StringIO()
            #getvalue()
        self._init_curl()

    #delete object
    def __del__(self):
        try:
            self.curl.close()
            self.output.close()
        except:
            pass

    #init curl
    def _init_curl(self):
        c=pycurl.Curl()
        userpwd=""
        if self.sn:
            userpwd= "%s:%s" % (self.id,self.sn)
            c.setopt(c.USERPWD,userpwd)

        c.setopt(c.URL, str(Api('test')))

        if DEBUG:
            c.setopt(c.VERBOSE, 1)

        self.output.truncate(0)
        c.setopt(c.WRITEFUNCTION, self.output.write)
        c.perform()
        self.curl=c

    def _callback(self, api_type, jsonData={}, POST=False):
        c=self.curl
        self.output.truncate(0)

        dynamic_api=False
        if jsonData.has_key('id'):
            url=str(Api(api_type, jsonData['id']))
        else:
            url=str(Api(api_type))
        assert url, 'No API named %s!' % api_type

        data=urllib.urlencode(jsonData)

        if POST:
            #the original curl object is not contaminated
            #here is only a local copy
            c.setopt(c.POSTFIELDS, data)
        else:
            url += "?"+data
        try:
            c.setopt(c.URL, url)
            c.perform()
        except Exception, e:
            print "Error: _callback in Fanfou Class"+str(e)

        return self._getJson() if not DEBUG else self.output.getvalue()

    #parse string and return json
    def _getJson(self):
        value=self.output.getvalue()
        return json.loads(value)

# apis
# public timeline
#???????????????????????????
    def PublicTimeline(self, count=20, format=""):
        jsonData={
            'count':count,
            'format':format,
        }
        api='public_timeline'
        return self._callback(api, jsonData)
#??????????????????????????????
    def FriendsTimeline(self, count=20, since_id="", max_id="", page=1, format=""):
        jsonData={
            'id':self.id,
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
            'format':format, #might be html
        }
        api="friends_timeline"
        return self._callback(api, jsonData)

#?????????????????????
    def UserTimeline(self, count=20, since_id="", max_id="", page=1, format=""):
        jsonData={
            'id':self.id,
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
            'format':format, #might be html
        }
        api="user_timeline"
        return self._callback(api, jsonData)

#??????????????????
    def Show(self, msgid):
        jsonData={
            'id': msgid,
        }
        api="show"
        return self._callback(api, jsonData)

#?????????????????????????????????
    def Replies(self, count=20, since_id="", max_id="", page=1, format=""):
        jsonData={
            'id':self.id,
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
            'format':format, #might be html
        }
        api="replies"
        return self._callback(api, jsonData)

#?????????????????????????????????
    def Mentions(self, count=20, since_id="", max_id="", page=1, format=""):
        jsonData={
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
            'format':format, #might be html
        }
        api="mentions"
        return self._callback(api, jsonData, POST=True)#????????????
    def Update(self, status, in_reply_to_status_id="", source="", location=""):
        jsonData={
            'status':status,
            'in_reply_to_status_id':in_reply_to_status_id,
            'source':source if source else self.source,
        }

        api="update"
        return self._callback(api, jsonData, POST=True)

#????????????
    def Destroy(self, msgid):
        jsonData={
            'id':msgid,
        }

        api="destroy"
        return self._callback(api, jsonData, POST=True)

#?????????????????????
#????????????
    def PhotosUpload(self, photo_full_path, status="", source="", location=""):
        '''uploading photo to fanfou
           new curl request.'''
        jsonData=[
            ('photo', (pycurl.FORM_FILE, photo_full_path)),
            ('status', status),
            ('source', source),
            ('location', location),
        ]
        api='photos_upload'
        c=self.curl
        self.output.truncate(0)
        url=str(Api(api))
        assert url, 'No API named %s!' % api_type

        c.setopt(c.URL, url)
        c.setopt(c.HTTPPOST, jsonData)
        c.perform()

        return self._getJson() if not DEBUG else self.output.getvalue()
#?????????????????????
#????????????
    def SearchPublicTimeline(self, q, max_id=""):
        jsonData={
            'q':q,
            'max_id':max_id,
        }
        api='search_public_timeline'

        return self._callback(api, jsonData)
#??????
    def Trends(self):
        jsonData={}
        api='trends'
        return self._callback(api, jsonData)

#?????????????????????
#??????????????????
    def UsersFriends(self, userid="", page=1):
        jsonData={
            'id': userid if userid else self.id,
            'page':page,
        }
        api="users_friends"
        return self._callback(api, jsonData)

#?????????????????????
    def UsersFollowers(self, userid="", page=1):
        jsonData={
            'id': userid if userid else self.id,
            'page':page,
        }
        api="users_followers"
        return self._callback(api, jsonData)

#????????????????????????
    def UsersShow(self, userid=""):
        '''id (??????) - ?????? id?????????????????????????????????????????????????????????????????????????????????????????????'''
        jsonData={
            'id': userid if userid else self.id,
        }
        api="users_show"
        return self._callback(api, jsonData)

#?????????????????????
#???????????????????????????
    def DirectMessages(self, count=20, since_id="",
            max_id="",
            page=1):
        jsonData={
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
        }
        api="direct_messages"
        return self._callback(api, jsonData)

#???????????????????????????
    def DirectMessagesSent(self,
            count=20,
            since_id="",
            max_id="",
            page=1):

        jsonData={
            'count':count,
            'since_id':since_id,
            'max_id':max_id,
            'page':page,
        }

        api="direct_messages_sent"
        return self._callback(api, jsonData)
#????????????
    def DirectMessagesNew(self,
            user_id,
            text,
            in_reply_to_id=""):
        jsonData={
            "user":user_id,
            "text":text,
            "in_reply_to_id":in_reply_to_id,
        }
        api="direct_messages_new"
        return self._callback(api, jsonData, POST=True)

#????????????
    def DirectMessagesDestroy(self, id):
        jsonData={
            "id":id,
        }
        api="direct_messages_destroy"
        return self._callback(api, jsonData, POST=True)

#????????????
#???????????????????????????
    def Favorites(self, userid="", count=20, page=1):
        jsonData={
        'id':userid if userid else self.id,
        'count': count,
        'page': page,
        }
        api='favorites'
        return self._callback(api, jsonData)

#??????????????????
    def FavoritesCreate(self, id):
        jsonData={
            "id":id,
        }
        api="favorites_create_id"
        return self._callback(api, jsonData, POST=True)

#????????????
    def FavoritesDestroy(self, id):
        jsonData={
            "id":id,
        }
        api="favorites_destroy"
        return self._callback(api, jsonData, POST=True)

#??????????????????
#????????????
    def FriendShipCreate(self, id):
        jsonData={
            "id":id,
        }
        api="friendships_create"
        return self._callback(api, jsonData, POST=True)
#????????????
    def FriendShipDestroy(self, id):
        jsonData={
            "id":id,
        }
        api="friendships_destroy"
        return self._callback(api, jsonData, POST=True)

#??????????????????????????????

    def FriendShipExists(self, user_a, user_b):
        '''test if user_b is in user_a's friends list'''
        jsonData={
            "user_a": user_a,
            "user_b": user_b,
        }
        api="friendships_exists"
        return self._callback(api, jsonData)

#????????????????????????
#????????????id??????
    def FriendsIDs(self, id=''):
        '''id (??????) - ?????? id?????????????????????????????????????????????????????????'''
        jsonData={
            "id": id if id else self.id,
        }
        api="friends_ids"
        return self._callback(api, jsonData)


#???????????????id??????
    def FollowersIDs(self, id=""):
        '''id (??????) - ?????? id?????????????????????????????????????????????????????????'''
        jsonData={
            "id": id if id else self.id,
        }
        api="followers_ids"
        return self._callback(api, jsonData)

#????????????????????????
#????????????
    def NotificationsFollow(self, id):
        jsonData={
            "id": id,
        }
        api="notifications_follow"
        return self._callback(api, jsonData, POST=True)

#????????????
    def NotificationsLeave(self, id):
        jsonData={
            "id": id,
        }
        api="notifications_leave"
        return self._callback(api, jsonData, POST=True)
#???????????????
#???????????????
    def BlocksCreate(self, id):
        jsonData={
            "id": id,
        }
        api="blocks_create"
        return self._callback(api, jsonData, POST=True)
#???????????????
    def BlocksDestroy(self, id):
        jsonData={
            "id": id,
        }
        api="blocks_destroy"
        return self._callback(api, jsonData, POST=True)

#???????????????????????????
#???????????????????????????????????????
    def SavedSearches(self):
        api="saved_searches"
        return self._callback(api)

#????????????????????????
    def SavedSearchesShowID(self, id):
        jsonData={
            'id':id,
        }
        api="saved_searches_show_id"
        return self._callback(api, jsonData)

#???????????????
    def SavedSearchesCreate(self, query):
        jsonData={
            "query":query,
        }
        api="saved_searches_create"
        return self._callback(api, jsonData, POST=True)

#???????????????
    def SavedSearchesDestroy(self, id):
        jsonData={
            'id':id,
        }
        api="saved_searches_destroy"
        return self._callback(api, jsonData, POST=True)


