#With love, Abhilash Panigrahi.
import requests
url = "http://phc.prontonetworks.com/cgi-bin/authlogout"
s = requests.Session()
s.get(url)
