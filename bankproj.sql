
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT=0;
START TRANSACTION;
SET time_zone="+00:00";

DROP database if exists proj1;
Create database proj1;
use proj1;
DROP table if exists customers;
create table customers(
    acno int not NULL AUTO_INCREMENT,
    name varchar(50) DEFAULT NULL,
    address varchar(50) DEFAULT NULL,
    phone varchar(30) DEFAULT NULL,
    email varchar(30) DEFAULT NULL,
    aadhar_no varchar(50) DEFAULT NULL,
    account_type varchar(20) DEFAULT NULL,
    status varchar(20) DEFAULT NULL,
    balance float(10,2) DEFAULT NULL,
    PRIMARY KEY (acno) );

insert into customers values(1, 'riya', 'surya-nagar', 121, 'riya@gmail.com', '1231', 'saving', 'active', 1200.0);
insert into customers values(2, 'mansi', 'surya-nagar2', 122, 'mansi@gmail.com', '1232', 'current', 'active', 1000.0);
insert into customers values(3, 'sita', 'surya-nagar3', 123, 'sita@gmail.com', '1233', 'saving', 'active', 1000.0);

create table transactions(
    tid int(11) not null AUTO_INCREMENT,
    tr_date date DEFAULT NULL,
    amount float(10,2) DEFAULT NULL,
    type varchar(20) DEFAULT NULL,
    acno int DEFAULT NULL, 
    primary key (tid));

insert into transactions values(1, '2020-10-10', 200, 'deposit', 1);
insert into transactions values(2, '2020-10-15', 200, 'deposit', 2);
insert into transactions values(3, '2020-10-18', 400, 'withdraw', 1);
insert into transactions values(4, '2020-10-18', 500, 'withdraw', 3);

SELECT * FROM customers;
