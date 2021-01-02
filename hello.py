print("hello world")
#econding="utf-8"
import os

lst = os.listdir(os.getcwd())

for c in lst:
    if os.path.isfile(c) and c.endswith('.py'): #and c.find("AllTest") == -1:  # 去掉AllTest.py文件
        print(c)
        #os.system(os.path.join(os.getcwd(), c))