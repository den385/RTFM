# location of the Python header files
PYTHON_VERSION = 2.7
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)

# location of the Boost Python include files and library
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib/x86_64-linux-gnu

#compile mesh classes
TARGET = gateway_back
COTARGET = hello_mysql

.PHONY: all clean

all: $(TARGET).so

clean:
        rm -rf *.o;
        rm $(TARGET).so

# (!!!) breaked the string for good formatting @ askubuntu
# important: linking against boost.python, python and connector/c++
# order might be crucial: had to place -lmysqlcppconn at the end
$(TARGET).so: $(TARGET).o $(COTARGET).o
        g++ -shared -Wl,--export-dynamic $(TARGET).o $(COTARGET).o 
        -L$(BOOST_LIB) -lboost_python-py27 
        -L/usr/lib/python$(PYTHON_VERSION)/config 
        -lpython$(PYTHON_VERSION) -o $(TARGET).so -lmysqlcppconn

# (!!!) breaked the string for good formatting @ askubuntu
# important: boost and python includes
$(TARGET).o: $(TARGET).cpp $(COTARGET).cpp
        g++ -I$(PYTHON_INCLUDE) -I$(BOOST_INC) -fPIC -c 
        $(TARGET).cpp $(COTARGET).cpp