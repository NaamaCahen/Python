import datetime


class Airline:
    def __init__(self, id: str, name):
        self.id = id
        self.name = name
        self.planes = []

    def add_plane(self, airplane):
        self.planes.append(airplane)


class Airplane:
    def __init__(self, id: int, current_location, company, next_flights):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights

    def fly(self, destination):
        self.current_location = destination

    def location_on_date(self, date):
        if date >= datetime.datetime.now():
            for flight in self.next_flights:
                if flight.date >= date:
                    return flight.origin.city
        else:
            return 'not valid date'

    def available_on_date(self, date, location):
        pass


class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = destination.city + plane.company.id + str(date)

        self.origin.add_to_departures(self)
        self.destination.add_to_arrivals(self)

    def take_off(self):
        pass

    def land(self):
        pass


class Airport:
    def __init__(self, city: str, planes, scheduled_departures, scheduled_arrivals):
        self.city = city
        self.planes = planes
        self.scheduled_depatures = scheduled_departures
        self.scheduled_arrivals = scheduled_arrivals

    def schedule_flight(self, destination, datetime):
        pass

    def info(self, start_date, end_date):
        pass

    def add_to_departures(self,flight: Flight):
        #if the list is empty
        if len(self.scheduled_depatures == 0):
            self.scheduled_depatures.append(flight)
        else:
            # insert the flight in the order of the dates (to keep the list sorted by date)
            for i in range(len(self.scheduled_depatures)):
                if self.scheduled_depatures[i].date >= flight.date:
                    self.scheduled_depatures.insert(i + 1, flight)



natbag = Airport(city='Tel Aviv', planes=[], scheduled_departures=[], scheduled_arrivals=[])
cdg = Airport(city='Paris', planes=[], scheduled_departures=[], scheduled_arrivals=[])

elal = Airline('EL', 'Elal')
easyjet = Airline('EJ', 'easyjet')

airplane1 = Airplane(id=1, current_location=natbag, company=elal, next_flights=[])
airplane2 = Airplane(id=2, current_location=cdg, company=easyjet, next_flights=[])

elal.add_plane(airplane1)

flight1 = Flight(date=datetime.date(2023,3,15),destination=cdg, origin=natbag, plane=airplane1)
flight2 = Flight(date=datetime.date(2023,3,28),destination=natbag, origin=cdg, plane=airplane1)