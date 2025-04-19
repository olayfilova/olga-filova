# OPEN TO EXPANSION/CLOSE TO CHANGES
class CalculateSalary:
    def __init_(self, salary):
        self.salary = salary


class SalaryTrainee(CalculateSalary):
    def calculate_salary(self):
        return self.salary * 0.5


class SalaryJunior(CalculateSalary):
    def calculate_salary(self):
        return self.salary * 1


class SalaryMiddle(CalculateSalary):
    def calculate_salary(self):
        return self.salary * 1.5


