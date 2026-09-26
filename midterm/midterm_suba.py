"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Marian Sofie M. Suba
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():

    input("=== Network Device Inventory === \n1. Add a device\n2. View all devices\n3. Count active vs inactive devices\n4. Find a device by name\n5. Remove Device\n6. Exit\nChoose an option: ")
    # print the menu, return the user's choice
    
    match input:
        case 1:
            print(add_device)
        case 2:
            print(view_devices)
        case 3:
            print(count_active_inactive)
        case 4:
            print(find_device)
        case 5:
            print(remove_device)
        case 6:
            pass

def add_device(device_list):
     # ask for name, IP, status — build the string, add to the list

    devices.append(input("-----------------\n=== Add a Device ===\nName of the Device:"))
    devices.append(input("The IP Address: "))
    devices.append(input("Status: "))

    return


def view_devices(device_list):
    # loop through and print every device — handle empty list
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()