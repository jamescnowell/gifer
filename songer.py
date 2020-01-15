#!/usr/bin/env python

import webbrowser
import sys
url = r'https://www.youtube.com/results?search_query='
args = sys.argv[1:]
test = url + '+'.join(args)
webbrowser.open(test)
