import time

my_time = int(input("Enter the time in seconds: "))

# # version 1
# for sec in range(0, my_time):
#     print(sec)
#     time.sleep(1)

# # version 2
# for sec in range(my_time, 0, -1):
#     print(sec)
#     time.sleep(1)

# # version 3
# for sec in range(my_time, 0, -1):
#     seconds = sec % 60
#     print(f"00:00:{seconds:02}")
#     time.sleep(1)

# version 4
for sec in range(my_time, 0, -3):
    seconds = sec % 60
    minutes = int(sec / 60) % 60
    print(f"00:{minutes: 02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!")
