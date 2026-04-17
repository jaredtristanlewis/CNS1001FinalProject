# =============================================================================
# CLINIC PATIENT QUEUE MANAGER SYSTEM
# =============================================================================



priority_queue = []
regular_queue = []

_next_priority_ticket = 1
_next_regular_ticket = 1

AVG_TIME_PER_PATIENT = 25  # minutes per patient


# -----------------------------
# TICKET SYSTEM
# -----------------------------

def issue_priority_ticket(patient):
    global _next_priority_ticket
    patient["queue_line"] = "PRIORITY"
    patient["ticket"] = f"P-{_next_priority_ticket:04d}"
    _next_priority_ticket += 1


def issue_regular_ticket(patient):
    global _next_regular_ticket
    patient["queue_line"] = "REGULAR"
    patient["ticket"] = f"R-{_next_regular_ticket:04d}"
    _next_regular_ticket += 1


# -----------------------------
# Registration
# -----------------------------

def get_name():
    while True:
        name = input("Patient Name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def get_age():
    while True:
        try:
            age = int(input("Patient Age: "))
            if age > 0:
                return age
            print("Age must be positive.")
        except:
            print("Invalid input. Enter a number.")


def get_reason():
    while True:
        reason = input("Reason for Visit: ").strip()
        if reason:
            return reason
        print("Reason cannot be empty.")


def yes_no(prompt):
    while True:
        ans = input(prompt).lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Enter yes or no.")


# -----------------------------
# VALIDATION
# -----------------------------

def validate(name, age, reason, elderly_flag):
    errors = []

    if not name:
        errors.append("Name missing")
    if age <= 0:
        errors.append("Invalid age")
    if not reason:
        errors.append("Reason missing")
    if elderly_flag and age < 65:
        errors.append("Elderly assistance only for 65+")

    return (len(errors) == 0, errors)


# -----------------------------
# PRIORITY SYSTEM
# -----------------------------

def priority_level(emergency, age, elderly):
    if emergency:
        return "Emergency"
    if age >= 65 and elderly:
        return "Urgent"
    return "Routine"


def insert_priority(queue, patient):
    levels = {"Emergency": 1, "Urgent": 2, "Routine": 3}
    p_level = levels[patient["priority_level"]]

    pos = len(queue)
    for i in range(len(queue)):
        if p_level < levels[queue[i]["priority_level"]]:
            pos = i
            break

    queue.insert(pos, patient)


# -----------------------------
# WAIT TIME CALCULATION
# -----------------------------

def calc_wait(queue, index):
    return index * AVG_TIME_PER_PATIENT


# -----------------------------
# REGISTER PATIENT
# -----------------------------

def add_patient():
    print("\n--- PATIENT REGISTRATION ---")

    name = get_name()
    age = get_age()
    reason = get_reason()
    emergency = yes_no("Emergency? (y/n): ")

    elderly = False
    if age >= 65:
        elderly = yes_no("Needs elderly assistance? (y/n): ")

    valid, errors = validate(name, age, reason, elderly)

    if not valid:
        print("\nErrors found:")
        for e in errors:
            print("-", e)
        return

    level = priority_level(emergency, age, elderly)

    # PRIORITY PATIENT
    if level != "Routine":
        patient = {
            "name": name,
            "age": age,
            "reason": reason,
            "priority_level": level
        }

        issue_priority_ticket(patient)
        insert_priority(priority_queue, patient)

        pos = priority_queue.index(patient)
        wait = calc_wait(priority_queue, pos)

        print(f"\nAdded to PRIORITY queue | Ticket: {patient['ticket']}")
        print(f"Position: {pos + 1} | Estimated wait: {wait} min")

    # REGULAR PATIENT
    else:
        patient = {
            "name": name,
            "age": age,
            "reason": reason
        }

        issue_regular_ticket(patient)
        regular_queue.append(patient)

        pos = len(regular_queue) - 1
        wait = calc_wait(regular_queue, pos)

        print(f"\nAdded to REGULAR queue | Ticket: {patient['ticket']}")
        print(f"Position: {pos + 1} | Estimated wait: {wait} min")


# -----------------------------
# DISPLAY QUEUES
# -----------------------------

def display():
    print("\n==============================")
    print("PRIORITY QUEUE")
    print("==============================")

    if not priority_queue:
        print("Empty")
    else:
        for i, p in enumerate(priority_queue):
            print(f"{p['ticket']} | {p['name']} | {p['priority_level']} | Wait: {calc_wait(priority_queue,i)} min")

    print("\n==============================")
    print("REGULAR QUEUE")
    print("==============================")

    if not regular_queue:
        print("Empty")
    else:
        for i, p in enumerate(regular_queue):
            print(f"{p['ticket']} | {p['name']} | Wait: {calc_wait(regular_queue,i)} min")


# -----------------------------
# CALL PATIENT SYSTEM
# -----------------------------

def call_patient():
    if priority_queue:
        p = priority_queue.pop(0)
        print(f"\nNOW SERVING (PRIORITY): {p['ticket']} | {p['name']}")

        if priority_queue:
            print(f"NEXT: {priority_queue[0]['ticket']} | {priority_queue[0]['name']}")

    elif regular_queue:
        p = regular_queue.pop(0)
        print(f"\nNOW SERVING (REGULAR): {p['ticket']} | {p['name']}")

        if regular_queue:
            print(f"NEXT: {regular_queue[0]['ticket']} | {regular_queue[0]['name']}")

    else:
        print("\nNo patients waiting.")


# -----------------------------
# WELCOME SCREEN
# -----------------------------

def welcome():
    print("\n" + "=" * 60)
    print("   CLINIC PATIENT QUEUE MANAGEMENT SYSTEM ")
    print("=" * 60)
  


# -----------------------------
# MENU SYSTEM
# -----------------------------
 
def menu():
    while True:
        print("\n---MAIN MENU---")
        print("\n1. Register Patient")
        print("2. Display Queues")
        print("3. Call Next Patient")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            display()
        elif choice == "3":
            call_patient()
        elif choice == "0":
            print("\nSystem shutting down. Goodbye.")
            break
        else:
            print("Invalid option.")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():
    welcome()
    menu()


if __name__ == "__main__":
    main()
