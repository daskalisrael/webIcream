from mysqlConnector import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# smtp_username = "server@daskal.co.il"
# smtp_password = "D@sk@l32!"
# smtp_host = "smtp.daskal.co.il:25"

def send_mail(username):
    try:
        msg = MIMEMultipart()
        msg['From'] = "server@daskal.co.il"
        msg['To'] = get_email_by_username(username)
        msg['Subject'] = "Reset Password To WebSite"
        SingleSignOn, LinkFromEmail = single_sign_on(username)
        LinkFromEmail = "http://" + domainSite + "/?ResetPassword=" + LinkFromEmail
        message = """
        MIME-Version: 1.0" . "\r\n
        Content-type:text/html;charset=UTF-8
        <html><head><title>send mail</title></head><body>
        <center>
        <h2>Reset Login Form E-mail</h2>
        <h3>hello %s </h3>
        <h4> if you want to reset your password the code is</h4>
        <h2> %s </h2>
        <h2> To reset Password you Need link On <a href="%s">Reset Password</a> </h>
        </center>
        </body></html>
        """ % (get_firstname_and_lastname(username), SingleSignOn, LinkFromEmail)
        # msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText(message, 'html'))
        server = smtplib.SMTP(smtp_host)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Successfully sent email message to %s:" % (msg['To']))
        return True
    except:
        return False

# print(send_mail("daskal"))
