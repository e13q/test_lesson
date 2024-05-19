import requests  
import json

class BitlyAPI:
    #urlUserInfo = 'https://api-ssl.bitly.com/v4/user'
    urlExpand = 'https://api-ssl.bitly.com/v4/expand'
    urlBitlinks = 'https://api-ssl.bitly.com/v4/bitlinks'
    apiKeyHeader = None
    def __init__(self, apiKey):
        self.apiKeyHeader = { 'Authorization': apiKey}
        return
    def responseCheckAndOut(self, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Response error')   
        print("Status Code: " + str(response.status_code))   
        return
    def createBitlink(self, url):        
        res = requests.post(self.urlBitlinks, headers = self.apiKeyHeader, data = json.dumps({ "long_url": url}))
        self.responseCheckAndOut(res)    
        if res.status_code == 200:
            print(json.loads(res.text)['link']) 
        return     
    def expandBitlink(self, url):        
        res = requests.post(self.urlExpand, headers = self.apiKeyHeader, data = json.dumps({ "bitlink_id": url}))
        self.responseCheckAndOut(res)
        if res.status_code == 200:
            print(json.loads(res.text)['long_url']) 
        return     



    



