class Employee:
    def __init__(self, emp_id, name, base_salary):
        """Initialize employee with id, name and base salary."""
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self):
        """Display employee basic information."""
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Base Salary:", self.base_salary)

    def annual_salary(self):
        """Return the annual salary calculated from base salary."""
        return self.base_salary * 12


class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, department, bonus):
        """Initialize manager with employee details and manager specific attributes."""
        super().__init__(emp_id, name, base_salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self):
        """Calculate total annual salary including bonus."""
        return self.annual_salary() + self.bonus

    def display_manager(self):
        """Display complete manager details including department and total salary."""
        self.display_employee()
        print("Department:", self.department)
        print("Bonus:", self.bonus)
        print("Total Annual Salary:", self.total_salary())
        print("-----------------------")


# Creating manager objects
manager1 = Manager(201, "Rahul", 50000, "IT", 100000)
manager2 = Manager(202, "Priya", 60000, "HR", 120000)
manager3 = Manager(203, "Amit", 55000, "Finance", 90000)

# Storing managers in a list
managers = [manager1, manager2, manager3]

# Displaying manager details
for m in managers:
    m.display_manager()