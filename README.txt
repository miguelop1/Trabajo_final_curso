Code used for the mysql:
//Login table
CREATE DATABASE loginInfo;

CREATE TABLE Login (
    Userid int PRIMARY KEY,
    Username varchar(20),

    Password varchar(20)
);

//Database config table
CREATE TABLE admin_config (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gmail VARCHAR(20) NOT NULL,
    text_to_receive VARCHAR(20) NOT NULL,
    server_name VARCHAR(20) NOT NULL,
    trigger_for_activation VARCHAR(20) NOT NULL
);