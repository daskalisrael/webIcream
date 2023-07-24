from configCharacter import *
import http.cookies
import uuid
import datetime

cookies_jar = {}


def check_cookies_by_username(self):
    cookie_header = self.headers.get("Cookie")
    # print("cookie_header: ", cookie_header)
    if cookie_header is not None:
        coockies = http.cookies.SimpleCookie(cookie_header).values()
        for morsel in coockies:
            if morsel.key == "session":
                try:
                    return cookies_jar.get(morsel.value)["username"]
                except:
                    print("ERR cookie was not found")
    return None


def delete_cookies(self):
    cookie_header = self.headers.get("Cookie")
    if cookie_header is not None:
        coockies = http.cookies.SimpleCookie(cookie_header).values()
        for morsel in coockies:
            if morsel.key == "session":
                # print(morsel.value)
                cookies_jar.pop(morsel.value)
                return True
    return False


def create_cookies(username):
    cookie_str = str(uuid.uuid4())
    cookies_jar[cookie_str] = {"username": username}
    cookie = http.cookies.SimpleCookie()
    cookie['session'] = cookie_str
    cookie['session']['domain'] = domainSite
    cookie['session']['path'] = '/'
    expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutesExpiresCookies)  # expires in 5 minutes
    cookie['session']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return cookie
