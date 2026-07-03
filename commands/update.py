from db_class import DB


def update(args: list):
    print(r"""   __  __          __      __
  / / / /___  ____/ /___ _/ /____
 / / / / __ \/ __  / __ `/ __/ _ \
/ /_/ / /_/ / /_/ / /_/ / /_/  __/
\____/ .___/\__,_/\__,_/\__/\___/
    /_/                           """)
    if len(args) == 0:
        area = input(
            "What area would you like to update\n1 = Personal\n2 = Project\n3 = Experience\n4 = Education\n5 = Tech Stack\n").strip().lower()
    else:
        area = args[0]

    db = DB()
    match area:
        case "1" | "personal":
            personal_update(db)
        case "2" | "project":
            print("another TO-DO app sir")
        case "3" | "experience":
            print("10+ for entry level")
        case "4" | "education":
            print("school")
        case "5" | "tech Stack" | "techstack" | "tech":
            print("RUST ALL THE WAY")
        case _:
            print(f'Unknown Input: "{area}" Please try again')

# * Update Functions


def personal_update(db):
    personal_data = {
        "name": input("Enter name: "),
        "email": input("Enter email: "),
        "phone": input("Enter phone: "),
        "address": input("Enter address: "),
        "location": input("Enter location: ")
    }
    print("\nConfirm Details")
    for field, value in personal_data.items():
        print(f"{field}: {value}")
    confirm = input("Enter y to confirm: ")
    if confirm == "y":
        print("Writing To Database")
        db.update_personal(1, personal_data)
    else:
        print("Operation Canceled")
