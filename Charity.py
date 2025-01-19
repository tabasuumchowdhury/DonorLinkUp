import pandas as pd
import json

class Charity:
    bn = ""
    cat = ""
    legalName = ""
    accName = ""
    addressLine1 = ""
    addressLine2 = ""
    city = ""
    province = ""
    postalCode = ""
    country = ""

    def __init__(self, bn, cat, legalName, accName, addressLine1, 
                 addressLine2, city, province, postalCode, country):
        self.bn = bn
        self.cat = cat
        self.legalName = legalName
        self.accName = accName
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.province = province
        self.postalCode = postalCode
        self.country = country

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get('bn', ""),
            data.get('cat', ""),
            data.get('legalName', ""),
            data.get('accName', ""),
            data.get('addressLine1', ""),
            data.get('addressLine2', ""),
            data.get('city', ""),
            data.get('province', ""),
            data.get('postalCode', ""),
            data.get('country', "")
        )

    @classmethod
    def from_csv(cls, file_path):
        charities = []
        df = pd.read_csv(file_path, encoding='utf-8', on_bad_lines="skip", 
                         keep_default_na=False, na_values=["", "NA", "N/A"])
        for _, row in df.iterrows():
            charity_instance = cls(
                bn=str(row['BN']),
                cat=str(row['Category']),
                legalName=str(row['Legal Name']),
                accName=str(row['Account Name']),
                addressLine1=str(row['Address Line 1']),
                addressLine2=str(row['Address Line 2']),
                city=str(row['City']),
                province=str(row['Province']),
                postalCode=str(row['Postal Code']),
                country=str(row['Country'])
            )
            charities.append(charity_instance)
        return charities
    
    def get_city(self):
        return self.city
    
    def get_category(self):
        return self.cat
    
    def to_json(self):
        obj = {"bn",self.bn, "cat", self.cat, "city", self.city}
        return json.dumps(obj)
    
    def __str__(self):
        return self.to_json()

    @classmethod
    def charity_search(cls, category="", city=""):
        charities = cls.from_csv("charity.csv")
        charity_chosen = []
        for charity in charities:
            if (category.lower() in charity.get_category().lower()) and (city.lower() in charity.get_city().lower()):
                charity_chosen.append(charity)
        return charity_chosen
