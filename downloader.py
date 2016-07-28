import urllib
import urllib2
import cookielib

def grab_table(nucleus):
    nucleus = "24Mg"

    data = {'submit':'Retrieve selected datasets',
            '0':'on'
        }


    data = urllib.urlencode(data)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.open('http://www.nndc.bnl.gov/chart/checkENSDFDatasets.jsp?nucleus={}'.format(nucleus))
    response = opener.open('http://www.nndc.bnl.gov/chart/getENSDFDatasets.jsp',data)
    html = response.read()

    begin = '<pre>'
    end = '</pre>'
    table = html[html.index(begin)+len(begin):html.index(end)]
    return table
