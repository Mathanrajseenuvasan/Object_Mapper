from Mapper.object_mapper import ObjectMapper
from service import Request


class Request_Json():
    def __init__(self):
        self.total = []
        request_json = Request.request_url()
        for i in request_json:
            condense = {
                "name":i['employee_name'],
                "age":i['employee_age']
            }
            self.total.append(condense)
            

class Response_Json():
    def __init__(self):
        self.total = []
        

mapper = ObjectMapper()
# mapper.create_map(Request_Json, Response_Json,{'total': (lambda x:x.total)})
mapper.create_map(Request_Json, Response_Json,{'total': (lambda x:x.total)})
instance_b = mapper.map(Request_Json(), Response_Json, allow_unmapped=True)
