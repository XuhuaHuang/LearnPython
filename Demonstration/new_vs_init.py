# Topic: The relations between two dunder methods
# __new__ vs. __init__
# File: fun_new_init.py
#
# Author: Xuhua Huang
# Last updated: Oct 19, 2021
# Created on: Sept 27, 2021

class Singleton:
    _instance = None;

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


def singleton_example():
    print("Singleton Example")
    x = Singleton()
    y = Singleton() # obtain 2 identical instance
    print(f"{x is y = }")
    return


# Client Caching Example
# suppose that an Client object is expensive to copy and initialize
class Client:
    _loaded: dict = {}
    _db_file: str = 'external_file.db'

    def __new__(cls, client_id: int):
        if (client := cls._loaded.get(client_id)) is not None:
            print(f"Returning existing client {client_id} from cache")
            return client
        else:
            client = super().__new__(cls)
            cls._loaded[client_id] = client
            client._init_from_file(client_id, cls._db_file)
            return client

    def _init_from_file(self, client_id: int, file: str):
        # lookup client in parsed file and read properties
        print(f"Reading client {client_id} data from {file}")
        name = ...
        email = ...
        self._name: str = name
        self._email: str = email
        self._id: int = client_id


def main():
    singleton_example()

    # Demonstration of class Client
    x = Client(0)
    y = Client(0)
    print(f"{x is y = }")
    z = Client(1)


if __name__ == '__main__':
    main()
