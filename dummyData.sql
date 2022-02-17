INSERT INTO users (id, email) VALUES (1, 'john@test.com');
INSERT INTO users (id, email) VALUES (2, 'sladehirsc@gmail.com');

INSERT INTO accounts (id, user_id, username, password) VALUES (1, 1, 'John', 'apple123');
INSERT INTO accounts (id, user_id, username, password) VALUES (2, 1, 'Joe', 'apple1234');
INSERT INTO accounts (id, user_id, username, password) VALUES (3, 2, 'Slade', 'asdf');

INSERT INTO friends (id, to_id, from_id, blocked) VALUES (1, 2, 1, 0);

INSERT INTO posts (id, account_id, content, likes, dislikes) VALUES (1, 2, "I Joe am having a great day.", 15, 1);

INSERT INTO comments (id, post_id, content, account_id) VALUES (1, 1, "Joe I like your post -John", 1);

