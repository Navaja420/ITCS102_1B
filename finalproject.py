

def main_menu():

    while True:
        print("\\n===== PYTHON LEARNING PROGRAM =====")
        print("1 - Python Printing")
        print("2 - Python Variables")
        print("3 - Conditional Statements")
        print("4 - Looping Statements")
        print("5 - Functions")
        print("6 - Arrays (Lists)")
        print("7 - Dictionaries")
        print("0 - Exit")

        choice = input("Select a lesson: ")

        if choice == '1':
            lesson_printing()
        elif choice == '2':
            lesson_variables()
        elif choice == '3':
            lesson_conditionals()
        elif choice == '4':
            lesson_loops()
        elif choice == '5':
            lesson_functions()
        elif choice == '6':
            lesson_arrays()
        elif choice == '7':
            lesson_dictionary()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def lesson_printing():
    print("\n--- Lesson 1: Python Printing ---")
    print("Printing means displaying test or values on the screen.")
    print("Example:")
    print("print('Hello, World!') will display Hello, World! on the screen.")

    print("\nTry IT YOURSELF:")
    user_text = input("Enter text to print:")
    print("You entered:", user_text)
    input("Press Enter to return to the main menu...")


def lesson_variables():
    print("\n--- Lesson 2: Python Variables ---")
    print("Variables are used to store data values")
    print("Example:")
    print("name = 'John'")
    print("age = 18")

    print("\nTry IT YOURSELF:")
    var_name = input("Enyter your name: ")
    var_age = input("Enter your age: ")

    print("Stored in variables!")
    print("Name", var_name)
    print("Age:", var_age)

    print("\nPRACTICE:")
    print("Create 2 variables: favorite_food and favorite_color.")
    input("Please Enter to return to menu...")


def lesson_conditionals():
    print("\n--- Lesson 3: Conditional Statements ---")
    print("Conditonal statements are used to perform different actions based on different conditions.")
    print("Example:")
    print("if age >= 18:")
    print("   print('adult)")
    print("else:")
    print("   print('minor'")

    print("\nTry IT YOURSELF:")
    num = int(input("Enter a number:"))

    if num > 0:
        print("The number is POSITIVE.")
    elif num < 0:
        print("The number is NEGATIVE")
    else:
        print("The number is ZERO.")

    print("\nPRACTICE")
    print("Ask the user for their gradea and give feedback (e.g., Pass/Fail.")
    input("Press Enter to return to the main menu...")
    

    
def lesson_loops():
    print("\n--- Lesson 4: Looping Staements --")
    print("Loops are used to repeat a block of code as long as a specified condition is met.")
    print("\nWhile Loop Example:")
    print("i = 1")
    print("while i <= 5:")
    print("   print(i)")
    print("  i+= 1")

    print("\nFor Loof Example:")
    print("fir i in range(1, 6):")
    print("  print(i)")

    print("\nTry IT YOURSELF:")
    print("Printing number 1 to 5 using a loop:")
    for i in range(1, 6):
        print(i)

    print("\nPACTICE:")
    print("MAke a loop that prints your name 5 times.")
    input("Press Enter to return to menu...")


def lesson_functions():
    print("\n--- Lesson 5: Functions ---")
    print("functions are blocks of code which only run when they are called.")
    print("Example:")

    print("def greet():")
    print("  print('Hello!")
    print("greet()")

    print("\nTry IT YOURSELF:")

    def greet_user():
        print("Hello student! You called afunction!")

    greet_user()

    print("\nPRACTICE:")
    print("create a function that takes adds 2 numbers and prints the results.")
    input("Press Enter to rerturn to the main menu...")


def lesson_arrays():
    print("\n--- Lesson 6: Arrays (Lists) ---")
    print("Arrays (LIsts) are used to store multiple items in a single variable.")
    print("Example:")
    print("fruits = ['apple', 'banana', 'cherry']")

    fruits = ['apple', 'banana', 'cherry']
    print("\nHere is a sample list:", fruits)

    print("\nTry IT YOURSELF:")
    your_list = []
    item = input("Add an item to your list: ")
    your_list.append(item)
    print("Your list now contains:", your_list)

    print("\nPRACTICE:")
    print("Make alist of 3 movies and print them.")
    input("Press Enter to return to menu..")


def lesson_dictionary():
    print("\n--- Lesson 7: Dictiopnaries ---")
    print("Dictionaries are used to store data values in key:value pairs.")
    print("Example:")
    print("student = {'name' : 'John, 'age': 18}")

    student = {'name': 'John', 'age': 18}
    print("\nHere is a sample dictionary:", student)

    print("\nTry IT YOURSELF:")
    name = input("Enter sturent name: ")
    age = input("Enter student age: ")
    new_student = {'name': name, 'age': age}
    print("New student record:", new_student)

    print("\nPRACTICE")
    print("Create a dictionnary with: name, age, course,")
    input("Press Enter to return to the main menu...")

main_menu()


