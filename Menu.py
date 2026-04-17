def add_patient():
    print("\n--- Patient Registration ---")
    
    name = input("Enter patient name: ")
    
    while True:
        try:
            age = int(input("Enter patient age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    reason = input("Enter reason for visit: ")
    emergency = input("Is this an emergency? (yes/no): ").lower()

    patient = {
        "name": name,
        "age": age,
        "reason": reason,
        "emergency": emergency
    }

    if age >= 65:
        elderly_option = input("Patient is 65 or older. Choose self-service or assistance: ").lower()
        patient["elderly_option"] = elderly_option

    print("\nPatient Information Recorded:")
    print("Name:", patient["name"])
    print("Age:", patient["age"])
    print("Reason for Visit:", patient["reason"])
    print("Emergency:", patient["emergency"])

    if "elderly_option" in patient:
        print("Service Type:", patient["elderly_option"])


add_patient()