#!/usr/bin/python3
'''
a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
'''


if __name__ == '__main__':
    import urllib.request
    from sys import argv
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode())
    except HTTPError as e:
        print(f'Error code: {e.code}')
