Task = input("Enter your task: ")
Time_Bound= input("Is it time-bound? (yes/no): ")
Priority = input("Priority (high/medium/low): ")

match Priority:
    case 'high':
        print("Reminder: " , Task , " is a high priority task that requires immediate attention today!")
    case 'medium':
        print("Reminder: " , Task , " is a medium priority task. You should complete it soon.")
    case 'low':
        print(Task , " is a low priority task. Consider completing it when you have free time.")
if Time_Bound == 'yes':
    print(Task , " is time-bound, you must complete it today.")
elif Time_Bound == 'no':
    print( Task , " is not time-bound, you can complete it later.")