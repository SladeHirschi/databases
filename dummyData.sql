INSERT INTO users (id, email) VALUES (1, 'test@test.com');

INSERT INTO accounts (id, user_id, name, password) VALUES (1, 1, 'test', 'test');
INSERT INTO accounts (id, user_id, name, password) VALUES (2, 1, 'test2', 'test2');

INSERT INTO friends (id, to_id, from_id, blocked) VALUES (1, 2, 1, 0);

INSERT INTO posts (id, account_id, content, likes, dislikes) VALUES (1, 2, "THIS is from account 2", 1, 300);

INSERT INTO comments (id, post_id, content, account_id) VALUES (1, 1, "Commenting on test1's post", 1);

