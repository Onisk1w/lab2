import os
print("введите название дирректорию")
path = input()
print(os.listdir(path))
for i in os.listdir(path):
    print(i,type(i),path+'\\'+i)