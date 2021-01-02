#encoding: utf-8
from time import sleep, ctime


# 播放音乐
def music(musicname, loop):
    for i in range(loop):
        print("我要播放音乐,%s,%s" % (musicname, ctime()))
        sleep(3)


# 播放视频
def video(videoname, loop):
    for i in range(loop):
        print("我要看电视,%s,%s" % (videoname, ctime()))
        sleep(3)


if __name__ == "__main__":
    music("西游记", 3)
    video("水浒传", 2)
    print("all end:%s" % ctime())