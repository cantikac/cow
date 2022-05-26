import requests as req, re

"""

Copyright © 2021 - 2023 | Latip176
Semua codingan dibuat oleh Latip176.

"""

class Main:
	
	import requests as req, re

"""

Copyright © 2021 - 2023 | Latip176
Semua codingan dibuat oleh Latip176.

"""

class Main:
	
	def convert(cookie):
	cookies = {"cookie":cookie}
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
		'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		'referer'	:	'https://www.facebook.com/',
		'host'	:	'business.facebook.com',
		'origin'	:	'https://business.facebook.com',
		'upgrade-insecure-requests'	:	'1',
		'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'	:	'max-age=0',
		'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'	:	'text/html; charset=utf-8'
	}, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',str(res.text)).group(1)
			if "EAAG" in __token:
				return __token
			else:
				return "Cookies Invalid"
		except AttributeError:
			return "Cookies Invalid"
			if "EAAG" in __token:
				return __token
			else:
				return "Cookies Invalid"
		except AttributeError:
			return "Cookies Invalid"
