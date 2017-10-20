"""
程序分析：质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，
除了1和它本身以外不再有其他因数的数称为质数，如：2、3、5、7、11、13、17、19。
"""
total = []
for i in range(2, 101):
    flag = True
    for j in range(2, int(i / 2)):
        if i % j == 0:
            flag = False
    if flag:
        total.append(i)
print(total)
