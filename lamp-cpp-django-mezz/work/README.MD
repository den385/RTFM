work folder has this structure:

work
|
+-www
| |
| +-mysite@ [symlink to ../myproject/mysite dir, for apache and neatness]
|
+-mysite
| |
| +-deploy/    [mezzanine deploy stuff]
| +-static/    [static files we collected]
| +-fabfile.py [script that creates mezzanine-project]
| +-hello.py   [script for testing service output]  
| +-local_settings.py [mezzanine site-specific settings]
| +-settings.py [django settings with mezzanine addon]
| +-manage.py   [management script wrapping calls to django admin functions]
| +-urls.py     [url patterns]
| +-wsgi.py     [wsgi entry point]
| +-gateway.py  [in here I import wrapped C++]
| +-__init__.py [to treat dir as python module]
|   
+-backend [c++ backend is in separate folder]
  |
  +-gateway.cpp [Boost.Python wrapping code]
  +-hello_mysql.cpp [adapter to DB]
  +-gateway_back.o [object file after compilation]
  +-hello_mysql.o [object file after compilation]
  +-gateway_back.so [this will be a module for python]
  +-Makefile [cause Boost.Python works w/ python by an .so object]
  +-__init__.py [to import backend into python app]