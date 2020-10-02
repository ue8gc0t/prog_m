import json
import requests

token = '8f23deef8f23deef8f23deefdd8f512b7588f238f23deefd025c3bb7745969b42b1368f'
version = '5.120'
user_id = 'qoozkid'



def posts(token, version, owner_id):
    response = requests.get('https://api.vk.com/method/wall.get',
        params={
            'access_token': token,
            'v': version,
            'owner_id':int('-'+str(owner_id)),
            'count':100,
            'offset':0,
            'extend':1
            }
        )
    return(response.json())
    
def post_id(js_file):
    ids = []
    for post in js_file["response"]["items"]:
        ids.append(post["id"])
    return(ids)
        
def liked(owner_id,item_id):
    response = requests.get('https://api.vk.com/method/',
        params={
            'access_token': token,
            'v': version,
            'user_id':user_id
            }
        )
        
        

response = requests.get('https://api.vk.com/method/users.getSubscriptions',
        params={
            'access_token': token,
            'v': version,
            'user_id':user_id
            }
        )

data = response.json()

print(json.dumps(data, indent=3))   
    
"""for group in data["response"]["groups"]["items"]:
    posts(token,version,group)"""

group = data["response"]["groups"]["items"][1]
slc = posts(token,version,group)
print("-"+str(group))
print(post_id(posts(token,version,group)))

with open("vkn.json", "w", encoding='utf-8') as vk_user:
    json.dump(slc, vk_user, sort_keys=True, ensure_ascii=False, indent=2)