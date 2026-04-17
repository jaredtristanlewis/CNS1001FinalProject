def patient_call(queue):
    print("Queue Call ")
#displays this message if there is no patient in the queue 
    if not queue:
        print("There is no patients in the queue.")
        return
#determines the highest priority based on first in first out manner
    patient = queue.pop(0)  
#displays the patient name and  priority level
    print(
        f"The queue is now serving: {patient['name']} | "
        f"Priority Level : {patient['priority_level']}"
    )
