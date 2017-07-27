# -*- coding:utf-8 -*-

'''
MySQL_Server


Filed 字段
record
recordset

Name     Time       Person       LeaveTime

登录数据库服务器
mysql.exe -h 127.0.0.1 -u root -p

(1)数据库
创建数据库
create database rookie;
删除数据库
create database rookie;
查看数据库
show databases;

(2)数据库表

创建表
create table tb1 (movie int(4),moviename char(128), movieyear int(4));
查看表结构
show columns from tb1;
查看库中有什么表
show tables;

show columns from tb2;

设置id为key
create table tb3 (id int(4) not null PRIMARY KEY, namr char(64));

create table tb4 (id int(4) not null PRIMARY KEY auto_increment, namr char(64));

设置默认值
create table tb5 (id int(4) not null primary key auto_increment, name char(64), sex char(1) default 'm');

'''

