import sys
import sqlite3


# con = sqlite3.connect('example.db')
# cur = con.cursor()

def addUser(email):
    print(email)

def addRelation(user1, user2):
    print(user1, user2)

 

if sys.argv[1] == 'addUser':
    email = sys.argv[2]
    addUser(email)
elif sys.argv[1] == 'addRelation':
    person1 = sys.argv[2]
    person2 = sys.argv[3]
    addRelation(person1, person2)

