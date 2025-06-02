import re
import socket
import os

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

def hotspot2(ip2):
    if ip2 is None:
        ip2 = '192.168.12.56'
    sock = socket.socket()
    sock.bind((ip2, 9090))

def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:@domain.com"

def execute_command(command):
    os.system(command)

def insecure_deserialization(data):
    # Insecure deserialization vulnerability
    obj = pickle.loads(data)
    obj.execute()

def sql_injection(username, password):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
    execute_query(query)

def xss_vulnerability(input):
    # Cross-Site Scripting (XSS) vulnerability
    html = "<div>%s</div>" % input
    return html

def insecure_file_upload(file):
    # Insecure file upload vulnerability
    file.save("/var/www/uploads/" + file.filename)

def command_injection(command):
    # Command injection vulnerability
    os.system("ping " + command)

def insecure_randomness():
    # Insecure randomness vulnerability
    password = random.randint(1000, 9999)
    return password

a = 1
while a < 3:
    if a % 2 == 0:
        return # Noncompliant: return is outside of a function
    a += 1

for n in range(5):
  yield n # Noncompliant: yield is outside of a function