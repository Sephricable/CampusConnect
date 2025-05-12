'''
Groupmate Data Structure and Algorithm

1. Sephric Rigor Delos Santos (Leader)
2. Cheska Cuya
3. Althea Carandang
'''

students = {}
events = ["Databiz", "BIT Conference", "ROTC Month", "National Women Month"]

# Add Account Student Info
def register():
    student_id = input("Enter student ID: ")
    name = input("Enter your name: ")
    students[student_id] = {"name": name, "messages": []}
    print(f"Registered successfully! Welcome, {name}.\n")

# Campus Events
def show_events():
    print("\nCampus Events:")
    for e in events:
        print("- " + e)
    print()

# Sending Message
def send_message():
    student_id = input("Enter your student ID: ")
    if student_id in students:
        sender = students[student_id]["name"]
        msg = input("Type your message: ")
        for s in students:
            # Also include sender so they can see their sent message
            students[s]["messages"].append((sender, msg))
        print("Message sent!\n")
    else:
        print("Student not found. Please register first.\n")

# Read Messages
def read_messages():
    student_id = input("Enter your student ID: ")
    if student_id in students:
        print("\nYour Messages:")
        for sender, msg in students[student_id]["messages"]:
            print(f"{sender}: {msg}")
        print()
    else:
        print("Student not found.\n")

# Menu
def menu():
    while True:
        print("=== Campus Connect ===")
        print("1. Register")
        print("2. Show Events")
        print("3. Send Message")
        print("4. Read Messages")
        print("5. Exit")
        print("======================")

        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            show_events()
        elif choice == '3':
            send_message()
        elif choice == '4':
            read_messages()
        elif choice == '5':
            print("Thanks for using Campus Connect!")
            break
        else:
            print("Invalid option. Try again.\n")

menu()
      
