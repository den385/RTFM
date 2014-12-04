import web             #web.py framework
import gateway_front   #python adapter to c++

urls = (
    '/.*', 'hello',    #url pattern for web.py to call hello.GET beneath
    )

class hello:
    def GET(self):
        #some browsers don't like plain text, so I use html
        web.header( 'Content-type', 'text/html' )
        g = gateway_front.Gate() # get gateway to c++
        s = g.hello()            # get 'Hello World' message
        return str(s)            # return it as a HTTP response

#sets web.py's func as WSGI entry point
application = web.application(urls, globals()).wsgifunc()

# to test from console
def main():
    g = backend.Gate()
    s = g.getDefaultQuote()
    print s

if __name__ == '__main__':
    main()
