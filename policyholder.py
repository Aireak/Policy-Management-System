### policyholder.py
class Policyholder:
    def __init__(self, id, name, sex, status='active'):
        self.id = id
        self.name = name
        self.sex = sex
        self.status = status
        
    def register(self):
        self.status = 'active'
        print(f"Policyholder {self.name} registered.")

    def suspend(self):
        self.status = 'suspended'
        print(f"Policyholder {self.name} suspended.")

    def reactivate(self):
        self.status = 'active'
        print(f"Policyholder {self.name} reactivated.")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Sex:{self.sex}, Status: {self.status}"

