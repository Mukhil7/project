def add_time(start, duration, start_day=None):
  start_time, period = start.split()
  start_hours, start_minutes = map(int, start_time.split(':'))

  duration_hours, duration_minutes = map(int, duration.split(':'))

  if period == "PM":
      start_hours += 12

  total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes

  days = total_minutes // (24 * 60)
  remaining_minutes = total_minutes % (24 * 60)

  result_hours = remaining_minutes // 60
  result_minutes = remaining_minutes % 60
  result_period = "AM" if result_hours < 12 else "PM"

  if result_hours == 0:
      result_hours = 12
  elif result_hours > 12:
      result_hours -= 12

  result_time = f"{result_hours:02}:{result_minutes:02} {result_period}"

  if start_day:
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_day_index = days_of_week.index(start_day.lower().capitalize())
      new_day_index = (start_day_index + days) % 7
      result_day = days_of_week[new_day_index]

      if days == 1:
          result = f"{result_time}, {result_day} (next day)"
      elif days > 1:
          result = f"{result_time}, {result_day} ({days} days later)"
      else:
          result = f"{result_time}, {result_day}"
  else:
      if days == 1:
          result = f"{result_time} (next day)"
      elif days > 1:
          result = f"{result_time} ({days} days later)"
      else:
          result = result_time

  return result

# Get user input for start time, duration, and optional starting day
start = input("Enter the start time (e.g., 3:00 PM): ")
duration = input("Enter the duration (e.g., 3:10): ")
start_day = input("Enter the starting day of the week (optional, e.g., Monday): ")

result = add_time(start, duration, start_day)
print("Result:", result)


