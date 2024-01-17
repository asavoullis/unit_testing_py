import requests

class Employee:
    """ A simple employee class """

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
            return "Employee('{}', '{}', {}, '{}')".format(self.first, self.last, self.pay, self.email, self.fullname)

    def __str__(self):
        return '{} - ${} - {}'.format(self.fullname, self.pay, self.email)

    def __add__(self, other):
        return self.pay + other.pay 

    def attribute_length(self, attribute='fullname'):
        att = attribute.lower()

        if att == 'name' or att == 'first':
            return len(self.first)
        elif att == 'fullname':
            return len(self.fullname)
        elif att in ['surname', 'last']:
            return len(self.last)
        elif att == 'email':
            return len(self.email)
        else:
            raise ValueError("Invalid attribute. [Please type 'name', 'first', 'fullname', 'surname', 'last' or 'email'.")
    
    def give_promotion(self, percentage):
        if percentage < 0:
            raise ValueError("Percentage cannot be negative for promotions.")
        else:
            self.pay = int(self.pay * (1 + percentage / 100))

    def __eq__(self, other):
        return self.pay == other.pay

    def __lt__(self, other):
        return self.pay < other.pay
    
    def monthly_schedule(self, month):
        """
        Intended to fail so I can do a mock test 
        
        The information from that website is something that I would want to mock 
        because I don't want the success of our tests to depend on that website being up
        
        I only care if the get method was called with the correct URL and that the code
        behaves correctly whether the response is okay or not okay
        """
        # pulls an employee's schedule for a given month
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

if __name__ == "__main__":
    # Example usage
    employee = Employee("John", "Doe", 50000)

    # Initial employee details
    print("Initial Name:", employee.first)   
    print("Last Name (Surname):", employee.last) 
    print("Full Name:", employee.fullname)   # Output: Full Name: John Doe
    print("Initial Pay:", employee.pay)              # Output: Initial Pay: 50000
    print("")

    # __repr__ and __str__
    print(repr(employee))  # Employee('John', 'Doe', 50000, 'John.Doe@email.com')")
    a = repr(employee)
    print(type(a))
    print(str(employee))   # John Doe - John.Doe@email.com      

    # __add__
    employee2 = Employee("Jane", "Smith", 60000)
    total_pay = employee + employee2
    print("Jane's and Smith's total salary: ", total_pay)  # 110000
    print("")

    # attribute_length
    print(employee.attribute_length('Email'))  # Length of the email address: (depends on the email format)
    print(employee.attribute_length('name'))   # Length of the first name ('John'): 4
    print(employee.attribute_length('surname'))  # Length of the last name ('Doe'): 3
    print("")
    
    # give_promotion 
    employee.give_promotion(10)
    print(employee.pay)  # New pay after promotion: 55000

    # apply_raise
    employee.apply_raise()
    print(employee.pay)  # New pay after applying the default raise_amt: 57750
    print("")

    # __eq__ and __lt__
    employee3 = Employee("Alice", "Wonder", 55000)
    print(employee == employee3)  # False
    print(employee < employee3)   # True