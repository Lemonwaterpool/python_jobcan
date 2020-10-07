import requests
import getpass
from bs4 import BeautifulSoup

email = input('Enter your email: ')
password = getpass.getpass('Enter your password: ')

login_url = 'https://id.jobcan.jp/users/sign_in'
session = requests.session()
response = session.get(login_url)
bs = BeautifulSoup(response.text, 'html.parser')

authenticity = bs.find(attrs={'name':'authenticity_token'}).get('value')
cookie = response.cookies

print(authenticity)

info = {
    "authenticity_token": authenticity,
    "user[email]": email,
    "user[password]": password,
}

login_res = session.post(login_url, data=info, cookies=cookie)
print(login_res.status_code)
