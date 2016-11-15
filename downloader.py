#!/usr/bin/env python3

import os

import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import http.cookiejar

from io import StringIO
from zipfile import ZipFile

archive_filename = os.path.join(os.path.dirname(__file__),
                                'archive.zip')

def grab_table_from_web(nucleus):
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

    save_table_in_archive(nucleus, table)
    return table

def save_table_in_archive(nucleus, table):
    with ZipFile(archive_filename, 'a') as f:
        f.writestr(nucleus, table)

def grab_table_from_archive(nucleus):
    with ZipFile(archive_filename, 'r') as f:
        return f.read(nucleus).decode('utf8')

def table_in_archive(nucleus):
    with ZipFile(archive_filename, 'r') as f:
        return nucleus in f.namelist()

def grab_table(nucleus):
    try:
        return grab_table_from_archive(nucleus)
    except (KeyError, IOError):
        return grab_table_from_web(nucleus)

if __name__=='__main__':
    import IPython; IPython.embed()
