Code used for the mysql:
CREATE DATABASE loginInfo;

CREATE TABLE Login (
    Userid int PRIMARY KEY,
    Username varchar(10),

    Password varchar(10)
);