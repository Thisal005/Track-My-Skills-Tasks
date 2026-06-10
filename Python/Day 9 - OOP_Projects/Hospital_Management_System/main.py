# Hospital Management System

class Patient:
    p_id = 1000
    def __init__(self):
        self.p_id = Patient.p_id;
        self.p_name = ""
        self.age = 0
        self.p_phone_number = 0
        self.gender = "" 
        self.medical_history = ""
        self.current_appointments = []
        Patient.p_id += 1

    def create_new_patient(self):
        print("Register New Patient")
        self.p_name = input("Enter Full Name : ")
        self.age = input("Enter Patient Age :  ")
        self.p_id = self.p_id + 1
        self.p_phone_number = input("Enter Patient Phone Number : ")
        self.gender = input("Enter Patient Gender : ")
        self.medical_history = input("Enter Patient Medical History : ")
        print("Patient Registered Successfully with ID : ", self.p_id)

        self.p_id = {
            "Id" : self.p_id,
            "Name" : self.p_name,
            "Age" : self.age,
            "Phone Number" : self.p_phone_number,
            "Gender" : self.gender,
            "Medical History" : self.medical_history,
        }
        return self.p_id
    
    def get_patient_info_by_id(self, p_id):
        if self.p_id == p_id:
            return f"Patient ID : {self.p_id} , Patient Name : {self.p_name}, Age : {self.age}, Phone Number : {self.p_phone_number}, Gender : {self.gender}, Medical History : {self.medical_history}"
        else:
            return "Patient not found"
        
class Doctor:
    d_id = 5000
    def __init__(self):
        self.d_id = Doctor.d_id
        self.d_name = ""
        self.specialization = ""
        self.d_phone_number = 0
        self.d_email = ""
        self.current_appointments = []
        Doctor.d_id += 1

    def create_new_doctor(self):
        print("Register New Doctor")
        self.d_name = input("Enter Full Name : ")
        self.specialization = input("Enter Doctor Specialization : ")
        self.d_id += 1
        self.d_phone_number = input("Enter Doctor Phone Number : ")
        self.d_email = input("Enter Doctor Email : ")
        print("Doctor Registered Successfully with ID : ", self.d_id)
        return self.d_id
    
    def get_doctor_info_by_id(self, d_id):
        if self.d_id == d_id:
            return f"Doctor Name : {self.d_name}, Specialization : {self.specialization}, Phone Number : {self.d_phone_number}, Email : {self.d_email}"
        else:
            return "Doctor not found"   
        
class Appointment:
    a_id = 2000
    def __init__(self):
        self.a_id = Appointment.a_id
        self.patient_id = 0
        self.doctor_id = 0
        self.appointment_date = ""
        self.appointment_time = ""
        self.status = ""
        Appointment.a_id += 1

    def create_new_appointment(self, patient_id, doctor_id, appointment_date, appointment_time, status):
        self.a_id = self.a_id + 1
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.status = status
        print("Appointment Created Successfully with ID : ", self.a_id)
        return self.a_id
    
    def get_appointment_info_by_id(self, a_id):
        if self.a_id == a_id:
            return f"Appointment ID : {self.a_id}, Patient ID : {self.patient_id}, Doctor ID : {self.doctor_id}, Appointment Date : {self.appointment_date}, Appointment Time : {self.appointment_time}, Status : {self.status}"
        else:
            return "Appointment not found"
        
    def update_appointment_status(self, a_id, status):
        if self.a_id == a_id:
            self.status = status
            print("Appointment Status Updated Successfully")
        else:
            print("Appointment not found")
        
