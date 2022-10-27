#!/usr/bin/python3
'''
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    basic = HTTPBasicAuth(argv[1], argv[2])
    url = f'https://api.github.com/users/{argv[1]}'
    r = requests.get(url, auth=basic)
    print(r.json().get('id'))
    # print(r.json())
