import sys
import gateway_back # .so object, written in C++ with Boost.Python

#simple singletone
class Gate(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Gate, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    def hello(self):
        return gateway_back.hello() #take hello from c++ backend

# to test from console
def main():
    g = Gate()
    s = g.hello()
    print s

if __name__ == '__main__':
    main()
