import requests


def hero_intelligence(name):
    url1 = 'https://superheroapi.com/api/2619421814940190/search/name/powerstats'
    url2 = url1.replace('name', name)
    response = requests.get(url2)
    response_json = response.json()
    results = response_json['results'][0]
    powerstats = results['powerstats']
    return powerstats['intelligence']


if __name__ == '__main__':
    name_list = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    intel_list = []
    for hero in name_list:
        intell = int(hero_intelligence(hero))
        pre_dict = {'Name': hero, 'Intelligence': intell}
        intel_list.append(pre_dict)
    low_high_list = sorted(intel_list, key=lambda i: i['Intelligence'], reverse=True)
    print(f'Самый умный - {low_high_list[0]["Name"]}, его интеллектуальный уровень - {low_high_list[0]["Intelligence"]}')



    #
    # url = "https://api.github.com"
    # param = {"foo": "bar", "message": "helllo"}
    # headers = {"Authorization": "secret-token-123"}
    #
    # resp = requests.get(url)
    # resp = requests.get(url, params=param, headers=headers)
    # response = requests.get('https://httpbin.org/get')

    # print(response.content)
    # print(response.text)
    # print(response.json())
    # print(response.)
    # print(response.headers['Access-Control-Expose-Headers'])

    # response = requests.get(
    #     'https://api.github.com/search/repositories',
    #     params={'q': 'requests+language:python'},
    # )
    # Анализ некоторых атрибутов местонахождения запросов
    # json_response = response.json()
    # repository = json_response['items'][0]
    # print(f'Repository name: {repository["name"]}')  # Python 3.6+
    # print(f'Repository description: {repository["description"]}')  # Python 3.6+
    # print(json_response)

    # response = requests.get(
    #     'https://api.github.com/search/repositories',
    #     params={'q': 'requests+language:python'},
    #     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
    # )
    #
    # # просмотр нового массива `text-matches` с предоставленными данными
    # # о поиске в пределах результатов
    # json_response = response.json()
    # repository = json_response['items'][0]
    # print(f'Text matches: {repository["text_matches"]}')
    # resp = requests.post('https://httpbin.org/post', data={'key3332323': 'value'})
    # print(resp.text)

    # response = requests.post('https://httpbin.org/post', json={'keyfor':'valueme'})
    # json_response = response.json()
    # print(json_response['data'])
    # print(json_response)
    # print(json_response['headers']['Content-Type'])
    # help(requests)
