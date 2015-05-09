#! /usr/bin/python3.4


import http.client
import re

def get_page(env):
    conn = http.client.HTTPConnection(url)

    conn.request(env['REQUEST_METHOD'] ,"/index.html")

def is_Get_Method(env):
    if env['REQUEST_METHOD'] == 'GET':
        return True
    else:
        return False

def get_uri(env):
    uri = env['REQUEST_URI']
    prefix = "/proxy/"
    if uri.startswith(prefix):
        uri =  uri[len(prefix):]
    return uri


def get_url_and_urn( uri ):
    #pattern = "^(http[s]?|ftp):\/?\/?([^:\/\s]+)(:([^\/]*))?((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(\?([^#]*))?(#(.*))?$"
    pattern = "^(?P<port>http[s]?):\/?\/?(?P<url>[^:\/\s]+)?(?P<urn>.*)$"
    regex = re.compile(pattern)
    m = regex.search( uri )
    #print("m",m)
    if m is not None:
        res = m.groupdict()
        #print("res",res)
        return res

def return_page(env, dic):
    url = dic["url"]
    print(url)
    conn = http.client.HTTPConnection(url)
    conn.request( env['REQUEST_METHOD'] , dic["urn"] )
    rep = conn.getresponse()
    response_body =  rep.read()
    conn.close()
    return reponse_body.encode("utf-8")


def application(env, start_response):
    status = '200 OK'
    #response_body = 'The request method was %s' % env['REQUEST_METHOD']
    #response_body = str(env.keys())
    response_body = str([env['PATH_INFO'] , env['REQUEST_URI'] ,env['REQUEST_METHOD'] , env['HTTP_ACCEPT_ENCODING'] ,  env['HTTP_USER_AGENT'] ,  env['CONTENT_TYPE'] ,  env['QUERY_STRING'] , env['HTTP_ACCEPT'] , env['CONTENT_TYPE'] , env['DOCUMENT_ROOT']   ])

    uri  =  get_uri(env)
    dic = get_url_and_urn( uri )
    page = return_page(env,dic)

    response_headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return page
    #return [response_body.encode("utf-8")]
