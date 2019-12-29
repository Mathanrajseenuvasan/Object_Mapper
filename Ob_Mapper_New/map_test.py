from Mapper.object_mapper import ObjectMapper
data = {
    "name": "mathan"
}, {
    "name": "suresh"
}


def test():
    res = data
    for i in res:
        print(i)


class Aa():
    def __init__(self, test):
        self.test = test


a = Aa(data)


class A():
    def __init__(self, test):
        self.test = []
        for i in test:
            print(i)
            self.test.append(i)

class B():
    def __init__(self):
        self.test = []


mapper = ObjectMapper()
mapper.create_map(A, B)
instance_b = mapper.map(A(data), B,allow_unmapped=True)
print("instance_b",instance_b.test)