class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        
    def view_patients(self):
        if len(self.patients) == 0 :
            print("There are no any patients registered")
        for patient in self.patients:
            print(patient.get_patient_info_by_id(patient.p_id))
    
    def view_doctors(self):
        if len(self.doctors) == 0 :
            print("There are no any doctors registered")
        for doctor in self.doctors:
            print(doctor.get_doctor_info_by_id(doctor.d_id))

    def view_appointments(self):
        if len(self.appointments) == 0 :
            print("There are no any appointments scheduled")
        for appointment in self.appointments:
            print(appointment.get_appointment_info_by_id(appointment.a_id))
    
    def get_appointments_by_patient_id(self, patient_id):
        patient_appointments = []
        for appointment in self.appointments:
            if appointment.patient_id == patient_id:
                patient_appointments.append(appointment)
        
        if not patient_appointments:
            print("No appointments found for the given patient ID.")
            return None
        
        for app in patient_appointments:
            print(app.get_appointment_info_by_id(app.a_id))
        return patient_appointments
    
    def get_appointments_by_doctor_id(self, doctor_id):
        doctor_appointments = []
        for appointment in self.appointments:
            if appointment.doctor_id == doctor_id:
                doctor_appointments.append(appointment)
        
        if not doctor_appointments:
            print("No appointments found for the given doctor ID.")
            return None
        
        for app in doctor_appointments:
            print(app.get_appointment_info_by_id(app.a_id))
        return doctor_appointments
    
    def get_appointments_by_id(self, a_id):
        appointments = []
        for appointment in self.appointments:
            if appointment.a_id == a_id:
                appointments.append(appointment)
        
        if not appointments:
            print("No appointments found for the given ID.")
            return None
        
        for app in appointments:
            print(app.get_appointment_info_by_id(app.a_id))
        return appointments
    
    def update_appointment_status(self, a_id, status):
        for appointment in self.appointments:
            if appointment.a_id == a_id:
                appointment.update_appointment_status(a_id, status)
                return appointment
                print("Appointment not found")
        return None

    def create_new_patient(self):
        patient = Patient()
        patient.create_new_patient()
        return patient
    
    def create_new_doctor(self):
        doctor = Doctor()
        doctor.create_new_doctor()
        return doctor
    
    def create_new_appointment(self, patient_id, doctor_id, appointment_date, appointment_time, status):
        appointment = Appointment()
        appointment.create_new_appointment(patient_id, doctor_id, appointment_date, appointment_time, status)
        return appointment
    

print("Welcome to Hospital Management System ")

hospital = Hospital()

while True:
    print("1. Register New Patient")
    print("2. Register New Doctor")
    print("3. Schedule New Appointment")
    print("4. View Patients")
    print("5. View Doctors")
    print("6. View Appointments")
    print("7. Update Appointment Status")
    print("8. Get Appointment by Patient ID ")
    print("9. Get Appointment by Doctor ID ")
    print("10. Get Appointment by ID ")
    print("11. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        patient_id = hospital.create_new_patient()
        hospital.add_patient(patient_id)
    elif choice == 2:
        doctor_id = hospital.create_new_doctor()
        hospital.add_doctor(doctor_id)
       
    elif choice == 3:
        patient_id = int(input("Enter Patient ID : "))
        doctor_id = int(input("Enter Doctor ID : "))
        appointment_date = input("Enter Appointment Date : ")
        appointment_time = input("Enter Appointment Time : ")
        status = input("Enter Appointment Status : ")
        appointment_id = hospital.create_new_appointment(patient_id, doctor_id, appointment_date, appointment_time, status)
        hospital.add_appointment(appointment_id)
       
    elif choice == 4:
        hospital.view_patients()
    elif choice == 5:
        hospital.view_doctors()
    elif choice == 6:
        hospital.view_appointments()
    elif choice == 7:
        appointment_id = int(input("Enter Appointment ID : "))
        status = input("Enter New Status : ")
        hospital.update_appointment_status(appointment_id, status)
    elif choice == 8:
        patient_id = int(input("Enter Patient ID : "))
        hospital.get_appointments_by_patient_id(patient_id)
    elif choice == 9:
        doctor_id = int(input("Enter Doctor ID : "))
        hospital.get_appointments_by_doctor_id(doctor_id)
    elif choice == 10:
        appointment_id = int(input("Enter Appointment ID : "))
        hospital.get_appointments_by_id(appointment_id)
    elif choice == 11:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")