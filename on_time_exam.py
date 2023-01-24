hour_exam = int(input())
minute_exam = int(input())
hour_student = int(input())
minute_student = int(input())

minutes_total = hour_exam * 60 + minute_exam #640
minutes_arrival = hour_student * 60 + minute_student #600

diff = minutes_total - minutes_arrival

if diff > 30:
    print("Early")
elif 0 <= diff <= 30:
    print("On time")
else:
    print("Late")

hours = 0
minutes = abs(diff)

result = ""

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

if hours > 0:
    result = f"{hours}:{minutes:02d} hours"
else:
    result = f"{minutes} minutes"

if diff > 0:
    result += " before the start"
elif diff < 0:
    result += " after the start"

print(result)




