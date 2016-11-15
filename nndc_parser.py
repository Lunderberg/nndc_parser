#!/usr/bin/env python3

from downloader import grab_table
from parsers import Level, Transition, parse_table
from plotter import plot_table

table = grab_table('24Mg')
parsed = parse_table(table)
plot_table(parsed)
import IPython; IPython.embed()
