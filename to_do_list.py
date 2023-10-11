#open the file and set to append mode

#select method to select what a user want

for i in range(0,100):
    
    to_do = int(input("prees 1 for creating a to do list: "))
    if(to_do==1):
        f = open('to_do_list.txt','a')
        list = str(input("Enter what you want to save: "))
        f.write(list)
    elif(to_do==0):
        print("sucessfully exited from the code")
        f.close()
        break
