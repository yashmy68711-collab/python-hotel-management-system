class HotelManagement:
    def __init__(self):
        self.rooms = {}

    def add_room(self):
        room_no = input("Enter Room Number: ").strip()

        if room_no in self.rooms:
            print("Room already exists!")
            return

        room_type = input("Enter Room Type: ").strip()

        try:
            price = float(input("Enter Room Price: "))
        except:
            print("Invalid price!")
            return

        self.rooms[room_no] = {
            "Type": room_type,
            "Price": price,
            "Status": "Available",
            "Customer": "-"
        }

        print("Room added successfully!")

    def view_rooms(self):
        if len(self.rooms) == 0:
            print("No rooms available.")
            return

        print("\n------ Hotel Rooms ------")

        for room_no, data in self.rooms.items():
            print(f"\nRoom Number : {room_no}")
            print(f"Room Type   : {data['Type']}")
            print(f"Price       : ₹{data['Price']}")
            print(f"Status      : {data['Status']}")
            print(f"Customer    : {data['Customer']}")

    def book_room(self):
        room_no = input("Enter Room Number: ")

        if room_no not in self.rooms:
            print("Room not found!")
            return

        if self.rooms[room_no]["Status"] == "Booked":
            print("Room is already booked!")
            return

        customer = input("Enter Customer Name: ").strip()

        self.rooms[room_no]["Status"] = "Booked"
        self.rooms[room_no]["Customer"] = customer

        print("Room booked successfully!")

    def check_out(self):
        room_no = input("Enter Room Number: ")

        if room_no not in self.rooms:
            print("Room not found!")
            return

        if self.rooms[room_no]["Status"] == "Available":
            print("Room is already available!")
            return

        self.rooms[room_no]["Status"] = "Available"
        self.rooms[room_no]["Customer"] = "-"

        print("Check-out completed successfully!")

    def search_room(self):
        room_no = input("Enter Room Number: ")

        if room_no not in self.rooms:
            print("Room not found!")
            return

        data = self.rooms[room_no]

        print("\nRoom Details")
        print(f"Room Number : {room_no}")
        print(f"Room Type   : {data['Type']}")
        print(f"Price       : ₹{data['Price']}")
        print(f"Status      : {data['Status']}")
        print(f"Customer    : {data['Customer']}")


hotel = HotelManagement()

while True:
    print("\n===== Hotel Management System =====")
    print("1. Add Room")
    print("2. View Rooms")
    print("3. Book Room")
    print("4. Check Out")
    print("5. Search Room")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hotel.add_room()

    elif choice == "2":
        hotel.view_rooms()

    elif choice == "3":
        hotel.book_room()

    elif choice == "4":
        hotel.check_out()

    elif choice == "5":
        hotel.search_room()

    elif choice == "6":
        print("Thank you for using Hotel Management System!")
        break

    else:
        print("Invalid choice!")