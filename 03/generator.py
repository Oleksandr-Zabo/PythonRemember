def doctor_reception(petient_queue):
    print("Doctors Reception")
    for patient in petient_queue:
        print(f"{patient} is waiting.")
        yield f"{patient} is being seen by doctor."

        print(f"The {patient} has been treated")


waiting_room = ['John', 'James', 'Jonathan', 'Jacob', 'Joseph']

reception = doctor_reception(waiting_room)

current_patient = next(reception)

print(current_patient)
next_patient = next(reception, "All patients have been seen")
print(next_patient)

