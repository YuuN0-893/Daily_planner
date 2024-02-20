# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Activity:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

def check_conflicts(activities):
    conflicts = []
    for i in range(len(activities)):
        for j in range(i+1, len(activities)):
            if (activities[i].start_time < activities[j].end_time and 
                activities[i].end_time > activities[j].start_time):
                conflicts.append((activities[i], activities[j]))
    return conflicts

def parse_activity():
    name = input("Enter activity name: ")
    start_time = input("Enter start time (e.g., 9:00): ")
    end_time = input("Enter end time (e.g., 10:00): ")
    return Activity(name, start_time, end_time)

def export_activities(activities, filename):
    with open(filename, 'w') as file:
        for activity in activities:
            file.write(f"{activity.name}, {activity.start_time}, {activity.end_time}\n")
#yesyes

def main():
    activities = []

    # Dynamically insert activities
    while True:
        choice = input("Do you want to add a new activity? (yes/no): ")
        if choice.lower() != 'yes':
            break
        activity = parse_activity()
        activities.append(activity)
    # Export activities to a file
    export_filename = input("Enter filename to export activities (e.g., activities.txt): ")
    export_activities(activities, export_filename)
    print("Activities exported successfully.")

    # Check for conflicts
    conflicts = check_conflicts(activities)

    if conflicts:
        print("Conflicts found:")
        for activity1, activity2 in conflicts:
            print(f"Conflict between {activity1.name} and {activity2.name}")
    else:
        print("No conflicts found")

if __name__ == "__main__":
    main()
