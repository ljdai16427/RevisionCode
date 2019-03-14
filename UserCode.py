i = 0
totalnum = 2
num = str(input('请输入密码：'))
correctcode = 'FishC.com'
while True:
    if '*' in num:
        print("密码中不能带有\"*\"号！您还有{0}次机会！请输入密码: ".format(\
            totalnum - i + 1), end = '')
        print(input())
    else:

        if num != correctcode:
            if i < totalnum:
                extranum = totalnum - i
                print("密码输入错误！您还有{0}次机会！请输入密码：".format(extranum), \
                    end = '')
                print(input())
                i += 1
            else:
                break
        else:
            print("密码正确，进入程序......")
