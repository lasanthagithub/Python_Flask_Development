create database python_Flask;


create table python_Flask.users(id int(11) auto_increment primary key, 
name varchar(100), email varchar(100),
username varchar(30), password varchar(100), 
register_date timestamp default current_timestamp);