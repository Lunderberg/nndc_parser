#!/usr/bin/env python2

from downloader import grab_table
from parsers import Level, Transition, parse_table

table = grab_table('24Mg')
parsed = parse_table(table)
import IPython; IPython.embed()
