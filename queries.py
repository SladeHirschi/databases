import sys
import sqlite3


con = sqlite3.connect('test.db')
cur = con.cursor()

def addUser(email):
    cur.execute("INSERT INTO users (email) VALUES (?)", [email])
    con.commit()

def addRelation(user1, user2):
    print("This was the inputted users: ", user1, user2)
    data1 = cur.execute("SELECT id FROM accounts WHERE username = ?", [user1])
    username1 = data1.fetchone()
    data2 = cur.execute("SELECT id FROM accounts WHERE username = ?", [user2])
    username2 = data2.fetchone()

    print("usernames: ", username1, username2)
    if username1 is not None:
        toInput1 = username1[0]
    else:
        print("The inputted username for your account does not exist or was inputted incorrectly")
        return
    if username2 is not None:
        toInput2 = username2[0]
    else:
        print("The inputted username for your friend does not exist or was inputted incorrectly")
        return

    cur.execute("INSERT INTO friends (from_id, to_id, blocked) VALUES (?, ?, ?)", [toInput1, toInput2, 0])
    con.commit()

def addAccount(email, username, password):
    data = cur.execute("SELECT id FROM users WHERE email = ?", [email])
    user = data.fetchone()
    if user is not None:
        userId = user[0]
    else:
        print("THERE IS NO ONE WITH THAT EMAIL!")
        return
    cur.execute("INSERT INTO accounts (user_id, username, password) VALUES (?, ?, ?)", [userId, username, password])
    con.commit()

def addPost(username, content):
    data1 = cur.execute("SELECT id FROM accounts WHERE username = ?", [username])
    accountId = data1.fetchone()
    if accountId is not None:
        id = accountId[0]
    else:
        print("This is an invalid username")
        return
    cur.execute("INSERT INTO posts (account_id, content, likes, dislikes) VALUES (?, ?, ?, ?)", [id, content, 0, 0])
    con.commit()



def viewAccounts():
    data = cur.execute("SELECT username FROM accounts")
    accounts = data.fetchall()
    for account in accounts:
        if account is None:
            print("There are none")
            return
        else:
            print(account[0])

def viewPosts():
    data = cur.execute("""
        SELECT 
            p.content, 
            p.likes, 
            p.dislikes,
            a1.username as poster,
            a2.username as commenter,
            c.content
        FROM 
            posts p
        LEFT JOIN
            accounts a1
            ON p.account_id = a1.id
        LEFT JOIN
            comments c
            ON c.post_id = p.id
        LEFT JOIN
            accounts a2
            ON c.account_id = a2.id
        ORDER BY a1.username
        """)
    posts = data.fetchall()
    print(posts)
    for post in posts:
        if post is None:
            print("There are none")
            return
        else:
            print("""
                Posted By: {}
                    Content: {}
                Comments:
                    {}
                    Commented By: {}
                Likes {}  Dislikes {}
            """.format(post[3], post[0], post[5], post[4], post[1], post[2]))

def viewFriendsPosts(username):
    data1 = cur.execute("SELECT id FROM accounts WHERE username = ?", [username])
    accountId = data1.fetchone()
    if accountId is not None:
        id = accountId[0]
    else:
        print("This is an invalid username")
        return
    data = cur.execute("""
        SELECT 
            p.content, 
            p.likes, 
            p.dislikes,
            a1.username as poster,
            a2.username as commenter,
            c.content
        FROM 
            posts p
        LEFT JOIN
            accounts a1
            ON p.account_id = a1.id
        LEFT JOIN
            comments c
            ON c.post_id = p.id
        LEFT JOIN
            accounts a2
            ON c.account_id = a2.id
        JOIN
            friends f
            ON f.from_id = ? AND p.account_id = f.to_id
        ORDER BY a1.username
        """, [id])
    posts = data.fetchall()
    print(posts)
    for post in posts:
        if post is None:
            print("There are none")
            return
        else:
            print("""
                Posted By: {}
                    Content: {}
                Comments:
                    {}
                    Commented By: {}
                Likes {}  Dislikes {}
            """.format(post[3], post[0], post[5], post[4], post[1], post[2]))
    

def getFunction():
    return input("""
    What command would you like to do? 
        Possible: addUser, addAccount, viewAccounts, addRelation, viewPosts, addPost, addComment, addReply, likeComment, viewFriendsPosts)

    TO QUIT enter exit  
""")



def main():
    function = getFunction()
    while function != 'exit':
        if function == 'addUser':
            email = input("What is your email? ")
            addUser(email)
            function = getFunction()

        elif function == 'addAccount':
            email = input("What is the email associated with the account you want to create? ")
            username = input("What do you want your username to be? ")
            password = input("What is your password? ")
            addAccount(email, username, password)
            function = getFunction()

        elif function == 'viewAccounts':
            viewAccounts()
            function = getFunction()

        elif function == 'addRelation':
            username1 = input("What is the username of your account? ")
            username2 = input("What is the username of the friend you want to add? ")
            addRelation(username1, username2)
            function = getFunction()

        elif function == 'viewPosts':
            viewPosts()
            function = getFunction()

        elif function == 'addPost':
            username = input("What is your username? ")
            content = input("What do you want to write in your post? ")
            addPost(username, content)
            function = getFunction()

        elif function == 'viewFriendsPosts':
            username = input("What is your username? ")
            viewFriendsPosts(username)
            function = getFunction()

        elif function == 'exit':
            break

        else:
            print("There is no function named " + function)
            function = getFunction()

main()

