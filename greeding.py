import datetime
current_time = datetime.datetime.now().time()
current_hour = current_time.hour
if(5<current_hour<12):
    print("Good morning")
elif(11<current_hour<14):
    print("Good Noon")
elif(13<current_hour<16):
    print("Good Afternoon")
elif(15<current_hour<21):
    print("Good evening")
else:
    print("good night")
print()
print()