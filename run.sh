#!/usr/bin/env bash

echo "开始测试......"
python /var/jrnkins_home/git/myjenkins/python1.py
wait
python /var/jrnkins_home/git/myjenkins/python2.py
wait
python /var/jrnkins_home/git/myjenkins/python3.py

echo "结束测试......"