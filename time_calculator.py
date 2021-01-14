def add_time(start, duration, input_day=""):
  start_minutes = convert_hour_to_minutes(convert_hour_to_24_h_time(start))
  duration_minutes = convert_hour_to_minutes(duration)
  sum_of_minutes = start_minutes + duration_minutes
  raw_time, past_days = convert_minutes_to_hour(sum_of_minutes)
  raw_time_converted = convert_hour_to_12_h_time(raw_time)
  
  if input_day == "":
    if past_days == 0: 
      new_time = raw_time_converted
    elif past_days > 0:
      past_days_text = display_past_days(past_days)
      new_time = raw_time_converted +" "+ past_days_text
  else:
    input_day_index = display_week_day_index(input_day)
    new_weekday = display_weekday(calculate_new_week_day(past_days,input_day_index))
    if past_days == 0: 
      new_time = raw_time_converted +", "+ input_day
    elif past_days > 0:
      past_days_text = display_past_days(past_days)
      new_time = raw_time_converted +", "+ new_weekday +" "+ past_days_text
  return new_time
  
#format HH:MM PM
def convert_hour_to_24_h_time(hour):
  hours, minutes = split_hour_by_colon(hour)
  if "AM" in hour:
    if hours == 12:
      return "00" + minutes
    return "{:d}:{:02d}".format(hours, minutes)
  elif "PM" in hour:
    if hours == 12:
      return "{:d}:{:02d}".format(hours, minutes)
    return "{:d}:{:02d}".format(hours+12, minutes) 

def convert_hour_to_12_h_time(hour):
  hours, minutes = split_hour_by_colon(hour)
  if hours > 12:
    hours = hours - 12
    return "{:d}:{:02d} PM".format(hours, minutes)
  elif hours == 12:
    return "{:d}:{:02d} PM".format(hours, minutes)
  elif hours == 0:
    hours = 12
    return "{:d}:{:02d} AM".format(hours, minutes)
  else:
    return "{:d}:{:02d} AM".format(hours, minutes)

def convert_hour_to_minutes(hour):
  hours, minutes = split_hour_by_colon(hour)
  minutes += hours * 60
  return minutes

def split_hour_by_colon(hour):
  elements = hour.split(":")
  hours = int(elements[0])
  right_side = elements[1].split(" ")
  minutes = int(right_side[0])
  return hours, minutes

def convert_minutes_to_hour(minutes):
  hours, minutes = divmod(minutes, 60)
  days, hours = divmod(hours, 24)
  return "{:d}:{:02d}".format(hours, minutes), days

def display_past_days(days):
  if days == 1:
    return "(next day)"
  else:
    return "({} days later)".format(days)

def display_week_day_index(day):
  weekdays = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
  day = day.lower()
  for index, weekday in enumerate(weekdays):
    if day == weekday: return index  

def calculate_new_week_day(past_days,input_day_index):
  return divmod(past_days + input_day_index,7)[1]

def display_weekday(day_index):
  weekdays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
  return weekdays[day_index]