CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    session VARCHAR,
    validity INTEGER,
    username VARCHAR,
    password VARCHAR,
    firstname VARCHAR,
    lastname VARCHAR,
    email VARCHAR,
    mfa_enabled BOOLEAN,
    mfa_secret VARCHAR,
    is_internal BOOLEAN,
    role VARCHAR,
    status INTEGER,
    deleted BOOLEAN,
    profile_img_base64 VARCHAR,
    session_timeout_min INTEGER
);

INSERT INTO users (id, validity, username, password, firstname, lastname, email, mfa_enabled, is_internal, role, status, deleted, profile_img_base64, session_timeout_min)
VALUES
    (1, 1, 'mario.rossi', 'tortello', 'Mario', 'Rossi', 'mario.rossi@example.com', 0, 1, 'admin_system', 1, 0, 'string', 0),
    (2, 1, 'luigi.rossi', 'raviolo', 'Luigi', 'Rossi', 'luigi.rossi@example.com', 0, 1, 'admin_system', 1, 0, 'string', 0),
    (3, 1, 'pippo.rossi', 'ripieno', 'Pippo', 'Rossi', 'pippo.rossi@example.com', 0, 1, 'admin_system', 1, 0, 'string', 0);


