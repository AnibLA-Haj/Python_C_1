#ATTENDANCE SYSTEM


print("-----------------------------------")
print("          Attendance System        ")
print("----------------------------------\n")

students = ['alice', 'bob', 'david', 'henry','sofia', 'zein','aria']

c_present = 0
c_absent = 0
present = []
absent = []

for student in students:
    print("Enter 'P' for Present, and 'A' for absent")
    user_enter = input(f"Is student {student} present: ")
    if user_enter == "P":
       # for p in present:
        # present = present + student
        present.append(student)
        c_present += 1
  #  print(f"{c_present}.{present}")
 
    elif user_enter == "A":
       # for a in absent:
        absent.append(student)
        c_absent += 1
  # print(f"{c_absent}.{absent}")

    else:
        print("Please Enter only 'P' -Present or 'A' - Absent.")
        continue
    ##error nuk po mi qet studentat qe jane absent edhe ata qe jane present
print(f"{c_present}.{present}")
print(f"{c_absent}.{absent}")

print("Students that are present: ")
for p in present:
    print()
   # print("Students that are present: ")
    print(f"{c_present}.{p}")
print("Students that are absent:")
for a in absent:
    print()
    #print("Students that are absent:")
    print(f"{c_absent}.{a}")
# ERROR PO MA PERSERIT LISTEN JO VLERAT NJA KA NJO
    










