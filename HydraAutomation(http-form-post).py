import requests
import sys
import mechanize
reload(sys)
sys.setdefaultencoding('utf-8')
URL = sys.argv[1]
request = requests.get(URL)
x = request.text

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ''

def find_between_r(s, first, last): 
    try:
        start = s.rindex(first) + len(first)
        end = s.rindex(last, start)
        return s[start:end]
    except ValueError:
        return ''
		
source = str(request.text)
passIndex = '<input type=' + '"' + 'password' + '"'
nameIndex = 'name=' + '"'
line = (find_between(source, passIndex,'/>'))
name = (find_between(line, nameIndex, '"'))
P = name
PASS = name + '=^PASS^'

userIndexTypeA = '<input type=' + '"' + 'email' + '"'
userIndexTypeB = '<input type=' + '"' + 'text' + '"'
line = (find_between_r(source, userIndexTypeA, passIndex))
if line in "":
	line = (find_between_r(source, userIndexTypeB, passIndex))
else:
	line = (find_between_r(source, userIndexTypeA, passIndex))
name = (find_between(line, nameIndex,'"'))
U = name
USER = name + '=^USER^'

formIndex = '<form '
actionIndex = 'action=' + '"'
line = (find_between_r(source, formIndex, passIndex))
name = (find_between(line, actionIndex,'"'))
ACTION = '"' + name + ':'

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)
browser.open(URL)
browser.select_form(nr = 0)
browser.form[U] = 'value'
browser.form[P] = 'value'
response = browser.submit()
y = response.read()
i = 0 
for i in xrange(len(x)):
	if x[i] != y[i]: 
		break
ERROR = ':' + str(find_between(y[i:], '>', '<')) + '"'
RUN = 'hydra ' + URL + ' http-form-post ' + ACTION + USER + '&' + PASS + ERROR + ' -L user.txt -P pass.txt -t 10'
print "--------------------------------------------" + '\n' + 'HYDRA COMMAND AUTOMATER RESULTS:' + '\n' + ACTION + '\n' + USER + '\n' + PASS + '\n' + ERROR + '\n\n' + RUN
