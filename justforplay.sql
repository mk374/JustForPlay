--all tables
CREATE TABLE Zip (
	zip_code INTEGER NOT NULL PRIMARY KEY,
	latitude FLOAT NOT NULL,
	longitude FLOAT NOT NULL
);

CREATE TABLE ruser (
   uid VARCHAR(256) NOT NULL PRIMARY KEY,
   name VARCHAR(64) NOT NULL,
   password VARCHAR(64) NOT NULL,
   bio VARCHAR(1024) NOT NULL,
   zip_code INTEGER NOT NULL REFERENCES Zip(zip_code)
);

-- CREATE TABLE Community (
-- 	communityid VARCHAR(256) NOT NULL PRIMARY KEY,
-- 	description VARCHAR(1000) NOT NULL
-- );

-- CREATE TABLE SubCommunity (
-- 	communityid VARCHAR(256) NOT NULL,
-- 	subid VARCHAR(256) unique,
-- 	sub_description VARCHAR(1000) NOT NULL,
-- 	PRIMARY KEY (communityid, subid),
-- 	FOREIGN KEY (communityid) REFERENCES Community(communityid)
-- );

CREATE TABLE GROUPS (
   gid VARCHAR(256) NOT NULL UNIQUE,
   group_name VARCHAR(256) NOT NULL,
   community VARCHAR(256) NOT NULL,
   zip_code INTEGER NOT NULL REFERENCES Zip(zip_code),
   public_or_private VARCHAR(32) NOT NULL, CHECK (public_or_private in ('private', 'public')),
   description VARCHAR(1024) NOT NULL,
   PRIMARY KEY (gid)
);

CREATE TABLE MEMBERS (
   uid VARCHAR(256) NOT
    NULL REFERENCES ruser(uid),
   gid VARCHAR(256) NOT NULL REFERENCES Groups(gid),
   admin BOOLEAN,
   PRIMARY KEY(uid, gid)
);

CREATE TABLE Events (
	gid VARCHAR(256) NOT NULL,
	eventid VARCHAR(256) NOT NULL UNIQUE,
	event_name VARCHAR(512) NOT NULL,
	host VARCHAR(256) NOT NULL,
	location VARCHAR(512) NOT NULL,
	e_date date not null,
  e_time time not null,
	public_or_private VARCHAR(32) NOT NULL CHECK (public_or_private = 'private' or public_or_private = 'public'),
	PRIMARY KEY (gid, eventid),
	FOREIGN KEY (gid) REFERENCES Groups(gid)
);

CREATE TABLE Attending (
	eventid VARCHAR(256) NOT NULl,
	uid VARCHAR(256) NOT NULl,
  PRIMARY key(eventid,uid),
	FOREIGN KEY (eventid) REFERENCES Events(eventid),
	FOREIGN KEY (uid) REFERENCES ruser(uid)
);

