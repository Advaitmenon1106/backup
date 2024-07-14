"""
symbols:-
flight: flight is on time
college: students attend college
weather: weather is good
holiday: students have a holiday
on_time: Anshuman reaches home on time


sentences:-

weather->flight
~holiday
~weather <-> holiday
college V holiday
~(college ^ holiday)
flight -> on_time

"""

from easy_logic import *

flight = Symbol('flight')
college = Symbol('college')
weather = Symbol('weather')
holiday = Symbol('holiday')
on_time = Symbol('Anshuman_is_on_time')

knowledge = And(
    Implication(weather, flight),
    Not(holiday),
    Biconditional(Not(weather), holiday),
    Or(college, holiday),
    Not(And(college, holiday)),
    Implication(flight, on_time)
)

print(model_check(knowledge=knowledge, query=on_time))

# Yes Anshuman reached home on time