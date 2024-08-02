# Code written by Peter
# Contact info is peter@husky.nz

# print the application name
print("Meeting time calculator")

# ask our user to input the meeting start end and run time
meeting_start_hour_time = int(input("Please enter the start time (hours): "))
meeting_start_minute_time = int(input("Please enter the start time (minutes): "))
meeting_run_time = int(input("Please enter the duration (minutes): "))

# do our main caculations
start_time_hour_to_minutes = meeting_start_hour_time * 60 + meeting_start_minute_time
start_time_with_duration = start_time_hour_to_minutes + meeting_run_time
start_time_with_duration_hours = int(start_time_with_duration / 60)
start_time_with_duration_minutes = int(start_time_with_duration % 60)


# Print our output
print(f"\nThe meeting will start at {meeting_start_hour_time:0>2d}:{meeting_start_minute_time:0>2d}")
print(f"The meeting will end at {start_time_with_duration_hours:0>2d}:{start_time_with_duration_minutes:0>2d}\n")
