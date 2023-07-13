#airline - track of the booked seats

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self,name):
        if not self.open_seats():  #if open_seats is not 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

people = ['Harry', "Ron",'Hermione', "Ginny"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} to flight succs")
    else:
        print(f"no available seat for {person}")
