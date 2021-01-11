def add_time(start, duration, day=""):
  print(start)
  print(duration)
  normal_format_hour = convert_to_24_h(start)
  print(normal_format_hour)
  minutes_start = convert_to_minutes(normal_format_hour)
  print(minutes_start)
  minutes_duration = convert_to_minutes(duration)
  print(minutes_duration)
  minutes = minutes_start + minutes_duration
  print(minutes)
  days = convert_to_hour(minutes)
  print(days)




  #return new_time
  
#format HH:MM PM
def convert_to_24_h(hour):
  if "AM" in hour:
    if "12" in hour[:2]:
      return "00" + hour[2:-2]
    return hour[:-2]
  elif "PM" in hour:
    if "12" in hour[:2]:
      return hour[:-2]
    return str(int(hour[:2]) + 12) + hour[2:5] 

def convert_to_minutes(hour):
  hours, minutes = split_by_colon(hour)
  hours = get_rid_of_zero(hours)
  minutes = get_rid_of_zero(minutes)
  minutes += hours * 60
  return minutes

def split_by_colon(hour):
  elements = hour.split(":")
  hours = elements[0]
  minutes = elements[1]
  return hours, minutes

def get_rid_of_zero(number):
  if "0" in number:
    return int(number[1:])
  else:
    return int(number)

def convert_to_hour(minutes):
  hours, minutes = divmod(minutes, 60)
  days, hours = divmod(hours, 24)
  return "{:d}:{:02d}:{:02d}".format(days, hours, minutes)
