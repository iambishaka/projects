
# create a python list
# what comese in your mind ?
# ???
# some data inside [ ] brackets separated by commas
# stored in a variable

guests = [
        "bishu",
        "reeya",
        "sibu",
        "reshma",
        "birendra",
        "gajodhar",
        "kali"
        ]

for guest in guests:
    # print(f"Hello, {guest.capitalize()}")

    if guest == "sibu":
        continue

    if guest == "gajodhar":
        print(f"{guest} is not my friend")
        break

    print(f"{guest.capitalize()}, you are welcome to my B'day party")


