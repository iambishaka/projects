print("==== Employee Record Book ====")

emp_id = int(input("Employee ID : "))

emp_exist = False

with open("employee_records.txt", "r") as file:
    for line in file:
        # print(int(line.split(",")[0]) == emp_id)
        if int(line.split(",")[0]) == emp_id:
            print("Id already exist")
            emp_exist = True
            break

if emp_exist:
    print("Employee data already exist, we cannot proceed further")
else:
    emp_name = input("Employee Name : ")
    emp_phone = int(input("Employee Phone Number : "))
#
    with open("employee_records.txt", "a") as file:
        file.write(f"{emp_id},{emp_name},{emp_phone}\n")
