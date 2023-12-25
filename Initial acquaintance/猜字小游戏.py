
import random
import time
guess = 0
answer = random.randint(0,100)
people = random.randint(0,100)
temp = input("不妨猜一下我正在想什么数字\n给你提个醒哦,范围是零到一百呢")
start = time.perf_counter()
guess = eval(temp)
if guess == answer:
    print("你可真是我肚子里的蛔虫")
while guess != answer:
    if guess > answer:
        temp = input("你猜的太大了,再猜一遍吧.")
        guess = eval(temp)
    elif guess < answer:
        temp = input("猜的太小,再猜一遍吧.")
        guess = eval(temp)
end = time.perf_counter()
print("游戏结束了,本次用时{:.2f},打败了{}%的人".format(end - start,people))
