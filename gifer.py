#!/usr/bin/env python

import webbrowser
import sys
url = r'https://www.google.com/search?tbm=isch&tbs=itp:animated&q='
args = sys.argv[1:]
test = url + '+'.join(args)
webbrowser.open(test)
