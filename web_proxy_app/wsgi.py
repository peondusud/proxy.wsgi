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
    if uri.startswith("/api/"):
        uri =  uri[5:]
    return uri


def get_url_and_urn( uri ):
    #pattern = "^(http[s]?|ftp):\/?\/?([^:\/\s]+)(:([^\/]*))?((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(\?([^#]*))?(#(.*))?$"
    pattern = "^(http[s]?|ftp):\/?\/?([^:\/\s]+)(:([^\/]*))?(.*?)$"
    regex = re.compile(pattern) 
    m = regex.search(uri)
    print(m)
    res = m.groups()
    print(res)
    protocol = res[0]
    url = res[1]
    port = res[3]
    urn = res[4]

    return url, urn

def return_page(env):
    response_body =  None
    return reponse_body.encode("utf-8")


def application(env, start_response):
    status = '200 OK'
    response_body = 'The request method was %s' % env['REQUEST_METHOD']
    response_body = str(env.keys())
    response_body = str([env['PATH_INFO'] , env['REQUEST_URI'] ,env['REQUEST_METHOD'] , env['HTTP_ACCEPT_ENCODING'] ,  env['HTTP_USER_AGENT'] ,  env['CONTENT_TYPE'] ,  env['QUERY_STRING'] , env['HTTP_ACCEPT'] , env['CONTENT_TYPE'] , env['DOCUMENT_ROOT']   ])
    
    uri  =  get_uri(env)
    print(uri)
    url, urn = get_url_and_urn( uri )
    http.client.HTTPConnection(url)
    response_headers = [('Content-Type', 'text/plain'),('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    #print("ca rentre")
    return [response_body.encode("utf-8")]
