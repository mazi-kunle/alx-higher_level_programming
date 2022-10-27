#!/usr/bin/python3
'''
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
'''
if __name__ == '__main__':
    import requests
    from sys import argv

    data = {'q': None}
    if len(argv) == 1:
        data['q'] = ''
    else:
        data['q'] = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user',
                      data=data)
    try:
        json_data = r.json()
    except requests.exceptions.JSONDecodeError:
        print('Not a  valid JSON')
    else:
        if (len(json_data) == 0):
            print('No result')
        else:
            print('[{}] {}'.format(json_data.get('id'),
                  json_data.get('name')))
