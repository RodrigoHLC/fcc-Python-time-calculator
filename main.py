def add_time(start, duration, day=""):
    if duration == "0:00": 
        return start
    # --- GET START TIME DATA ---
    colon_index = start.index(":")
    start_hour = int(start[:colon_index])
    start_min = int(start[colon_index+1:colon_index+3])
    start_moment = start[-2::]
    start_day = day
    # --- GET DURATION DATA ---
    colon_index = duration.index(":")
    duration_hour = int(duration[:colon_index])
    duration_min = int(duration[colon_index+1:colon_index+3])

    # --- ADD MINUTES ---
    final_min = start_min + duration_min
    # IF ADDED MINUTES CREATE NEW HOUR
    if final_min > 59:
        duration_hour += 1
        final_min -= 60
        # IF final_min IS A SINGLE DIGIT, ADD 0 BEFORE IT
        if final_min < 10:
            final_min = f"0{final_min}"

    # --- ADD HOURS ---
    carry_days = 0
    if start_moment == "PM":
        # SWITCH TO 24-HOUR FORMAT
        start_hour += 12

    # CALCULATE HOW MANY DAYS THE HOURS EQUAL
    carry_days = duration_hour // 24
    # ONLY ADD HOURS THAT ARE LOWER THAN 24
    duration_hour = duration_hour % 24
    # ADD HOURS
    final_hour = start_hour + duration_hour
    # RESULT NEEDS TO BE LESS THAN 24
    if final_hour >= 24:
        carry_days += 1
        if final_hour > 24:
            final_hour %= 24
    # GO BACK TO 12-HOUR FORMAT
    if (final_hour >=1 and final_hour <12) or final_hour == 24 :
        end_moment = "AM"
    else:
        end_moment = "PM"
    if final_hour >= 13:
        final_hour -= 12

        
    # IF END-TIME IS ON A DIFFERENT DAY
    diff_day_str = ""
    if carry_days == 1:
        diff_day_str = "(next day)"
    elif carry_days >1:
        diff_day_str = f"({carry_days} days later)"
    
    
    # OPTIONAL CASE: day PARAMETER IS USED
    if day:
        days_list = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        final_day_index = (days_list.index(day.lower()) + carry_days) % 7
        final_day = days_list[final_day_index][:1].upper()  +  days_list[final_day_index][1:]
        # PREPARE FINAL STRING
        new_time = f"{final_hour}:{final_min} {end_moment}, {final_day}"
        # IF END-TIME IS ON A DIFFERENT DAY
        if diff_day_str:
            new_time += f" {diff_day_str}"
        return new_time

    # IF NO day PARAMETER WAS USED
    # PREPARE FINAL STRING
    new_time = f"{final_hour}:{final_min} {end_moment}"
    if diff_day_str:
            new_time+=f" {diff_day_str}"
    return new_time

print(add_time('3:30 PM', '0:00'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
