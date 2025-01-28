import time

"""
Planing the classes structure:

Class -> Hospital 
    doctors
    patient
    rooms 
    
    methods:
    add_doctor()
    add_patient()
    register_room()
    
Class -> Person
    name
    indentification
    
Class -> Doctor(Person)
    name
    hospital id
    patients
    
    methods:
    get_patient()
    exam_patient()
    intern_patient()
    treat_patient()
    release_patient()
    
Class -> Patient(Person)
    name
    id
    sickness
    
    methods:
    has_insurance()
    get_diagnosis()
    get_treatment()
    
    
"""

class Person:
    def __init__(self, name, ident):
        self.name =  name
        self.ident = ident
        
    def __str__(self):
        return f"name:{self.name}, id:{self.ident};"

class Doctor(Person):
    
    def __init__(self, name, ident):
        super().__init__(name, ident)
        self.interned_patients = []
        self.patients = []
                        
    def __str__(self):
        return super().__str__() 
    
    def get_patient(self, client):
        result = client.attended() 
        if not result:
            self.patients.append(client)
            print(f"{self.name} successfully got a new patient!")
        elif result:
            print(f"Sorry {self.name}, this patient already has a doctor.")
        else:
            print(f"{self.name}, this patient doesn't exist.")

            
    def release_patient(self, client, hospital):
        result = client.be_released()
        if not result:
            self.patients.remove(client)
            print(f"{self.name} successfuly released your patient '{client.name}'.")
            hospital.remove_patient(client)
        elif result:
            print(f"Sorry {self.name}, this patient dosent have a doctor.")
        else:
            print(f"{self.name} this patient dosent exist.")
        
        
    def intern_patient(self, hospital, patient, room_id):
        add_room = hospital.register_room(patient, room_id)
        try:
            if add_room:
                self.interned_patients.append(patient)
                print(f"Patient {patient.name} has been interned by doctor {self.name}.")
            else:
                print(f"We couldn't register the patient {patient.name}, on room {room_id}")    
        except NameError:
            print("The patent dosent exist!")    
        
    
    def exam_patient(self, patient):
        return patient.sickness
    
    def treat_patient(self, patient):
        patient_sickness = self.exam_patient(patient)
        print(f"we are treating {patient.name} for {patient_sickness} waiting for results...") 
        
        count = 0
        txt = "waiting."
        while count <= 10:
            print(txt)
            count += 1
            txt += "."
            time.sleep(1)
        print("You are cured! Now go to the reception to sing a release form.")
    
    def list_active_patients(self):
        return [str(patient) for patient in self.patients]    
    
    
    
class Patient(Person):
    def __init__(self, name, ident, sickness, has_doctor=False, has_insurance=False):
        super().__init__(name, ident)
        self.sickness = sickness
        self.has_doctor = has_doctor
        self.has_insurance = has_insurance
        
    def __str__(self):
        return super().__str__()
        
    def attended(self):
        if not self.has_doctor:
            self.has_doctor = True
            print(f"{self.name}, now you have a doctor!")
            return False  
        else:
            print(f"The patient {self.name} already has a doctor on their case.")
            return True  
    
    def be_released(self):
        if self.has_doctor:
            self.has_doctor = False
            print(f"{self.name} you are realesed.")
            return False  
        else:
            print(f"The patient {self.name} no longer has a doctor.")
            return True 
    
    
    def get_insurance(self):
        if self.has_insurance:
            return True
        else:
            return False
    
    @classmethod
    def get_diagnosis(cls):
        print(f"The doctor detected a {cls.sickness} we will treat!")
        
    def get_treatment(self, doctor):
        doctor.treat_patient(self)
    

class Hosptal():
    doctors = []
    patients = []
    rooms = []
  
    @classmethod
    def add_doctor(cls, doctor):
        cls.doctors.append(doctor)
    
    @classmethod
    def add_patient(cls, patient):
        result = patient.get_insurance()
        if result:
            cls.patients.append(patient)
            print(f"{patient.name} have insurance, all of your bills will be covered.")
        else:
            cls.patients.append(patient)
            print(f"!WARNING!\n{patient.name} dont have insurance, all of your bills will be charged.")
        
    @classmethod
    def remove_doctor(cls, doctor):
        cls.doctors.remove(doctor)
    
    @classmethod
    def remove_patient(cls, patient):
        cls.patients.remove(patient)
    
    @classmethod
    def register_room(cls, patient, room_id):
        result = cls.search_patient(patient)
        if result:  # Patient is not interned
            new_patient = {"name": patient.name, "id": patient.ident, "room number": room_id}
            cls.rooms.append(new_patient)
            print(f"{patient.name} has been successfully registered in room {room_id}.")
            return True
        else:  # Patient is already interned
            print(f"{patient.name} is already interned in the hospital.")
            return False
    
    @classmethod
    def search_patient(cls, patient):
        for person in cls.rooms:
                if person['id'] == patient.ident:
                    return False
        return True
    
    @classmethod
    def list_doctors(cls):
        return [str(doctor) for doctor in cls.doctors]
    
    @classmethod
    def list_patients(cls):
        return [str(patient) for patient in cls.patients]
    
    @classmethod
    def list_rooms(cls):
        for patient in cls.rooms:
            print(f"In room {patient['room number']} we have {patient['name']};")
        
    
if __name__ == "__main__":    
    doc1 = Doctor("House md", 100)
    pat1 = Patient("Vitin", 201, "influenza", has_insurance=True)
    pat2 = Patient("Eva", 202, "lupus", has_insurance=False)
    
    Hosptal.add_doctor(doc1)
    Hosptal.add_patient(pat1)
    Hosptal.add_patient(pat2)
    print("-----------------")

    print("\n".join(Hosptal.list_doctors()))
    print("-----------------")
    print("\n".join(Hosptal.list_patients()))
        
    print("-----------------")
    doc1.get_patient(pat1)
    doc1.get_patient(pat2)
    print("-----------------")    
    print("\n".join(doc1.list_active_patients()))

    print("-----------------")    
    print(doc1.exam_patient(pat1))
    print(doc1.exam_patient(pat2))
    
    print("-----------------")
    doc1.treat_patient(pat1)
    
    print("-----------------")
    doc1.release_patient(pat1, Hosptal)
    print("-----------------")
    print("\n".join(doc1.list_active_patients()))
    
    print("-----------------")
    #doc1.intern_patient(Hosptal, pat1, 1010)
    doc1.intern_patient(Hosptal, pat2, 2020)
    doc1.treat_patient(pat2)
    
    print("-----------------")
    Hosptal.list_rooms()
    
    print("-----------------")
    print("\n".join(Hosptal.list_patients()))