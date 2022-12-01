class Customer:
    # pass allows you to avoid errors if class is incomplete
    #pass
    # need to pass self so the class can refer back to itself

    # this is a class variable - denoted by the _
    _sports = ["Golf", "Running", "Horse Riding", "Swimming"]

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer created")

    def __str__(self):
        return self.name + " " + self.membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership

     # for static methods can either use the decorator or call it on the class e.g. Customer.read_customers()
    @staticmethod
    def read_customers():
        print("Reading all customers from database")

    # can modify class variables - unlike static methods
    @classmethod
    def update_sports(cls, new_sport):     # cls stands for class
        cls._sports.append(new_sport)

    # can modify class variables - unlike static methods
    @classmethod
    def show_sports(cls):     # cls stands for class
        for sport in cls._sports:
            print(sport)

customers = [Customer("Simon", "Bronze"), Customer("Sarah", "Gold")]

print(customers[0].membership_type)

# add a new attribute to an individual instance
customers[1].verified = True
print(customers[1].verified)

print(customers[0])
customers[0].update_membership("Silver")
print(customers[0])

# Both of these are okay if decorator is used
customers[0].read_customers()
Customer.read_customers()

Customer.update_sports("Cycling")
Customer.show_sports()

# Inheritance
class Owner(Customer):
    def facts():
        print("I am an owner")

owner_one = Owner("Tim", "Bronze")
print(owner_one)
print(Owner.facts())
