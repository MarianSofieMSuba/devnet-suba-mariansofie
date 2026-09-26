"""
Midterm Practical Exam — Network Device Inventory Tool
Student: Marian Sofie M. Suba
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():

    input("=== Network Device Inventory === \n1. Add a device\n2. View all devices\n3. Count active vs inactive devices\n4. Find a device by name\n5. Remove Device\n6. Exit\nChoose an option: ")
    # print the menu, return the user's choice
    
    if input == 1:
        add_device()

    elif input == 2:
        view_devices()

    elif input == 3:
        count_active_inactive()

    elif input == 4:
        find_device()

    elif input == 5:
        remove_device()

    elif input == 6:
        


def add_device(device_list):
     # ask for name, IP, status — build the string, add to the list
     
    devices.append(input("-----------------\n=== Add a Device ===\nName of the Device:"))
    devices.append(input("The IP Address: "))
    devices.append(input("Status: "))
    print("Devices successfully added!")

    return

def view_devices(device_list):
    # loop through and print every device — handle empty list

    for view in devices:
        print(view)

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both

    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"

    input("The name of the device: ")

    if input == devices:
        print(devices)

# BONUS (optional)
def remove_device(device_list):
    # your code here

    devices.remove()

    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()