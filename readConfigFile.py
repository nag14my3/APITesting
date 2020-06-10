import json

import pytest


@pytest.fixture()
def read_method():
    with open('URL.json') as read_data:
        read_methoddata = json.load(read_data)
    return read_methoddata

@pytest.fixture()

def readpostData():
    with open('postData.json','r') as read_data:
        read_methoddata = read_data.read()
        request_json=json.loads(read_methoddata)
        print(request_json)
    return request_json