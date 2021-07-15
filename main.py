import requests

url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?'
paramas={
    'appid':'440',
    'count':'3',
    'maxlength':'300',
    'format':'json',
}

r = requests.get(url,paramas).json()
item = r['appnews']['newsitems']
for items in item:
    print(items['appid'])
    print(items['title'])
    print(items['url'])
