import requests
host = "http://localhost:9999"
r = requests.get(f"{host}/train")
print(r.text)

payload = [{"Age": 85, "Sex": "male", "Embarked": "S"},
           {"Age": 24, "Sex": "female", "Embarked": "C"},
           {"Age": 3, "Sex": "male", "Embarked": "C"},
           {"Age": 21, "Sex": "male", "Embarked": "S"}]

r = requests.post(f"{host}/predict", json=payload)
print(r.text)

r = requests.get(f"{host}/wipe")
print(r.text)

# Appendix
# http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

'''
from urlparse import urlparse
from threading import Thread
import httplib

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl
'''