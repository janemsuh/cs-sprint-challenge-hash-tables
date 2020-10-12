#  Hint:  You may not need all of these.  Remove the unused functions.
"""
Given an array of tickets with source and destination cities, return a list of cities in flight order

We can hash each ticket such that the starting location is the key and
the destination is the value. Then, when constructing the entire
route, the `i`th location in the route can be found by checking the
hash table for the `i-1`th location.
"""

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # create dict
    flight_dict = dict()

    # source as key, destination as value
    for ticket in tickets:
        flight_dict[ticket.source] = ticket.destination

    # loop through tickets
    route = []
    city = flight_dict['NONE']
    while city != 'NONE':
        route.append(city)
        city = flight_dict[city]
    # test file seems to include 'NONE' at the end of route list
    route.append('NONE')

    return route

"""
flight1 = Ticket('NONE', 'LGA')
flight2 = Ticket('LGA', 'CLT')
flight3 = Ticket('CLT', 'DCA')
flight4 = Ticket('DCA', 'PWM')
flight5 = Ticket('PWM', 'NONE')

flights = (flight1, flight2, flight3, flight4, flight5)
# output: ['LGA', 'CLT', 'DCA', 'PWM']

print(reconstruct_trip(flights, 5))
"""