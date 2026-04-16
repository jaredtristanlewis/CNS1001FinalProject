def validation_patient (name, age, reason, is_emergency, needs_elderly_help):
    errors = []

    if name.strip() == "":
      errors.append("Name cannot be empty")

    if not isinstance(age, int) or age <=0:
          errors.append("Age must be positive number")

    if reason.strip() == "":
        errors.append("reason cannot be empty")

    if needs_elderly_help and age < 60:
        errors.append("Elderly assistance selected but age is below 60")

    if is_emergency:
        queue = "Emergency Queue"
    elif age >= 60 or needs_elderly_help:
        queue = "Priority Queue"
    else:
        queue = "Normal Queue"

    if errors:
        return False, errors
    else:
        return True, queue
