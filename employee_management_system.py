employee={}
def main_menu():
  
    print("\n1.Add Employee\n2.View All Employees\n3.Search for Employee\n4.Exit")
def add_employee():
    try:
        print("Enter details of employee\n")
        emp_id=int(input("Employee ID :"))
        if emp_id in employee:
            print('\nEmployee is already added.')
            return
        name=input("\nName :")
        age=int(input("\nAge :"))
        department=input("Department :")
        salary=float(input("Salary :"))
    
        employee[emp_id]={
            'name':name,
            'age':age,
            'department':department,
            'salary':salary}
        print("employee added successfuly!")
    except valueError:
        print("Invalid input. Please enter correct data.")
    
def view_employee():
    if not employee:
        print("No employee is avilable")
        return
    print("\n{:<10} {:<15} {:<5} {:<15} {:<10}".format(
    "ID", "Name", "Age", "Department", "Salary"))
    print("-"*60)
    for emp_id,details in employee.items():
        print(f"{emp_id:<8} {details['name']:<15} {details['age']:<6} "
              f"{details['department']:<15} {details['salary']:<10}")
def search_employee():
     emp_id=int(input("enter employee id"))
     if emp_id in employee:
        emp=employee[emp_id]
        print(f"name:{emp['name']}")
        print(f"age:{emp['age']}")
        print(f"department:{emp['department']}")
        print(f"salary:{emp['salary']}")
     else:
        print("employee not found") 
while True:
    main_menu()
    c=int(input("ENter your choice(1-4):-"))
    if c==1:
        add_employee()
        
    elif c==2:
        view_employee()
        
    elif c==3:
        search_employee()
        
    elif c==4:
        print("Thank You!")
        break
    else:
        print("invalid details")
        
        