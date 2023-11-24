class Test:
    _instance = None

    def __new__(cls):
        print("Get Instance")

        if not cls._instance:
            print("Create instance")
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        print("Init")


def singleton(class_):
    """singleton decorator"""
    instances = {}

    def getinstance(*args, **kwargs):
        print("Get Instance")
        if class_ not in instances:
            print("Create instance")
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class SingleTest:
    def __init__(self):
        print("Init")


print()
print("SINGLETON CON NEW:")
Test()
Test()
Test()

print()
print("SINGLETON CON DECORATOR:")
SingleTest()
SingleTest()
SingleTest()
