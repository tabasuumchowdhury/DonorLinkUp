from Charity import Charity

class Person : 
    cur = 0
    name = ""
    email = ""
    interest = ""
    hometown = ""
    matches = list() # keeps track of matches
    def __init__(self, name, email, interest, hometown):
        self.name = name
        self.email = email
        self.interest = interest
        self.hometown = hometown


def get_interest(self) :
    return self.interest

def get_city(self) :
    return self.hometown

def compatibility(person: Person, charity: Charity) -> bool:
    return charity.city == person.hometown

def return_matches(person: Person) : # returns 5 of the matches, no repeats
    {
        # if we can find 5 charities with same interest and city, return those and add to the matches
        # else if we can find 5 charities with the same interest then we can add to the matches
        # else if we can find 5 charities in the same city then we add to the matches
        # else we return a message saying that we ran out of matches and we just return 5 random charities
    }
