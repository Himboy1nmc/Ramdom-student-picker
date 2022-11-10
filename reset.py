
def AddSamplespace():
    #样本空间：1班
    class_01 = open('Sample_space_01.txt','w+')
    for i in range(51):
        class_01.write(f'{i+1} \n')
    class_01.close()
    #样本空间:12班
    class_12 = open('Sample_space_12.txt','w+')
    for i in range(54):
        class_12.write(f'{i+1} \n')
    class_12.close()
def resetSelected():
    s01 = open('Selected_01.txt','w+')
    s02 = open('Selected_12.txt','w+')
    s01.close()
    s02.close()
AddSamplespace()
resetSelected()
input('已重置完毕，按Enter键来退出。 ')
