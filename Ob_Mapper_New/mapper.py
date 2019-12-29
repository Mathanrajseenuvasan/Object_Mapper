from Mapper.object_mapper import ObjectMapper

test = []

class Request_data():
    def __init__(self):
        self.test = test
        self.check = "check"


class Response_data():
    def __init__(self):
        self.test = None
        self.check = None


def request(data):
    test.append(data)
    mapper = ObjectMapper()
    mapper.create_map(Request_data, Response_data)
    instance_Response_data = mapper.map(
        Request_data(), Response_data, allow_unmapped=True)
    return instance_Response_data
