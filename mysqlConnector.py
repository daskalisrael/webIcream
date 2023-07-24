# ishay2012@gmail.com

import time
import datetime
import random
import mysql.connector
import hashlib
import binascii
import os
import pytz

from check_character import *

mysqldb = mysql.connector.connect(
    host=dbHost,
    user=dbUser,
    password=dbPassword,
    database=databaseName
)

my_cursor = mysqldb.cursor()


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    passwordHash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    passwordHash = binascii.hexlify(passwordHash)
    return (salt + passwordHash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password


def add_incorrect_login(username):
    now = datetime.datetime.now(pytz.timezone('Asia/Jerusalem')).strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO history_incorrect_login (username, date) VALUES (%s, %s)"
    val = (username, now)
    my_cursor.execute(sql, val)
    mysqldb.commit()
    if my_cursor.rowcount > 0:
        print("add password to history table")
        return True
    else:
        print("err no insert history login")
        return False
    # expires_url = (datetime.datetime.now(pytz.timezone('Asia/Jerusalem')) + datetime.timedelta(
    #     minutes=timeToExpiresUrl)).strftime('%Y-%m-%d %H:%M:%S')
# add_incorrect_login("daskal")

def max_incorrect_login(username):
    sql = "SELECT * FROM website.history_incorrect_login where DATE(date) = DATE(NOW()) AND username =\"{name}\"".format(name=username)
    my_cursor.execute(sql)
    my_result = my_cursor.fetchall()
    if len(my_result) >= maxIncorrectLogin:
        return False
    else:
        return True
# print(max_incorrect_login("daskal"))

def add_history_password(username, password):
    sql = "INSERT INTO history_password (username, password, date) VALUES (%s, %s, %s)"
    val = (username, hash_password(password), int(time.time()))
    my_cursor.execute(sql, val)
    mysqldb.commit()
    # mysqldb.close()
    if my_cursor.rowcount > 0:
        print("add password to history table")
        return True
    return False


def check_password_history(username, password):
    sql = "Select password from website.history_password where username = %s ORDER BY date DESC LIMIT %s;"
    val = (username, maxHistoryPassword)
    # print(sql, val)
    my_cursor.execute(sql, val)
    my_result = my_cursor.fetchall()
    for stored_password in my_result:
        if verify_password(stored_password[0], password):
            print("find password on history")
            return False
    print("No find password")
    return True


def authentication(username, password):
    if validation(username) and validation(password) and max_incorrect_login(username):
        sql = "SELECT password FROM username WHERE `username` = \"{name}\"".format(name=username)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        for stored_password in my_result:
            if verify_password(stored_password[0], password):
                return True
            else:
                add_incorrect_login(username)
                print("The password from username: " + username + " are incorectly")
                return False
        print("no user on sql")
        return False
    else:
        print("no validation")
        return False


def hacked_auction(username, password):
    if username != "" and password != "":
        sql = "SELECT username FROM hacked_users WHERE `username` = " + '"' + username + '"' + " AND `password` = " + '"' + password + '"'
        print(sql)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        if len(my_result) != 0:
            return True
            print("hacked login OK")
        print("no user on hacked sql")
        return False
    else:
        print("no user or password")
        return False


# t" or "a" = "a
# print(hacked_auction("test", "test"))

def change_password(username, password):
    if check_password_history(username, password):
        sql = "UPDATE website.username SET password = %s WHERE username = %s"
        val = (hash_password(password), username)
        my_cursor.execute(sql, val)
        mysqldb.commit()
        if my_cursor.rowcount >= 0:
            print("change password")
            return add_history_password(username, password)
    print("no change password")
    return False


# print(change_password("daskal", "W@q1w2e3"))

def register(username, password, password_repeat, email, phone, first_name, last_name):
    if password != password_repeat:
        print("password not mash")
        return False
    else:
        validationOK = True
        if not checkUsername(username):
            validationOK = False
        if not checkPassword(password):
            validationOK = False
        if not validation(first_name):
            validationOK = False
        if not validation(last_name):
            validationOK = False
        if not validation(email):
            validationOK = False
        if not checkPhone(phone):
            validationOK = False
        # print(username, hash_password(password), email, phone, firstName, lastName)
        if validationOK:
            print("validationOK")
            sql = "SELECT username FROM username WHERE `username` = \"{name}\"".format(name=username)
            my_cursor.execute(sql)
            my_result = my_cursor.fetchall()
            for user in my_result:
                if user[0] == username:
                    print("you have the sum username", user[0])
                    return False
            sql = "INSERT INTO username (username, password, email, phone, firstName, lastName) VALUES (%s, %s, %s, " \
                  "%s, %s, %s) "
            val = (username, hash_password(password), email, phone, first_name, last_name)
            my_cursor.execute(sql, val)
            mysqldb.commit()
            # mysqldb.close()
            if my_cursor.rowcount > 0 and add_history_password(username, password):
                print("register User")
                return True
            else:
                print("No register User")
                return False


def get_firstname_and_lastname(username):
    sql = "SELECT firstName, LastName FROM username WHERE `username` = \"{name}\"".format(name=username)
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    # mysqldb.close()
    if len(result) >= 1:
        for user in result:
            FullName = user[0] + " " + user[1]
            return FullName
    return None


def get_email_by_username(username):
    sql = "SELECT email FROM username WHERE `username` = \"{name}\"".format(name=username)
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    # mysqldb.close()
    if len(result) >= 1:
        for user in result:
            email = user[0]
            return email
    return None


def retry_password(username, password, new_password, password_repeat):
    changePassword = False
    validationOK = True
    if not validation(username):
        validationOK = False
    if not validation(password):
        validationOK = False
    if not checkPassword(new_password):
        validationOK = False
    if new_password == password_repeat and validationOK:
        sql = "SELECT password FROM username WHERE `username` = \"{name}\"".format(name=username)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        for stored_password in my_result:
            if verify_password(stored_password[0], password):
                print("The username and password are correctly")
                changePassword = change_password(username, new_password)
            else:
                changePassword = False
    return changePassword


def id_generator(size):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


# print(id_generator(numCharacterSingleSignOn))


def single_sign_on(username):
    expires_url = (datetime.datetime.now(pytz.timezone('Asia/Jerusalem')) + datetime.timedelta(
        minutes=timeToExpiresUrl)).strftime('%Y-%m-%d %H:%M:%S')
    SingleSignOn = id_generator(numCharacterSingleSignOn)
    LinkFromEmail = make_sha1(id_generator(numCharacterLinkFromEmail))
    sql = "INSERT INTO single_sign_on (username, single_sign_on_num, get_hash_login, date) VALUES (%s, %s, %s, %s)"
    val = (username, SingleSignOn, LinkFromEmail, expires_url)
    my_cursor.execute(sql, val)
    mysqldb.commit()
    if my_cursor.rowcount > 0:
        return SingleSignOn, LinkFromEmail
    else:
        return None, None

def make_sha1(value):
    import hashlib
    myhash = hashlib.sha1(value.encode('utf-8'))
    return myhash.hexdigest()


def get_url_from_email(get_url_key):
    if validation_code(get_url_key):
        now = datetime.datetime.now(pytz.timezone('Asia/Jerusalem')).strftime('%Y-%m-%d %H:%M:%S')
        sql = "SELECT username, date FROM single_sign_on WHERE get_hash_login = \"{get_url}\" ORDER BY date DESC LIMIT 1".format(
            get_url=get_url_key)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        if len(my_result) > 0:
            expires_url = my_result[0][1]
            now_str = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
            if now_str <= expires_url:
                return my_result[0][0]
    return None


# username = get_url_from_email('MD17TVYQ8FCNOS3H')


def reset_password(username, code, password, password_repeat):
    validationOK = True
    if not validation(username):
        validationOK = False
    if not checkPassword(password):
        validationOK = False
    if not validation_code(code):
        validationOK = False
    if password == password_repeat and validationOK:
        changePassword = True
        sql = "SELECT username FROM single_sign_on WHERE single_sign_on_num = \"{num}\" ORDER BY date DESC LIMIT 1".format(
            num=code)
        my_cursor.execute(sql)
        my_result = my_cursor.fetchall()
        if len(my_result) > 0:
            changePassword = change_password(username, password)
            sql = "DELETE FROM single_sign_on WHERE single_sign_on_num = \"{num}\" ".format(num=code)
            my_cursor.execute(sql)
            print("delete: ", code)
            mysqldb.commit()
        else:
            print("no find Code")
            changePassword = False
    else:
        changePassword = False
        print("password not mash")
    return changePassword


def add_store(store_name, street, city, phone, owner):
    if  validation(store_name) and validation(street) and validation(city) and validation(phone) and validation(owner):
        sql = 'INSERT INTO website.store (name, street, city, phone, owner) VALUES ("'
        sql += store_name + '", "' + street + '", "' + city + '", "' + phone + '", "' + owner + '" )'
        print(sql)
        my_cursor.execute(sql)
        mysqldb.commit()
        if my_cursor.rowcount > 0:
            return True
        else:
            return False
    else:
        return False


def table_store_by_name(store_name):
    mysqldb_hacked = mysql.connector.connect(
        host=dbHost,
        user="root",
        password="D@sk@l32!",
        database=databaseName
    )

    hacked_cursor = mysqldb.cursor()
    if store_name == "":
        sql = "SELECT name, street, city, phone, owner FROM store"
    else:
        sql = "SELECT name, street, city, phone, owner FROM store WHERE name = \"{name}\" ".format(name=store_name)
    hacked_cursor.execute(sql)
    store_table = hacked_cursor.fetchall()
    result_table = "<table> <tr> <th> name </th> <th>street</th> <th> city </th> <th> phone</th> <th> " \
                   "owner</th></tr> "
    for row in store_table:
        result_table += "<tr>"
        for column in row:
            result_table += "<th>"
            result_table += str(column)
            result_table += "</th>"
        result_table += "</tr>"
    result_table += "</table>"
    return result_table

def table_store_by_name_trust(store_name):
    if store_name == "":
        sql = "SELECT name, street, city, phone, owner FROM store"
    elif not validation(store_name):
        return "Err the Input is not correctly"
    else:
        sql = "SELECT name, street, city, phone, owner FROM store WHERE name = \"{name}\" ".format(name=store_name)
    my_cursor.execute(sql)
    store_table = my_cursor.fetchall()
    result_table = "<table> <tr> <th> name </th> <th>street</th> <th> city </th> <th> phone</th> <th> " \
                   "owner</th></tr> "
    for row in store_table:
        result_table += "<tr>"
        for column in row:
            result_table += "<th>"
            result_table += str(column)
            result_table += "</th>"
        result_table += "</tr>"
    result_table += "</table>"
    return result_table
