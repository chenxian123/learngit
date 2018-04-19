#coding=utf8
import random

class admin(object):
    def num(self):
        i=0
        while i<5:
            i+=1
            inp = input("请输入您要猜的数字:\n")
            numb = random.randint(1, 100)
            if inp > numb:
                print "您猜的数大了。"
            elif inp < numb:
                print "您猜的数小了。"
            elif inp==numb:
                print "恭喜您猜对了！"
            elif inp=="quit":
                print "直接退出程序"

            if i==4:
                print "仅剩一次机会了！"
            elif i==5:
                pand=raw_input("请问您要继续吗？Y or N:")
                if  pand=='Y' or pand=='y':
                    i=0
                if pand=='N' or pand=='n':
                    i=5

wo=admin()
wo.num()