from entity.Appointment import Appointment
from util.DBConnection import DBConnection
from exception.Exception import PatientNumberNotFoundException,AppointmentNotFoundException
from dao.IHospitalService import IHospitalService

class HospitalServiceImpl(IHospitalService):

    def get_appointment_by_id(self, appointmentId):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", (appointmentId,))
            appointment_data = cursor.fetchone()

            if not appointment_data:
                raise PatientNumberNotFoundException("Appointment with ID {} not found".format(appointmentId))

            appointment = Appointment(*appointment_data)
            return appointment

        except Exception as e:
            print("Error:", e)
            return None

    def get_appointments_for_patient(self, patientId):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", (patientId,))
            appointments_data = cursor.fetchall()

            appointments = []
            for appointment_data in appointments_data:
                appointment = Appointment(*appointment_data)
                appointments.append(appointment)

            return appointments

        except Exception as e:
            print("Error:", e)
            return []

    def get_appointments_for_doctor(self, doctorId):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", (doctorId,))
            appointments_data = cursor.fetchall()

            appointments = []
            for appointment_data in appointments_data:
                appointment = Appointment(*appointment_data)
                appointments.append(appointment)

            return appointments

        except Exception as e:
            print("Error:", e)
            return []

    def schedule_appointment(self, appointment):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?, ?)",
                (appointment.appointmentId, appointment.patientId, appointment.doctorId, appointment.appointmentDate,
                 appointment.description))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_appointment(self, appointment):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE Appointment SET patientId=?, doctorId=?, appointmentDate=?, description=? WHERE appointmentId=?",
                (appointment.patientId, appointment.doctorId, appointment.appointmentDate, appointment.description,
                 appointment.appointmentId))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def cancel_appointment(self, appointmentId):
        try:
            connection = DBConnection.getConnection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Appointment WHERE appointmentId=?", (appointmentId,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

