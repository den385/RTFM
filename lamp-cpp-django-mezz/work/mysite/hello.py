from django.http import HttpResponse

import gateway

def test(request):
    text = str( gateway.Gate().hello() )
    return HttpResponse( text, content_type="text/plain" )

def main():
    g = gateway.Gate()
    s = g.getDefaultQuote()
    print s

if __name__ == '__main__':
    main()
