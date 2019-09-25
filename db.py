# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:40:42 2019

@author: Mrunali
"""

drop table if exists users;
    create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);