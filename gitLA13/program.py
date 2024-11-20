print("A - Add Record")
print("B - View Records")
print("C - Clear All Records")
print("D - Exit")

choice = ""

while choice.upper() != 'D':
    choice = input("ENTER SELECTION [A, B, C, or D]: ")
    if choice.upper() == 'A':
        print("Add Record")
        addRec()
    elif choice.upper() == 'B':
        print("View Records")
        viewRec()
    elif choice.upper() == 'C':
        print("Clear All Records")
        clearRec()
    elif choice.upper() == 'D':
        print("Thank you!")

def addRec():
    file = open(filename, 'r')
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    addr = input("Enter Address: ")
    with open(filename, 'a') as file:
        file.write(name + ", " + email + ", " + addr + "\n")
    file.close()

def viewRec():
    filename = "records.txt"
    with open(filename, 'r') as file:
        print(file.read())
    file.close()

def clearRec():
    file = open(filename, 'w')
    file.write("")
    file.close()

try:
    filename = 'file1.txt'
    file = open(filename, "x")
    print(filename + " successfully created.")
except:
    print(filename + " already exists.")
