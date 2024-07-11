# Charles Perdue
# Program 9
# COP 2500
# 10/27/23

# Initialize
def initialize():

    # Lists 
    a_list = []
    b_list = []
    qualifiers_list = []

    # Variables
    races = 3
    racer_a = 0
    racer_b = 0
    qualifiers = 0

    # Race a times input
    print("Enter times for Racer A:")
    for i in range(1,races+1):
        racer_a = float(input(f"Race #{i}: "))
        a_list.append(racer_a)

    # Race b times input
    print("")
    print("Enter times for Racer B:")
    for i in range(1,races+1):
        racer_b = float(input(f"Race #{i}: "))
        b_list.append(racer_b)

    # Qualify times input
    print("")
    print("Enter times for qualifiers:")
    for i in range(1,races+1):
        qualifiers = float(input(f"Race #{i}: "))
        qualifiers_list.append(qualifiers)

    # Return list inputs to main
    return [a_list, b_list, qualifiers_list]

# 1 Add a time function
def Add_a_time(a_list, b_list):

    # Input for choosing racer
    racer = input("Which racer is adding a time?\n")

    # Input for time being added 
    if racer == "A":
        time = input("What is the time to be added?\n")
        a_list.append(float(time))
    elif racer == "B":
        time = input("What is the time to be added?\n")
        b_list.append(float(time))
    else:
        print("Could not interpret racer. Please use A or B.")

# 2 Delete a time function
def Delete_a_time(a_list, b_list):

    # Input for which racer is is deleting a time
    racer = input("Which racer is deleting a time?\n")
    delete = "0"

    # Racer A
    if racer == "A":
        delete = input("Delete a time or delete a race?\n")
        #delete race
        if delete == "race":
            race_numA = int(input("Which race should be deleted?\n"))
            del a_list[race_numA-1]    
        elif delete == "time":
            time_A = input("What is the time to be deleted?\n")
            a_list.remove(float(time_A))
        else: print("Could not interpret deletion. Please use time or race.")
        return
    
    # Racer B
    if racer == "B":
        delete = input("Delete a time or delete a race?\n")
        # Delete race
        if delete == "race":
            race_numB = int(input("Which race should be deleted?\n"))
            del b_list[race_numB-1]    
        elif delete == "time":
            time_B = input("What is the time to be deleted?\n")
            b_list.remove(float(time_B))
        else: print("Could not interpret deletion. Please use time or race.")
        return

    else:
        print("Could not interpret racer. Please use A or B.")

# 3 Compare times function
def Compare_Times(a_list, b_list):

    # Variable for length of list
    a_count = len(a_list)
    b_count = len(b_list)

    # elif's for comparing times
    if a_count == 0 or b_count == 0:
        print("At least one racer has no times!")

    elif a_count < b_count:
        print("Racer A has data for", a_count, "races")
        print("Racer B has data for", b_count, "races")
        print("We will compare the first", a_count,"races.")

    elif b_count < a_count:
        print("Racer A has data for", a_count, "races")
        print("Racer B has data for", b_count, "races")
        print("We will compare the first", b_count,"races.")
        
    elif b_count == a_count:
        print("We will compare the first", b_count,"races.")

    elif b_count >= 3 or a_count >= 3:
        print("We will compare the first", b_count,"races.")

    # Variable for which list is shorter
    common_races = min(a_count, b_count)

    # For loop to show who won race
    for i in range(common_races):
        if a_list[i] < b_list[i]:
            print("Racer A has won race #", i + 1,"!", sep="")
        elif a_list[i] > b_list[i]:
            print("Racer B has won race #", i + 1,"!", sep="")
        elif a_list[i] == b_list[i]:
           print("The racers tie race #" , i + 1, "." , sep="")

# 4 Check qualifiers function
def Check_qualifiers(qualifiers, a_list, b_list): 

    # For loop to check qualifying times
    for i in range (len(qualifiers)):
        print("Qualifier #" , i + 1, ":",sep="")

        if a_list[i] <= qualifiers[i]:
            print("Racer A Qualifies!")
        if b_list[i] <= qualifiers[i]:
            print("Racer B Qualifies!")
        elif a_list[i] > qualifiers[i] and b_list[i] > qualifiers[i]:
            print("Neither racer qualified.")

# 5 Exit function
def quit():
    exit()


# Menu function 
def menu():
    print("")
    print("What would you like to do?")
    print("1 - Add a time")
    print("2 - Delete a time")
    print("3 - Compare times")
    print("4 - Check qualifiers")
    print("5 - Quit")
    return int(input(""))
    
# Main function with lists and menu calls
def main():
    lists = initialize()
    
    a_list = lists[0]
    b_list = lists[1]
    qualifiers = lists[2]
        
    M = menu()

    # While loop menu calls
    while M != 5:
        if M == 1:
            Add_a_time(a_list, b_list)
        elif M == 2:
            Delete_a_time(a_list, b_list)
        elif M == 3:
            Compare_Times(a_list, b_list)
        elif M == 4:
            Check_qualifiers(qualifiers, a_list, b_list)
        M = menu()
# Call main function 
main()
