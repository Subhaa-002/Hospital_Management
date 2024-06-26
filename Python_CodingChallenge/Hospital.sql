CREATE DATABASE Hospital;
CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    dateOfBirth DATE,
    gender VARCHAR(10),
    contactNumber VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    specialization VARCHAR(255),
    contactNumber VARCHAR(20)
);

CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY,
    patientId INT,
    doctorId INT,
    appointmentDate DATE,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId),
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId)
);
INSERT INTO Patient (patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address)
VALUES
    (1, 'Ramesh', 'Kumar', '1990-01-01', 'Male', '9876543210', '123, ABC Street, Bangalore, Karnataka, 560001'),
    (2, 'Sita', 'Devi', '1985-05-15', 'Female', '8765432109', '456, XYZ Street, Mumbai, Maharashtra, 400001'),
    (3, 'Amit', 'Sharma', '1988-07-20', 'Male', '7654321098', '789, PQR Street, Delhi, Delhi, 110001'),
    (4, 'Priya', 'Singh', '1992-03-10', 'Female', '6543210987', '1011, LMN Street, Kolkata, West Bengal, 700001'),
    (5, 'Raj', 'Patel', '1987-11-25', 'Male', '5432109876', '1213, GHI Street, Chennai, Tamil Nadu, 600001');



INSERT INTO Doctor (doctorId, firstName, lastName, specialization, contactNumber)
VALUES
    (1, 'Dr. Gupta', 'Kumar', 'General Physician', '9876543210'),
    (2, 'Dr. Sharma', 'Devi', 'Dentist', '8765432109'),
    (3, 'Dr. Patel', 'Singh', 'Ophthalmologist', '7654321098');

INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description)
VALUES
    (1, 1, 1, '2024-03-20', 'Regular checkup'),
    (2, 2, 2, '2024-03-21', 'Dental appointment'),
    (3, 3, 3, '2024-03-22', 'Eye checkup'),
    (4, 4, 1, '2024-03-23', 'Follow-up appointment'),
    (5, 5, 2, '2024-03-24', 'General consultation');

