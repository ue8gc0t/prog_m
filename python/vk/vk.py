import requests
import json
import csv


def get_1000_posts():
    token = '8f23deef8f23deef8f23deefdd8f512b7588f238f23deefd025c3bb7745969b42b1368f'
    version = '5.120'
    domain = 'tmn_kzn'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
        params={
            'access_token': token,
            'v': version,
            'domain': domain,
            'count': count,
            'offset': offset
            }
        )
        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 100
    return(all_posts)

def file_writer(all_posts):
    with open('vk.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file, dialect='excel')
        a_pen.writerow('body')
        for post in all_posts:
            a_pen.writerow(post['text'])


all_posts = get_1000_posts()
file_writer(all_posts)

with open("vk.json", "w", encoding='utf-8') as vk_wall:
    json.dump(all_posts, vk_wall, sort_keys=True, ensure_ascii=False)