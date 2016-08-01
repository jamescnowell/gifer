import webbrowser
import sys
url = r'https://www.google.com/search?espv=2&biw=1280&bih=1303&tbs=itp%3Aanimated&tbm=isch&sa=1&q=REPLACE_STRING&oq=REPLACE_STRING&gs_l=img.3..0l10.22603.150807.0.151047.14.10.1.3.3.0.129.651.9j1.10.0....0...1c.1.64.img..0.14.661...0i30j0i5i30.abGf33oteBo'
args = sys.argv[1:]
test = url.replace('REPLACE_STRING', '+'.join(args))
webbrowser.open(test)
