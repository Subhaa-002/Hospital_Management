
class Doctor:
    def __init__(self, doctorId="", firstName="", lastName="", specialization="", contactNumber=""):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    def get_doctor_id(self):
        return self.__doctorId

    def set_doctor_id(self, doctorId):
        self.__doctorId = doctorId

    def get_first_name(self):
        return self.__firstName

    def set_first_name(self, firstName):
        self.__firstName = firstName

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, lastName):
        self.__lastName = lastName

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def get_contact_number(self):
        return self.__contactNumber

    def set_contact_number(self, contactNumber):
        self.__contactNumber = contactNumber

