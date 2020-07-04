import json
import requests
class CrypoCompare:
    base_uri = "https://min-api.cryptocompare.com/data/"
    def __init__(self, api_key):
        self.session = requests.session()
        self.headers = {
            "authorization": f"Apikey {api_key}"
        }
    def get(self, url):
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code < 200 or resp.status_code > 300:
            raise Exception("api error: {resp.reason}")
        resp = json.loads(resp.content)
        if resp['Response'] != 'Success':
            raise Exception("api error: {resp['Message']}")
        return resp['Data']
    def available_tokens(self):
        route = "blockchain/list"
        uri = self.base_uri + route
        return self.get(uri)
