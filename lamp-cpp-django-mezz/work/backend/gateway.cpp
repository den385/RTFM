#include <boost/python.hpp>

extern char const* hello();

BOOST_PYTHON_MODULE(gateway)
{
  using namespace boost::python;
  def("hello", hello);
}
