def add_time(start, duration, starting_day=""):
    #Separate the start time into houres and minutes
    pieces = start.split()
    time = pieces[0].split(":")
    end = pieces[1]
    
    #Calculate twenty four hour clock format
    if end == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)
        
    #Separate the duration into hours and minutes
    durTime = duration.split(":")
    
    #Add hours and minutes
    newHour = int(time[0]) + int(durTime[0])
    newMinutes = int(time[1]) + int(durTime[1])
    
    if newMinutes >= 60 :
        hours_add = newMinutes // 60
        newMinutes -= hours_add * 60
        newHour += hours_add
        
    daysAdd = 0
    if newHour > 24 :
        daysAdd = newHour // 24
        newHour -= daysAdd * 24
        
    #Find AM and PM
    if newHour > 0 and newHour < 12:
        end = "AM"
    elif newHour == 12:
        end = "PM"
    elif newHour > 12:
        end = "PM"
        newHour -= 12
    else:
        end = "AM"
        newHour += 12
        
    if daysAdd > 0 :
        if daysAdd == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(daysAdd) + " days later)"
    else: 
        days_later = ""
            
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        
    if starting_day :
        weeks = daysAdd // 7
        i = weekDays.index(starting_day.lower().capitalize()) + (daysAdd - 7 * weeks)
        if i > 6:
            i -= 7
        day = ", " + weekDays[i]
    else: 
        day = ""
            
    newTime= str(newHour) + ":" + \
        (str(newMinutes) if newMinutes > 9 else ("0" + str(newMinutes))) + \
        " " + end + day + days_later
                
    return newTime
            
        
        