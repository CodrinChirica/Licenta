import requests


def markupValidator(search_url):
    res = requests.get('https://validator.w3.org/check?uri={}&output=json'.format(search_url.encode('utf-8')))
    print(res.json) 
    print(res.raw) 
    print(res.text.encode('utf-8')) 
