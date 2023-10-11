import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(1, 100):
#     os.mkdir(f"data/Roll{i+1}")
# for i in range(1,100):
#     os.rename(f"data/Roll{i+1}",f"data/id{i+1}")
# folders = os.listdir("data")
# for folder in folders:
#     print(folder)
# print(os.getcwd())
# os.chdir("data/id2")
# To read a file we use 'r',to write a file we use'w' to add additional content we use 'a'
# f = open('my file.txt','w')
# f.write('My name id Yesin Arafat')
name = str(input("Enter your name: "))
f = open('my file.txt','a')
f.write(f'my name is {name}')
# print(text)
f.close()
# y = open('y.txt','r')
# text2 = y.read()
# print(text2)
# y.close()