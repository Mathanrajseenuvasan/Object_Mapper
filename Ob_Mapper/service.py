import requests
import json



class Request(object):

    @staticmethod
    def request_url():
        url = "http://dummy.restapiexample.com/api/v1/employees"
        dump = requests.get(url, headers={"User-Agent": "XY"})
        response = dump.json()
        return response



