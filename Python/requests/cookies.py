import requests
url = "https://www.polito.it/"

res = requests.get(url)
cookies = res.cookies

print(cookies)
