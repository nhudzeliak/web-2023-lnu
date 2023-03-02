class Singleton:
    _instance = None

    def __init__(self):
        pass

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def some_method():
        print("This is a Singleton class")


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)

s1.some_method()
