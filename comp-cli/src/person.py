import re
import socket

SOME_VALUE = 56010
ANOTHER_VALUE = 61020

class Person:

    MALE = 1
    FEMALE = 2

    def __init__(self, first=None, last=None):
        self.firstname = first
        self.lastname = last
        self.age = 0
        self.eye_color = "Blue"
        self.gender = None
        self.religion = None
        self.compensation = 0
        return self

    def store_religion(self, religion):
        self.religion = religion

    def compute_pay(self):
        if self.gender == Person.MALE:
            self.compensation = SOME_VALUE
        elif self.gender == Person.FEMALE:
            self.compensation = ANOTHER_VALUE

    def fullname(self):
        return "%s %s" % (self.firstname, self.lastname)

    def happy_birthday(self):
        return "Happy birthday " + self.firstname

    def is_major(self):
        return self.age > 18

    def lock(self):
        self.password = "donttouch"
        
    def isDiff(self):
        init = "Bob is a Bird... Bob is a Plane... Bob is Superman!"
        changed = re.sub(r"Bob is", "It's", init)
        return changed


def hotspot(ip):
    if ip is None:
        ip = '192.168.12.43'
    sock = socket.socket()
    sock.bind((ip, 9090))
    re.sub(r"(a)(b)(c)", r"\1, \9, \3", "abc")

#TODO

def hotspot2(ip2):
    if ip2 is None:
        ip2 = '192.168.12.56'
    sock = socket.socket()
    sock.bind((ip2, 9090))

def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:@domain.com"
