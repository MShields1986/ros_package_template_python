#!/usr/bin/env python3

class MyClass:
    """
    MyClass is a class that provides some examples of the types attributes and methods you might need.
    
    Attributes:
        arg1 (type): Description of arg1
        arg2 (type): Description of arg2
        arg3 (type): Description of arg3
    """
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

        self._class_property = None

        private_val = 1

        self.connected = False


    def my_method(self, arg):
        return result


    @property
    def class_property(self):
        return self._class_property


    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2


    @classmethod
    def modify_private_list(cls, new_val):
        cls.private_val = new_val


    def __enter__(self):
        self.resource = self.acquire_resource(self.arg1, self.arg2)

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release_resource()


    def __iter__(self):
        item = f"An item | init arg3: {self.arg3}"
        yield item


    def acquire_resource(self, arg1, arg2):
        self.connected = True


    def release_resource(self):
        self.connected = False



if __name__ == '__main__':
    try:
        with MyClass("arg1", "arg2") as instance:
            for item in instance:
                print(item)

    except Exception as e:
        print(e)
