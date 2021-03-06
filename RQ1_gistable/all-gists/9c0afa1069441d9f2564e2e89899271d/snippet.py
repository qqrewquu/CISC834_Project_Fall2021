# coding=utf-8                                                                                                                                    
# pip install zhihu_oauth                                                                                                                         
                                                                                                                                                  
import os                                                                                                                                         
import time                                                                                                                                       
import json                                                                                                                                       
                                                                                                                                                  
from zhihu_oauth import ZhihuClient                                                                                                               
                                                                                                                                                  
TOKEN_FILE = 'token.pkl' 
API = 'https://www.zhihu.com/api/v4/messages'

client = ZhihuClient()                                                                                                                                                                                                                                                           
                                                                                                                                                  
if os.path.isfile(TOKEN_FILE):                                                                                                                    
    client.load_token(TOKEN_FILE)                                                                                                                 
else:                                                                                                                                             
    client.login_in_terminal()                                                                                                                    
    client.save_token(TOKEN_FILE)     
    
me = client.me()
                                                                                                                                                  
rs = list(me.lives)                                                                                                                               
live = rs[0]                                                                                                                                      
if int(live.id) != 827530183664861184:                                                                                                            
    raise TypeError()                                                                                                                             

content = '''
???????????????????????????Live???????????????????????????????????????5??????????????????????????????????????????????????????4???15??????????????????????????????????????????????????????
 
-  ???????????????'''
                                                                                                                                                  
for p in live.participants:                                                                                                                       
    r = me._session.post(API, data=json.dumps({                                                                                                   
        'type': "common", 'content': content, 'receiver_hash': p[2].id}))                                                                         
    if r.status_code == 403 and '?????????????????????' not in r.json()['error']['message']:                                                             
        break                                                                                                                                     
    time.sleep(10)                 