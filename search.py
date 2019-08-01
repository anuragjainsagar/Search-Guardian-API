import requests
import json

BASE_URL = "http://content.guardianapis.com/"
END_POINT = "search?api-key=test&q=modi&showfields=thumbnail,headline&page=1&page-size=10"
def get_resources():
    resp = requests.get(BASE_URL+END_POINT)
    print(resp.status_code)
    print(type(resp))
    a = resp.json()
    print(a)
get_resources()
