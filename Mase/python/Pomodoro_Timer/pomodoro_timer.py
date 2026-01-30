import time

def main():
    print("=== POMODORO TIMER ===")
    print("\nStarting timer")
    pomodoro(25)

    print("Take a 5 minute break")
    pomodoro(5)
""" 
print("3 seconds to blast off...")
time.sleep(3)
print("Blast off!") """

""" 
print("Prepare for blast off...")
time.sleep(3)
print("launching...")
countdown = 3
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1
print("Blast off!")     """



def pomodoro(minutes):
    
    total_seconds = minutes * 60

    while total_seconds > 0:
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f"{minutes}: {seconds:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("Times up")
    print("\n\a\a\aTime's up!")    

if __name__ == '__main__':
    main()  


