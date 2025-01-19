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

def return_matches(person: Person) -> list : # returns all of the matches, no repeats
    matches = []
    precise = Charity.charity_search(person.interest, person.hometown)
    interest_list = Charity.charity_search(person.interest, "")
    city_list = Charity.charity_search("", person.hometown)
    matches = matches.extend(precise);
    matches = matches.extend(interest_list)
    matches = matches.extend(city_list)
    if not matches : return None
    return matches
