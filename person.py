from Charity import Charity

class Person:
    def __init__(self, name, email, interest, hometown):
        self.name = name
        self.email = email
        self.interest = interest
        self.hometown = hometown
        self.matches = []

    def get_interest(self):
        return self.interest

    def get_city(self):
        return self.hometown

    def return_matches(self) -> list:
        matches = []
        precise = Charity.charity_search(self.interest, self.hometown)
        interest_list = Charity.charity_search(self.interest, "")
        city_list = Charity.charity_search("", self.hometown)
        matches.extend(precise)
        matches.extend(interest_list)
        matches.extend(city_list)
        return matches

