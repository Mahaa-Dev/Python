import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

if (int(time.strftime('%H')) >= 1 and int(time.strftime('%H')) < 12):
    print("Good morning")
elif (int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) < 20):
    if (int(time.strftime('%H')) >= 12 and int(time.strftime('%H')) < 16):
        print("Good afternoon")
    elif (int(time.strftime('%H')) >= 16 and int(time.strftime('%H')) <= 20):
        print("Good evening")
    else:
        print("Good night")

else:
    print("Good night")
