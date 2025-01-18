class Charity() :
    bn = ""
    cat = ""
    subCat = ""
    designation = ""
    legalName =""
    accName =""
    addressLine1 =""
    addressLine2 =""
    city =""
    province =""
    postalCode =""
    country =""

    def __init__(self, bn, cat, subCat, designation,
                 legalName, accName, addressLine1,
                 addressLine2, city, province,
                 postalCode, country):
        self.bn = bn
        self.cat = cat
        self.subCat = subCat
        self.designation = designation
        self.legalName = legalName
        self.accName = accName
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.province = province
        self.postalCode = postalCode
        self.country = country

    def get_bn(self) :
        return self._bn

    def get_cat(self) :
        return self.cat

    def get_subCat(self) :
        return self.subCat

    def get_designation(self) :
        return self.designation

    def get_legalName(self) :
        return self.legalName

    def get_accName(self) :
        return self.accName

    def get_addressLine1(self) :
        return self.addressLine1

    def get_addressLine2(self) :
        return self.addressLine2

    def get_city(self) :
        return self.city
    
    def get_province(self) :
        return self.province
 
    def get_postalCode(self) :
        return self.postalCode
 
    def get_country(self) :
        return self.country
    
    def set_bn(self, bn) :
        self.bn = bn

    def set_cat(self, cat) :
        self.cat = cat

    def set_subCat(self, subCat) :
        self.subCat = subCat

    def set_designation(self, designation) :
        self.designation = designation

    def set_legalName(self, legalName) :
        self.legalName = legalName

    def set_accName(self, accName) :
        self.accName = accName

    def set_addressLine1(self, addressLine1) :
        self.addressLine1 = addressLine1

    def set_addressLine2(self, addressLine2) :
        self.addressLine2 = addressLine2

    def set_city(self, city) :
        self.city = city
    
    def set_province(self, province) :
       self.province =  province
 
    def set_postalCode(self, postalCode) :
        self.postalCode = postalCode
 
    def set_country(self,country) :
        self.country = country
