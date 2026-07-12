class Vehicle():
    def __init__(self, name):
        self.name=name
        print("Vehicle Created")

    def __del__(self):
        print("Vehicle Deleted")

v1=Vehicle("ABc")
print(v1.name)
del v1
print(v1.name)
