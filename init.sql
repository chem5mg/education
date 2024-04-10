CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comm (
    id SERIAL PRIMARY KEY,
    message_id INT REFERENCES messages(id),
    user_id INT REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, password) VALUES
    ('user1', 'user1@example.com', 'password1'),
    ('user2', 'user2@example.com', 'password2'),
    ('user3', 'user3@example.com', 'password3');
    
INSERT INTO messages (user_id, content) VALUES
    (1, 'Сообщение от пользователя 1'),
    (2, 'Сообщение от пользователя 2');
    
INSERT INTO comm (message_id, user_id, content) VALUES
    (1, 2, 'Комментарий от пользователя 2 к сообщению от пользователя 1'),
    (2, 1, 'Комментарий от пользователя 1 к сообщению от пользователя 2');