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
