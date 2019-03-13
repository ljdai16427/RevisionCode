i = 0
totalnum = 2
num = str(input('请输入密码：'))
correctcode = 'FishC.com'
while True:
    if '*' in num:
        print('456')
        print("密码中不能带有\"*\"号！您还有{1}次机会！{0}".format(input('请输入密码：'),\
             totalnum - i + 1))
    else:

        if num != correctcode:
            if i < totalnum:

                extranum = totalnum - i
                print('123')
                print("密码输入错误！您还有{0}次机会！{1}".format(extranum, input("请输入密码：")))
                print('907865')
                i += 1
            else:
                break
        else:
            print("密码正确，进入程序......")
