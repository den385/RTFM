work folder has this structure:

work
|
+-www
| |
| +-mysite@ [symlink to ../myproject/mysite dir, for apache and neatness]
|
+-mysite
| |
| +-myproject_front.py [that's WSGI entry point]
| +-gateway_front.py [in here I import wrapped C++]
| +-__init__.py [to treat dir as python module]
|   
+-mysite_back [c++ backend is in separate folder]
  |
  +-gateway_back.cpp [Boost.Python wrapping code]
  +-hello_mysql.cpp [adapter to DB]
  +-gateway_back.o [object file after compilation]
  +-hello_mysql.o [object file after compilation]
  +-gateway_back.so [this will be a module for python]
  +-Makefile [cause Boost.Python works w/ python by an .so object]