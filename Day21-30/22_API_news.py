import requests

resp = requests.get('http://api.tianapi.com/guonei/?key=aed4c42af72f3ff0fef68d5c23cca236&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)