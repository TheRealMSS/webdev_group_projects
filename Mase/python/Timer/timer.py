import time

def main():

    print("=== TIMER ===")
    work_time = int(input("How many minutes to work: "))
    break_time = int(input("How many minutes to break: "))

    print(f"\nStarting {work_time}-minute work session...")
    pomodoro(work_time)
    
    print(f"\nTake a {break_time}-minute break!")
    pomodoro(break_time)

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


