#!/usr/bin/python3
'''
This is a module
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    url = f' https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    r = requests.get(url)
    data = r.json()
    for i in range(10):
        print('{}: {}'.format(data[i]['sha'],
              data[i]['commit']['author']['name']))
