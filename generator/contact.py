from models.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


# данные для полей типа строка или textarea
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits# + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# данные для телефонов
def random_phone():
    return '+7' + ''.join([random.choice(string.digits) for i in range(10)])

# данные для email
def random_email():
    return ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(10))]) + '@gmail.com'

# данные для сайта
def random_site():
    return ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(10))]) + '.com'

# данные для дат
def random_date():
    return str(random.randrange(31))

# данные для месяцев
def random_month():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[random.randrange(12)]

# данные для годов
def random_year():
    return str(random.randrange(1980, 2000))


# тестовые данные
testdata = [Contact(firstname=random_string("First_name:", 10), middlename=random_string("Middle_name:", 10), lastname=random_string("Last_name:", 10),
                    nickname=random_string("Nickname:", 10), title=random_string("Title:", 10), company=random_string("Company:", 10),
                    address=random_string("Address:", 10), home=random_phone(), mobile=random_phone(), work=random_phone(), fax=random_phone(), email=random_email(),
                    email2=random_email(), email3=random_email(), homepage=random_site(), bday=random_date(), bmonth=random_month(), byear=random_year(), aday=random_date(), amonth=random_month(), ayear=random_year())
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))