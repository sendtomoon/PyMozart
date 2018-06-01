import json
import requests
import datetime

url = 'http://192.168.0.1/'
loginParam = '{"method":"do","login":{"password":"WrLio6Kc9TefbwK"}}'
headers = {'content-type':'application/json'}
responseLogin = requests.post(url, headers=headers, data=loginParam)
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '---'  + responseLogin.text
stokJson = json.loads(responseLogin.text)
stok = stokJson['stok']
url2 = 'http://192.168.0.1/stok=' + stok  + '/ds'
wanRequest = '{"network":{"name":"wan_status"},"method":"get"}'
wanResponse = requests.post(url2, headers=headers, data=wanRequest)
ipJson = json.loads(wanResponse.text)
ip = ipJson['network']['wan_status']['ipaddr']
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '---'  + ip
urlGodaddy = 'https://api.godaddy.com/v1/domains/name/records/A/*'
godaddyParam = '[{"data":"'+ip+'"}]'
headersGodaddy = {'Authorization':'sso-key *:*','Content-Type':'application/json'}
requests.packages.urllib3.disable_warnings()
godaddyResponse = requests.put(urlGodaddy,headers=headersGodaddy,data=godaddyParam,verify=False)
print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '---'  + godaddyResponse.text + '---'  + 'Done'
