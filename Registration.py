def patient_registration():
    name=get_name()
    age=get_age()
    reason =get_reason()
    print(f"{name} is {age} years old and reason for visit is {reason}")
def get_name():
    name=input("Patient Name: ")
    return name
def get_age():
            age=int(input("Patient Age: "))
            return age
def get_reason():
           reason=input("Reason for visit: ")
           return reason

if __name__=="__main__":
    patient_registration()


