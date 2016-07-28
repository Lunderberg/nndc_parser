import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import http.cookiejar

def grab_table(nucleus):
    nucleus = "24Mg"

    data = {'submit':'Retrieve selected datasets',
            '0':'on'
        }


    data = urllib.parse.urlencode(data).encode('ascii')
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.open('http://www.nndc.bnl.gov/chart/checkENSDFDatasets.jsp?nucleus={}'.format(nucleus))
    response = opener.open('http://www.nndc.bnl.gov/chart/getENSDFDatasets.jsp',data)
    html = response.read().decode('ascii')

    begin = '<pre>'
    end = '</pre>'
    table = html[html.index(begin)+len(begin):html.index(end)]
    return table
