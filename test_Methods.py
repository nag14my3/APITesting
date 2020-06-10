import json
import logging
import jsonpath
import pytest
from pip._vendor import requests
from readConfigFile import read_method
from readConfigFile import readpostData

logging.basicConfig(level=logging.DEBUG, filename='test.log',format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S')
logging.info("Test Session has Started")


@pytest.mark.usefixtures('read_method')
def test_getresponse(read_method):
    url = requests.get(read_method['get_link'])
    response = json.loads(url.content)
    assert url.status_code == 200
    id = jsonpath.jsonpath(response, 'data[0].id')
    assert id[0] == 7


logging.info("GET Method status code is 200 & ID value is asserted")


@pytest.mark.usefixtures('readpostData')
def test_postdata(read_method, readpostData):
    url = requests.post(read_method['post_link'], readpostData)
    response = json.loads(url.content)
    postedID = jsonpath.jsonpath(response, 'id')
    logging.info("ID of the Post Method", postedID)
    assert url.status_code == 201
    with open("postop.json", 'w')as outfile:
        json.dump(response, outfile)


logging.info("POST Method status code is 201 & Json Values are read to the post output file")


@pytest.mark.usefixtures('readpostData')
def test_putdata(read_method, readpostData):
    url = requests.put(read_method['put_link'], readpostData)
    response = json.loads(url.content)
    UpdatedTime = jsonpath.jsonpath(response, 'updatedAt')
    print("Updated Time", UpdatedTime)
    assert url.status_code == 200
    with open("putop.json", 'w')as outfile:
        json.dump(response, outfile)


logging.info("PUT Method status code is 200 & Json Values are read to the put output file")


def test_deletedata(read_method):
    url = requests.delete(read_method['delete_link'])
    assert url.status_code == 204


logging.info("DELETE Method status code is 204")

logging.info("Session has Ended")