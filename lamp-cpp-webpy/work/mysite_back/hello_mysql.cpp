#include <stdlib.h>
#include <iostream>
#include <string>

#include "mysql_connection.h"

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>

using namespace std;

char const* hello()
try {
  sql::Driver *driver;
  sql::Connection *con;
  sql::Statement *stmt;
  sql::ResultSet *res;

  /* Create a connection */
  driver = get_driver_instance();

  // MySQL IP address and your username
  con = driver->connect("tcp://127.0.0.1:3306", "username", "username");
  /* Connect to the MySQL test database */
  con->setSchema("test"); //your db name

  stmt = con->createStatement();
  res = stmt->executeQuery("SELECT * from hello;");

  string result;

  while (res->next()) {
    /* Access column data by alias or column name */
    result = res->getString("msg");  // field in db with actual 'Hello World'
    return result.c_str();
  }
  delete res;
  delete stmt;
  delete con;

} catch (sql::SQLException &e) {
  cerr << "# ERR: SQLException in " << __FILE__;
  cerr << "(" << __FUNCTION__ << ") on line "
     << __LINE__ << endl;
  cerr << "# ERR: " << e.what();
  cerr << " (MySQL error code: " << e.getErrorCode();
  cerr << ", SQLState: " << e.getSQLState() << " )" << endl;
}
