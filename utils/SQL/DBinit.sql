--CREATE USER mydbusername@localhost IDENTIFIED BY 'mydbuserpwd';

-- CREATE DATABASE piscium 09/06/2018 --
CREATE DATABASE piscium DEFAULT CHARACTER SET utf8;

CREATE TABLE authorities (
    authorityid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'AUTHORITY ID',
    authorityname VARCHAR(32) NOT NULL UNIQUE COMMENT 'AUTHORITY NAME',
    authoritydesc VARCHAR(32) NOT NULL UNIQUE COMMENT 'AUTHORITY DESCRIPTION'
) ENGINE = InnoDB;

CREATE TABLE statuses (
    statusid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'STATUS ID',
    statusname VARCHAR(32) NOT NULL UNIQUE COMMENT 'STATUS NAME',
    statusdesc VARCHAR(32) NOT NULL UNIQUE COMMENT 'STATUS DESCRIPTION'
) ENGINE = InnoDB;

CREATE TABLE users(
    userid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'USER ID',
    user_authorityid INT(8),
    user_statusid INT(8),
    FOREIGN KEY (user_authorityid) REFERENCES authorities (authorityid),
    FOREIGN KEY (user_statusid) REFERENCES statuses (statusid)
) ENGINE = InnoDB;

CREATE TABLE roles (
    roleid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'ROLE ID',
    rolename VARCHAR(32) NOT NULL UNIQUE COMMENT 'ROLE NAME',
    roledesc VARCHAR(32) NOT NULL UNIQUE COMMENT 'ROLE DESCRIPTION'
) ENGINE = InnoDB;

CREATE TABLE messages (
    messagetypeid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'MESSAGE´S TYPE ID',
    messagetypename VARCHAR(32) NOT NULL UNIQUE COMMENT 'MESSAGE´S TYPE NAME',
    messagetypedesc VARCHAR(32) NOT NULL UNIQUE COMMENT 'MESSAGE´S TYPE DESCRIPTION'
) ENGINE = InnoDB;

CREATE TABLE mstatuses (
    mstatustypeid INT(8) AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY COMMENT 'MESSAGE STATUS´S TYPE ID',
    mstatustypename VARCHAR(32) NOT NULL UNIQUE COMMENT 'MESSAGE STATUS´S TYPE NAME',
    mstatustypedesc VARCHAR(32) NOT NULL UNIQUE COMMENT 'MESSAGE STATUS´S TYPE DESCRIPTION'
) ENGINE = InnoDB;

CREATE TABLE users_profile(
    userid INT(8) AUTO_INCREMENT UNIQUE NOT NULL COMMENT 'USER ID',
    FOREIGN KEY (userid) REFERENCES users (userid),
    username VARCHAR(32) UNIQUE NOT NULL UNIQUE COMMENT 'USER NAME',
    useremail VARCHAR(32) UNIQUE NOT NULL UNIQUE COMMENT 'USER EMAIL',
    userpwd CHAR(32) NOT NULL COMMENT 'USER PASSWORD',
    userphone CHAR(20) NULL COMMENT 'USER MOBILE NUMBER',
    useravatar VARCHAR(128) NULL COMMENT 'USER AVATAR ICON',
    userloginstate TINYINT NOT NULL DEFAULT '0' COMMENT 'USER LOGIN STATE',
    userctime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'USER ACCOUNT CREATION TIME',
    userutime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'USER ACCOUNT LAST UPDATED TIME'
) ENGINE = InnoDB;

CREATE TABLE users_role(
    userid INT(8) NOT NULL COMMENT 'USER ID',
    FOREIGN KEY (userid) REFERENCES users (userid),
    user_roleid INT(8) NOT NULL COMMENT 'USER´S ROLE ID',
    FOREIGN KEY (user_roleid) REFERENCES roles (roleid)
) ENGINE = InnoDB;

