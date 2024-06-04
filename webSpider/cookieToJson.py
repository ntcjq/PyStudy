import requests
from http.cookies import SimpleCookie
import json
import urllib.parse

cookie_string = "_ga=GA1.1.1748330619.1703596632; kt_tcookie=1; kt_member=a437bd1b0c8dc24d6fd588f74e983eb3; kt_ips=2a09%3Abac5%3A1f0a%3A123c%3A%3A1d1%3Ad6%2C139.162.85.159%2C91.199.87.125%2C159.223.95.228%2C2a09%3Abac5%3A1f0a%3A1246%3A%3A1d2%3A89; PHPSESSID=ep93jfc69rk33hm6jvlfo006k2; __cf_bm=GI974rUUssC_l6XCQskjxnAgLoOJmAVtbcipI7HEOiI-1717508980-1.0.1.1-tfu2Sl2kViWDseR.gUobajXKDZXk.JMQOsLb2lXTYO9TcfygGywaC13zGFh8mAm_uQVSjA0Hti1GIwIKrTZ2yQ; asgfp2=ec0b05a02ca2bcbb7cffe0466ad7661f; cf_clearance=M1P9qFFU_0_MQ.VlSz3QMieQlmG17JS3fvcO6lMQp8Y-1717508983-1.0.1.1-zTxA8HzdqMCRQGDJAl6VecVlMP7nKVy_g0CpwwhEMHiwtdFrKFFEsab6kNPC0kTJfBAm7JOtq8wAKMrlZPHS4w; _ga_1DTX7D4FHE=GS1.1.1717508982.84.1.1717509005.0.0.0"

cookie_string = urllib.parse.unquote(cookie_string)
cookie = SimpleCookie()
cookie.load(cookie_string)

cookie_dict = {key: morsel.value for key, morsel in cookie.items()}
cookie_json = json.dumps(cookie_dict, indent=4)

print(cookie_json)