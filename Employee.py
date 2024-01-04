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
        return '{}.{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
            return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self, attribute='fullname'):
        if attribute == 'name':
            return len(self.first)
        elif attribute == 'fullname':
            return len(self.fullname)
        elif attribute == 'surname':
            return len(self.surname)
        else:
            raise ValueError("Invalid attribute. Use 'name', 'fullname', or 'surname'.")

    def give_promotion(self, percentage):
        self.pay = int(self.pay * (1 + percentage / 100))

    def __eq__(self, other):
        return self.pay == other.pay

    def __lt__(self, other):
        return self.pay < other.pay

if __name__ == "__main__":
    # Example usage
    employee = Employee("John", "Doe", 50000)

    print(len(employee))  # Prints the length of the full name
    print(len(employee, 'name'))  # Prints the length of the first name
    print(len(employee, 'surname'))  # Prints the length of the surname