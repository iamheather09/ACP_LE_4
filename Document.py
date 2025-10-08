
import os

# Step 0: Setup
doc_path = os.path.expanduser("~/Documents")

while True:
    # Step 1: Main Menu
    print("====== Student Records Menu ======")
    print("1. Register Student")
    print("2. Open Student Record")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Step 2: Register Student
        student_no = input("Enter Student No.: ")
        last_name = input("Enter Last Name: ")
        first_name = input("Enter First Name: ")
        middle_initial = input("Enter Middle Initial: ")
        program = input("Enter Program: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        birthday = input("Enter Birthday (YYYY-MM-DD): ")
        contact_no = input("Enter Contact No.: ")

        data = [
            f"Student No.: {student_no}",
            f"Full Name: {last_name}, {first_name} {middle_initial}.",
            f"Program: {program}",
            f"Age: {age}",
            f"Gender: {gender}",
            f"Birthday: {birthday}",
            f"Contact No.: {contact_no}"
        ]

        file_name = student_no + ".txt"
        file_path = os.path.join(doc_path, file_name)

        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")

        print(f"\nStudent {student_no} registered successfully!\n")

    elif choice == "2":
        # Step 3: Open Student Record
        student_no = input("Enter Student No. to open: ")
        file_name = student_no + ".txt"
        file_path = os.path.join(doc_path, file_name)

        try:
            with open(file_path, "r") as f:
                print("\n--- Student Record ---")
                for line in f:
                    print(line.strip())
                print("-----------------------\n")
        except FileNotFoundError:
            print("\nStudent record not found.\n")

    elif choice == "3":
        # Step 4: Exit
        print("\nGoodbye! Exiting program...")
        break

    else:
        print("\naInvalid choice. Please try again.\n")
