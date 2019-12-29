import requests
import json
from mapper import request


class Request(object):

    @staticmethod
    def request_url():
        url = "http://dummy.restapiexample.com/api/v1/employees"
        dump = requests.get(url, headers={"User-Agent": "XY"})
        response = dump.json()
        return response

    @staticmethod
    def request_data(data):
        response = request(data)
        return response.test
