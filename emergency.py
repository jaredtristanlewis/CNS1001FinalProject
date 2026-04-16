def add_patient_by_priority(queue, patient):
     priority_levels = {
        "Emergency": 1,
        "Urgent": 2,
        "Routine": 3
    }

    # Validate age
    try:
        patient["age"] = int(patient["age"])
        if patient["age"] < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError:
        raise ValueError("Age must be a valid number.")

    # Standardize and validate priority level
    patient["priority_level"] = patient["priority_level"].capitalize()

    if patient["priority_level"] not in priority_levels:
        raise ValueError("Invalid priority level. Use Emergency, Urgent, or Routine.")

    # Find where to insert patient
    patient_priority = priority_levels[patient["priority_level"]]
    position = len(queue)

    for i in range(len(queue)):
        current_priority = priority_levels[queue[i]["priority_level"]]

        if patient_priority < current_priority:
            position = i
            break

    queue.insert(position, patient)
    return queue


if __name__ == "__main__":
    # Simple standalone test
    queue = []

    patients = [
        {"name": "Mary", "age": "25", "reason": "Check-up", "priority_level": "Routine"},
        {"name": "David", "age": "40", "reason": "Fever", "priority_level": "Urgent"},
        {"name": "Sarah", "age": "67", "reason": "Breathing problem", "priority_level": "Emergency"},
        {"name": "Kevin", "age": "31", "reason": "Cough", "priority_level": "Routine"}
    ]

    try:
        for patient in patients:
            queue = add_patient_by_priority(queue, patient)

        print("Current Queue:")
        for i in range(len(queue)):
            print(
                str(i + 1) + ". "
                + queue[i]["name"]
                + " | Age: " + str(queue[i]["age"])
                + " | Reason: " + queue[i]["reason"]
                + " | Priority: " + queue[i]["priority_level"]
            )

    except ValueError as e:
        print("Error:", e)
