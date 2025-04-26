import csv

csv_file = "patient_dashboard.csv"
HIGH_BP_THRESHOLD = 140

def add_new_patient(file_path):
    print("\n📝 Add a New Patient Record")
    new_id = input("Enter Patient ID: ")
    new_age = input("Enter Age: ")
    new_bp = input("Enter Blood Pressure: ")
    new_diagnosis = input("Enter Diagnosis: ")

    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([new_id, new_age, new_bp, new_diagnosis])

    print(f"✅ Patient {new_id} added successfully!\n")

def run_analysis(file_path):
    total_age = 0
    patient_count = 0
    high_bp_patients = 0
    diagnosis_counts = {}
    risky_patients = []

    print("\n📊 Patient Data Summary")
    print(f"Total Patients: {patient_count}")
    if patient_count > 0:
        average_age = total_age / patient_count
        print(f"Average Patient Age: {average_age:.1f} years")
    print(f"Patients with High Blood Pressure (> {HIGH_BP_THRESHOLD} mmHg): {high_bp_patients}")

    print("\n📋 Diagnosis Breakdown:")
    for diag, count in diagnosis_counts.items():
        print(f" - {diag}: {count} patients")

    print("\n🚨 High-Risk Patients (High BP + Dangerous Diagnosis):")
    if risky_patients:
        for patient in risky_patients:
            print(
                f"Patient {patient['PatientID']}: Age {patient['Age']}, BP {patient['BloodPressure']} mmHg, Diagnosis: {patient['Diagnosis']}")
    else:
        print("No high-risk patients identified.")

    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            patient_id = row.get('PatientID')
            age_raw = row.get('Age')
            bp_raw = row.get('BloodPressure')
            diagnosis = row.get('Diagnosis', '').strip()

            if not age_raw or not bp_raw:
                print(f"⚠️ Skipping row with missing data: {row}")
                continue

            age = int(age_raw)
            bp = int(bp_raw)

            total_age += age
            patient_count += 1

        if bp > HIGH_BP_THRESHOLD:
            high_bp_patients += 1

        if diagnosis not in diagnosis_counts:
            diagnosis_counts[diagnosis] = 1
        else:
            diagnosis_counts[diagnosis] += 1

    if bp > HIGH_BP_THRESHOLD and diagnosis.lower() in ['hypertension', 'heart disease']:
        risky_patients.append({
            'PatientID': patient_id,
            'Age': age,
            'BloodPressure': bp,
            'Diagnosis': diagnosis
        })

while True:
    print("\n🏥 Patient Dashboard Menu")
    print("1. Add a new patient")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        add_new_patient(csv_file)
    elif choice == '2':
        run_analysis(csv_file)
    elif choice == '3':
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid option. Please choose 1, 2, or 3.")