CREATE TABLE users_message(
    userid INT(8) NOT NULL COMMENT 'USER ID',
    FOREIGN KEY (userid) REFERENCES users (userid),
    user_mtypeid INT(8) NOT NULL COMMENT 'USER´S MESSAGE TYPE ID',
    FOREIGN KEY (user_mtypeid) REFERENCES messages (messagetypeid),
    user_mstatusid INT(8) NOT NULL COMMENT 'USER´S MESSAGE STATUS ID',
    FOREIGN KEY (user_mstatusid) REFERENCES mstatuses (mstatustypeid),
    user_mfrom INT(8) NOT NULL COMMENT 'USER ID',
    FOREIGN KEY (user_mfrom) REFERENCES users (userid),
    user_mto INT(8) NOT NULL COMMENT 'USER ID',
    FOREIGN KEY (user_mto) REFERENCES users (userid),
    user_mctime DATETIME NOT NULL COMMENT 'USER´S MESSAGE CREATION TIME',
    user_mrtime DATETIME NULL COMMENT 'USER´S MESSAGE GOT READED TIME'
) ENGINE = InnoDB;

-- MOCK DATA --
INSERT INTO authorities (authorityid, authorityname, authoritydesc) VALUE (1, 'admin', 'Administrator');
INSERT INTO authorities (authorityid, authorityname, authoritydesc) VALUE (2, 'user', 'User');
INSERT INTO authorities (authorityid, authorityname, authoritydesc) VALUE (3, 'guest', 'Guest');
INSERT INTO statuses (statusid, statusname, statusdesc) VALUE (1, 'root', 'Root');
INSERT INTO statuses (statusid, statusname, statusdesc) VALUE (2, 'verified', 'Verified');
INSERT INTO statuses (statusid, statusname, statusdesc) VALUE (3, 'unverified', 'Unverified');
INSERT INTO users (userid, user_authorityid, user_statusid) VALUE (1, 1, 1);
INSERT INTO users (userid, user_authorityid, user_statusid) VALUE (2, 2, 2);
INSERT INTO users (userid, user_authorityid, user_statusid) VALUE (3, 3, 3);
INSERT INTO roles (roleid, rolename, roledesc) VALUE (1, 'cleaning_services', 'Cleaning Services');
INSERT INTO roles (roleid, rolename, roledesc) VALUE (2, 'community_relations', 'Community Relations');
INSERT INTO roles (roleid, rolename, roledesc) VALUE (3, 'ui_designer', 'UI designer');
INSERT INTO messages (messagetypeid, messagetypename, messagetypedesc) VALUE (1, 'notice', 'Notice');
INSERT INTO messages (messagetypeid, messagetypename, messagetypedesc) VALUE (2, 'message', 'Message');
INSERT INTO messages (messagetypeid, messagetypename, messagetypedesc) VALUE (3, 'upcoming', 'Upcoming');
INSERT INTO mstatuses (mstatustypeid, mstatustypename, mstatustypedesc) VALUE (1, 'read', 'Read');
INSERT INTO mstatuses (mstatustypeid, mstatustypename, mstatustypedesc) VALUE (2, 'unread', 'Unread');
INSERT INTO mstatuses (mstatustypeid, mstatustypename, mstatustypedesc) VALUE (3, 'blocking', 'Blocking');
INSERT INTO users_profile (userid, username, useremail, userpwd, useravatar) VALUE (1, "Jean Valjean", 'jlaxlopez@gmail.com', 'Jlax1', '/static/avatars/jlax.jpg');
INSERT INTO users_profile (userid, username, useremail, userpwd, useravatar) VALUE (2, "Scarlett O'Hara", 'xhan01@ucm.es', 'Xhax2', '/static/avatars/xhan.jpg');
INSERT INTO users_profile (userid, username, useremail, userpwd, useravatar) VALUE (3, "Don Quijote", 'menglongwu3@gmail.com', 'Mwu3', '/static/avatars/mwu.jpg');
INSERT INTO users_role (userid, user_roleid) VALUE (1, 1);
INSERT INTO users_role (userid, user_roleid) VALUE (2, 2);
INSERT INTO users_role (userid, user_roleid) VALUE (3, 3);