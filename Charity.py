import pandas as pd

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

    def __init__(self, bn, cat,
                 legalName, accName, addressLine1,
                 addressLine2, city, province,
                 postalCode, country):
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
                bn=row['BN'],
                cat=row['Category'],
                legalName=row['Legal Name'],
                accName=row['Account Name'],
                addressLine1=row['Address Line 1'],
                addressLine2=row['Address Line 2'],
                city=row['City'],
                province=row['Province'],
                postalCode=row['Postal Code'],
                country=row['Country']
            )
            charities.append(charity_instance)
        return charities
    @staticmethod
    def charity_search(category = "", city = ""):
        charities = Charity.from_csv(Charity, "charity.csv")
        charity_chosen = []
        for charity in charities:
            if (charity.cat == category ) and (charity.city == city) :
                charity_chosen.append(charity)
        return charity_chosen
