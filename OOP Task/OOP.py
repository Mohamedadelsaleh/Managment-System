import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Person:
    personMood = ("Happy", "Tired", "Lazy")

    def __init__(self, name, money, mood, healthRate):
        self.personName = name
        self.personMoney = money
        self.personMood = mood
        self.personHealthRate = healthRate

    def sleep(self, hours):
        if not isinstance(hours, int):
            print("Invalid input, Please Enter a Number")
            return False
        else:
            if hours < 7:
                self.personMood = Person.personMood[1]
                return True
            elif hours > 7:
                self.personMood = Person.personMood[2]
                return True
            elif hours == 7:
                self.personMood = Person.personMood[0]
                return True

    def eat(self, meals):
        if not isinstance(meals, int):
            print("Invalid input, Please Enter a Number")
            return False
        else:
            if meals == 3:
                self.personHealthRate = "100%"
                return True
            elif meals == 2:
                self.personHealthRate = "75%"
                return True
            elif meals == 1:
                self.personHealthRate = "50%"
                return True

    def buy(self, items):
        if not isinstance(items, int):
            print("Invalid input, Please Enter a Number")
            return False
        else:
            totalItems = items * 10
            if totalItems > self.personMoney:
                print("Cost of Items greater than Your Money....!")
                return True
            else:
                print("Successfully Payment")
                self.personMoney -= (10 * items)
                return True

    @property
    def personHealthRate(self):
        return self.__personHealthRate

    @personHealthRate.setter
    def personHealthRate(self,healthRate):
        if not isinstance(healthRate,int):
            print("Invalid Input")
            return False
        else:
            if (healthRate >= 0) and (healthRate <= 100):
                self.__personHealthRate = healthRate
                return True
            if not (healthRate >= 0) and (healthRate <= 100):
                return False


class Employee(Person):

    def __init__(self, id, car, email, salary, distanceToWork):
        self.employeeID = id
        self.employeeCar = car
        self.employeeEmail = email
        self.employeeSalary = salary
        self.employeeDistance = distanceToWork

    @property
    def employeeSalary(self):
        return self.__employeeSalary

    @employeeSalary.setter
    def employeeSalary(self, salary):
        if not isinstance(salary, int):
            print("Invalid input")
        else:
            if salary >= 1000:
                self.__employeeSalary = salary
            if salary < 1000:
                print("Salary Must be 1000 or more....!")
                self.__employeeSalary = 1000

    @property
    def employeeEmail(self):
        return self.__employeeEmail

    @employeeEmail.setter
    def employeeEmail(self, email):
        if re.fullmatch(regex, email):
            self.__employeeEmail = email
            return True
        else:
            print("Invalid Mail Type")
            return False


    def work(self, hours):
        if not isinstance(hours, int):
            print("Invalid input, Please Enter a Number")
            return False
        else:
            if hours < 8:
                self.personMood = Person.personMood[1]
                return True
            elif hours > 8:
                self.personMood = Person.personMood[2]
                return True
            elif hours == 8:
                self.personMood = Person.personMood[0]
                return True


    def drive(self):
        pass

    def refuel(self):
        pass

    def send_Mail(self, toPerson, subject, msg, receiver_name):
        counter = 1
        with open(f"Email.txt", "a") as emailFile:
            emailFile.write(f"From:{self.employeeEmail}")
            emailFile.write(f"To:{toPerson}")
            emailFile.write(" ")
            emailFile.write(f"==================={subject}===================")
            emailFile.write(" ")
            emailFile.write(f"Hello,{receiver_name}")
            emailFile.write(" ")
            emailFile.write(msg)
            emailFile.write(" ")
            emailFile.write("==========================================================================")


class Office:
    def __init__(self, name, employees):
        self.officeName = name
        self.officeEmployees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.carName = name
        self.carFuelRate = fuelRate
        self.carVelocity = velocity

    def run(self):
        pass

    def stop(self):
        pass
