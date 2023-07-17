import requests

url = 'https://akabab.github.io/superhero-api/api'
method = '/all.json'
response = requests.get(url + method)

# print(response.text)

hero_list = ['Hulk', 'Captain America', 'Thanos']
hero_int = []

for h in response.json():
    if h['name'] in hero_list:
        hero_int.append({h['name']: h['powerstats']['intelligence']})

for hero in hero_int:
    for h, i in hero.items():
        max_intel = 0
        # print(i)
        if i > max_intel:
            max_intel = i
            most_intel = h

print(f'Самый умный супергерой из списка - {most_intel}. Его интелект равен {max_intel}.')
