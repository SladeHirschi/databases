CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT
)

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    user_id INT,
    name text,
    password text,
    FOREIGN KEY (user_id) REFERENCES users(id)
)

CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    from_id INT,
    to_id INT,
    blocked INT,
    FOREIGN KEY (from_id) REFERENCES accounts(id),
    FOREIGN KEY (to_id) REFERENCES accounts(id)
)

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    account_id INT,
    likes INT,
    dislikes INT,
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)

CREATE TABLE comment (
    id INTEGER PRIMARY KEY,
    post_id INT,
    content TEXT,
    account_id INT,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (account_id) REFERENCES account(id)
)

CREATE TABLE replies (
    id INTEGER PRIMARY KEY,
    comment_id INT,
    account_id INT,
    FOREIGN KEY (comment_id) REFERENCES comments(id),
    FOREIGN KEY (account_id) REFERENCES accounts(id)
)