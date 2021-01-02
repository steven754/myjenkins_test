#!/usr/bin/env bash

echo "开始测试......"
python /var/jrnkins_home/git/myjenkins_test/python1.py
wait
python /var/jrnkins_home/git/myjenkins_test/python2.py
wait
python /var/jrnkins_home/git/myjenkins_test/python3.py

echo "结束测试......"