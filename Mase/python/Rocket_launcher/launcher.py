import time

print("3 seconds to blast off...")
time.sleep(3)


print("Prepare for blast off...")
time.sleep(3)
print("launching in...")
time.sleep(1)
countdown = 3
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1
print("Blast off!")     

