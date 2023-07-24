import cgi
from os import curdir, sep
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

from cookies import *
from mysqlConnector import *
from send_mail import send_mail
from file_type import *


logout_butten = '<form action="http://' + domainSite + '" method="post" >'
logout_butten += '<input type="submit" id="logout" value="logout" name="logout">'
logout_butten += '</form>'

class GP(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')

    def do_HEAD(self):
        self._set_headers()
        self.wfile.write(bytes("<html><head><title>daskal</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        file_content = open("html/index.html", "r").read()
        self.do_END(file_content)

    def do_GET(self):
        username_from_cookies = check_cookies_by_username(self)
        result = urllib.parse.parse_qs(self.path[2:])

        type_file = None
        for end in mimetype:
            if self.path.endswith(end):
                type_file = mimetype[end]
        if type_file != None:
            self.send_response(200)
            self.send_header('Content-type', type_file)
            self.end_headers()
            f = open((curdir + sep + self.path), "rb")
            self.wfile.write(f.read())
            f.close()

        elif self.path.endswith("icomoon.ttf?10si43"):
            self.send_response(200)
            self.send_header('Content-type', 'font/ttf')
            self.end_headers()
            f = open((curdir + sep + "fonts/icomoon/fonts/icomoon.ttf"), "rb")
            self.wfile.write(f.read())
            f.close()
            return
        elif self.path.endswith("icomoon.woff?10si43"):
            self.send_response(200)
            self.send_header('Content-type', 'font/woff')
            self.end_headers()
            f = open((curdir + sep + "fonts/icomoon/fonts/icomoon.woff"), "rb")
            self.wfile.write(f.read())
            f.close()
            return
        elif self.path.endswith("bootstrap.min.css%22"):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            f = open((curdir + sep + "css/bootstrap.min.css"), "rb")
            self.wfile.write(f.read())
            f.close()
            return
        elif self.path.endswith("bootstrap.min.css.map%22"):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            f = open((curdir + sep + "css/bootstrap.min.css.map"), "rb")
            self.wfile.write(f.read())
            f.close()
            return
        else:
            if not self.path == "/":
                print(self.path)

        if not result == {}:
            try:
                get_url_key = result['ResetPassword'][0]
                if result['ResetPassword'][0] != "":
                    print(get_url_key)
                    username = get_url_from_email(result['ResetPassword'][0])
                    if username != None:
                        print(username)
                        file_content = open("html/reset_password.html", "r").read()
                        file_content = file_content.format(url_site="http://" + domainSite)
                        file_content = file_content % ("")
                    else:
                        file_content = open("html/reset_password.html", "r").read()
                        file_content = file_content.format(url_site="http://" + domainSite)
                        file_content = file_content % ("<p style=\"color:red;\"> The URL IS incorrect.</p>")
                else:
                    print("No result")
                    file_content = open("html/reset_password.html", "r").read()
                    file_content = file_content.format(url_site="http://" + domainSite)
                    file_content = file_content % ("<p style=\"color:red;\"> The URL IS incorrect.</p>")
            except:
                print("Err GET parameters")

        elif self.path.startswith("/product_list"):
            file_content = open("html/product_list.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            print(file_content)

        elif self.path.startswith("/register"):
            file_content = open("html/register.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/login"):
            file_content = open("html/login.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/test"):
            file_content = open("html/test.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif username_from_cookies is not None:
            #file_content = "<p>Wellcome " + get_firstname_and_lastname(username_from_cookies) + "</p>"
            file_content = open("html/index.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite, wellcom_user="Wellcome " + get_firstname_and_lastname(username_from_cookies), butten=logout_butten, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))

        elif self.path.startswith("/about"):
            file_content = open("html/about.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/product"):
            file_content = open("html/product.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/service"):
            file_content = open("html/service.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/gallery"):
            file_content = open("html/gallery.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/contact"):
            file_content = open("html/contact.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/forgot_password"):
            file_content = open("html/forgot_password.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/change_password"):
            file_content = open("html/change_password.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")

        elif self.path.startswith("/hacked_login"):
            file_content = open("html/hacked_login.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite)
            file_content = file_content % ("")
        else:
            file_content = open("html/index.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite, wellcom_user="", butten="")
            file_content = file_content % ("")

        self._set_headers()
        self.do_END(file_content)

    def do_POST(self):
        # self.do_HEAD()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        self._set_headers()

        if form.getvalue('logout'):
            if delete_cookies(self):
                print("delete cookies")
                file_content = open("html/index.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, wellcom_user="", butten="")
                file_content = file_content % ("")
            else:
                print("Err Delete cookies")
                file_content = open("html/onLogin.html", "r").read()
                file_content += file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
        elif form.getvalue('add_store'):
            add_store(form.getvalue("store_name"), form.getvalue("street"), form.getvalue("city"), form.getvalue("phone"), form.getvalue("owner"))
            file_content = open("html/product_list.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))

        elif form.getvalue('search_form'):
            file_content = open("html/product_list.html", "r").read()
            file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(form.getvalue("search")), table_trust=table_store_by_name_trust(""))

        elif form.getvalue('search_form_trust'):
            if validation(form.getvalue("search_trust")):
                file_content = open("html/product_list.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(form.getvalue("search_trust")))
            else:
                file_content = open("html/product_list.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust="<p style=\"color:red;\"> Err validation Input</p>")

        elif form.getvalue('hacked_login'):
            if hacked_auction(form.getvalue("username"), form.getvalue("password")):
                print("OK Login")
                cookie_local = create_cookies(form.getvalue("username"))
                for morsel in cookie_local.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                file_content = open("html/onLogin.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            else:
                print("On Login")
                file_content = open("html/hacked_login.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite)
                file_content = file_content % ("<p style=\"color:red;\"> The UserName or Password are incorrect.</p>")


        elif form.getvalue("TypeForm") == "Login":
            if authentication(form.getvalue("username"), form.getvalue("password")):
                print("OK Login")
                cookie_local = create_cookies(form.getvalue("username"))
                for morsel in cookie_local.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                file_content = "<p>Wellcome " + get_firstname_and_lastname(form.getvalue("username")) + "</p>"
                file_content += open("html/onLogin.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            else:
                print("On Login")
                # file_content = ""
                file_content = open("html/login.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite)
                file_content = file_content % ("<p style=\"color:red;\"> The UserName or Password are incorrect.</p>")

        elif form.getvalue("TypeForm") == "Register":
            if register(form.getvalue("username"), form.getvalue("password"), form.getvalue("passwordRepeat"),
                        form.getvalue("email"), form.getvalue("phone"), form.getvalue("firstName"),
                        form.getvalue("lastName")):
                cookie_local = create_cookies(form.getvalue("username"))
                for morsel in cookie_local.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                file_content = "<p> your ditels: Username: " + form.getvalue("username") + "  E-mail: " + form.getvalue(
                    "email") + "  Phone Number: " + form.getvalue("phone") + "</p>"
                file_content += "<p> Hi: " + form.getvalue("firstName") + " " + form.getvalue(
                    "lastName") + "  Wellcome </p>"
                file_content += open("html/onLogin.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            else:
                file_content = open("html/register.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite)
                file_content = file_content % ("<p style=\"color:red;\"> The UserName or Password are incorrect.</p>")

        elif form.getvalue("TypeForm") == "change_password":
            if retry_password(form.getvalue("username"), form.getvalue("password"), form.getvalue("new_password"),form.getvalue("password_repeat")):
                print("OK auction")
                cookie_local = create_cookies(form.getvalue("username"))
                for morsel in cookie_local.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                file_content = "<p>Wellcome " + get_firstname_and_lastname(form.getvalue("username")) + "</p>"
                file_content += open("html/onLogin.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            else:
                print("On auction")
                # file_content = ""
                file_content = open("html/change_password.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite)
                file_content = file_content % ("<p style=\"color:red;\"> The UserName or Password are incorrect.</p>")


        elif form.getvalue("TypeForm") == "ForgotPassword":
            if validation(form.getvalue("username")):
                if send_mail(form.getvalue("username")):
                    print("send email")
                    file_content = "<center><h1>send You Email To Reset Password.</h1></center>"
                else:
                    print("No send Email")
                    file_content = open("html/forgot_password.html", "r").read()
                    file_content = file_content.format(url_site="http://" + domainSite)
                    file_content = file_content % ("<p style=\"color:red;\"> The UserName is incorrect.</p>")
            else:
                print("username is not corect")
                file_content = open("html/forgot_password.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite)
                file_content = file_content % ("<p style=\"color:red;\"> The UserName is incorrect.</p>")

        elif form.getvalue("TypeForm") == "ResetPassword":
            if reset_password(form.getvalue("username"), form.getvalue("code"), form.getvalue("password"),
                              form.getvalue("re_password")):
                print(" change password")
                cookie_local = create_cookies(form.getvalue("username"))
                for morsel in cookie_local.values():
                    self.send_header("Set-Cookie", morsel.OutputString())
                # print(form.getvalue("username"))
                # print(get_firstname_and_lastname(form.getvalue("username")))
                file_content = "<p>Wellcome " + get_firstname_and_lastname(form.getvalue("username")) + "</p>"
                file_content += open("html/onLogin.html", "r").read()
                file_content = file_content.format(url_site="http://" + domainSite, table=table_store_by_name(""), table_trust=table_store_by_name_trust(""))
            else:
                print("on change password")
                file_content = open("html/login.html", "r").read()
        self.do_END(file_content)
        # self.end_headers()
        # self.wfile.write(bytes(file_content, encoding='utf8'))

    def do_END(self, file_content):
        self.end_headers()
        self.wfile.write(bytes(file_content, encoding='utf8'))
        # mysqldb.close()


def runHTTPServer(server_class=HTTPServer, handler_class=GP, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:80...')
    httpd.serve_forever()


runHTTPServer()
