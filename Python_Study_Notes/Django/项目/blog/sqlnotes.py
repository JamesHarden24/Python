# -*- coding:utf-8 -*-
'''

码农如何理解数据库的结构

database -> table -> col
数据库   -> 表    -> 列

create table 'form3'(`Id`Integer PRIMARY KEY autoincrement, `name` varchar(100) not null,
`age` varchar(2) not null, 
`tall` varchar(3) not null;

(1)创建数据库(既然他是关系类型的，是有关系的，那我们得先确定关系)
关键词 create table
确定非空，默认等熟悉 not null, default
自增Id: 保证

(2)建立索引

(3)增删改查
insert: insert into table(col1) values (values)
update
delete
select

'''