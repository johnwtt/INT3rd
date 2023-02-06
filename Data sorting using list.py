#Create a list to store data
data = []

#Create a function to add data to the list
def add_data():
    student = input("Enter student's name: ")
    score = int(input("Enter student's score: "))
    data.append([student, score])

#Create a function to print out the data alphabetically
def print_data_alphabetically():
    data.sort()
    for i in data:
        print(i)

#Create a function to print out the data according to the score from highest to lowest
def print_data_score():
    data.sort(key=lambda x: x[1], reverse=True)
    for i in data:
        print(i)

#Create a function to print out a list of students that have a score under 5
def print_data_under_5():
    for i in data:
        if i[1] < 5:
            print(i)

#Create a function to print out the menu
def print_menu():
    print("1. Add data")
    print("2. Print data alphabetically")
    print("3. Print data according to the score from highest to lowest")
    print("4. Print data of students that have a score under 5")
    print("5. Exit")

#Create a function to run the program
def run():
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_data()
        elif choice == 2:
            print_data_alphabetically()
        elif choice == 3:
            print_data_score()
        elif choice == 4:
            print_data_under_5()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

#Run the program
run()