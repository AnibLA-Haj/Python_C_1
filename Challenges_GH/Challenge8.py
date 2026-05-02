#Challenge 8 

print("Temperatures of the week")
temps = [18,20,22,19,21,23,24]
days = ["Monday", "Tuesday","Wednesday", "Thursday","Friday","Saturday", "Sunday"]
for day in range(len(days)):
    print(days[day], ":",temps[day])
    
print("temperatures from day 2 to day 5 ", temps[1:-2])
temps = [18,20,22,19,21,23,24]
temps.sort()
print(temps)

r = temps.pop(0)
print(r)
print(temps)

del temps[0]
print(temps)
