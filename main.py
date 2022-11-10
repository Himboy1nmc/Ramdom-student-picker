#作者 Jack Li
import random
import datetime
now = datetime.datetime.now()
#导入1班与12班的学生
class01 = open('Sample_space_01.txt','r')
Students_01 = list(class01.readlines())
class01.close()
class12 = open('Sample_space_12.txt','r')
Students_12 = list(class12.readlines())
class12.close()
#随机抽取
selected = []
newadd = []
def pickc12():

    if len(Students_12) == 0 :
        print('十二班已经没有人可以抽取了。')
        input('press any key to exit ')
    elif len (Students_12)<= 4:
        _chosen = []
        _picked = []
        for i in Students_12:
            _chosen.append(i)
        _picked = _chosen
        for i in _chosen:
            Students_12.remove(i)
        clear(12)
        print("十二班已全部抽取完毕，再见")

    else:
        _picked = []
        for i in range(4):
            _chosen = (random.choice(Students_12))
            _picked.append(_chosen)
            Students_12.remove(_chosen)
        clear(12)

    s12= open('Selected_12.txt', 'a+')
    _tempload = s12.readlines()

    newadd.append(now.strftime("%Y-%m-%d %H:%M:%S"+ ' Lucky students: \n'))
    for i in _tempload:
        newadd.append(i)
    for i in _picked:
        newadd.append(i)
    for j in newadd:
        s12.write(j)
    s12.write('\n')
    return _picked

def pickc01():

    if len(Students_01) == 0 :
        print('一班已经没有人可以抽取了。')
        input('press any key to exit ')
    elif len (Students_01)<= 4:
        _chosen = []
        _picked = []
        for i in Students_01:
            _chosen.append(i)
        _picked = _chosen
        for i in _chosen:
            Students_01.remove(i)
        clear(1)
        print("一班已全部抽取完毕，再见")

    else:
        _picked = []
        for i in range(4):
            _chosen = (random.choice(Students_01))
            _picked.append(_chosen)
            Students_01.remove(_chosen)
        clear(1)

    s01 = open('Selected_01.txt', 'a+')
    s01.write(now.strftime("%Y-%m-%d %H:%M:%S" + ' Lucky students: \n'))
    for i in _picked:
        s01.write(i)
    s01.write('\n')
    s01.close()
    return  _picked

def clear(x):
    if x == 12:
        c12 = open('Sample_space_12.txt','w+')
        for i in Students_12:
            c12.write(i)
    if x == 1:
        c01 = open('Sample_space_01.txt','w+')
        for i in Students_01:
            c01.write(i)


def pickacg(x):
    if x == 12:
        selected = list(pickc12())
        for i in range(len(selected)):
            print(f'第{i + 1}位抽取到的学生是{selected[i]}')
    if x == 1:
        selected = list(pickc01())
        for i in range(len(selected)):
            print(f'第{i + 1}位抽取到的学生是{selected[i]}')
print("************************************************************************")
print('欢迎使用学生抽取小程序，作者：李佳阳')
print('查看已经抽取到的学生，请点击Selected_01或Selected_12文件。')
a = input('请输入要抽取的班级，例如12班就输入12，点击reset.exe来重置。>>  ')
pickacg(int(a))
print(f'学生已抽好，抽到的学生已保存在目录下的selected_{a}文件。')


print("************************************************************************")
input('按Enter(回车)键来退出。 ')








