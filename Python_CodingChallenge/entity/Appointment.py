class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def get_appointment_id(self):
        return self.appointmentId

    def set_appointment_id(self, appointmentId):
        self.appointmentId = appointmentId

    def get_patient_id(self):
        return self.patientId

    def set_patient_id(self, patientId):
        self.patientId = patientId

    def get_doctor_id(self):
        return self.doctorId

    def set_doctor_id(self, doctorId):
        self.doctorId = doctorId

    def get_appointment_date(self):
        return self.appointmentDate

    def set_appointment_date(self, appointmentDate):
        self.appointmentDate = appointmentDate

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def Print(self):
        print(f' Appointment_ID: {self.appointmentId},\n Patient_ID: {self.patientId},\n Doctor_ID {self.doctorId},\n Description: {self.description}')