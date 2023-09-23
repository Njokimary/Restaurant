class Customer:
    #list to hold all customers
    all_customers = []

    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name

    #method to return customers given_name and family_name
    def given_name(self):
        return self.given_name
    
    def family_name(self):
        return self.family_name
