import psycopg2
import csv
from connect import conn 

# Design table(s) for the PhoneBook
# Implement inserting data from a CSV file
# Implement inserting data entered from the console (user name, phone)
# Implement updating a contact's first name or phone number
# Implement querying contacts with different filters (e.g. by name, by phone prefix)
# Implement deleting a contact by username or phone number


def create_table():
    command = """CREATE TABLE IF NOT EXISTS contacts(
                    id SERIAL PRIMARY key,
                    name varchar(256) NOT NULL,
                    phone varchar(256) UNIQUE NOT NULL)"""
    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()
    print("\n" *2)
    print("Table created successfully \n")

def insert_contact(name, number):
    command = "INSERT INTO contacts (name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        cur.execute(command, (number, name))
        conn.commit()

def insert_from_console():
    name = input("Input name: ")
    number = input("Input number: ")

    insert_contact(number, name)
    print(f"Added successfully: {name} - {number}")

def drop_table():
    command = "DROP TABLE contacts"

    with conn.cursor() as cur:
        cur.execute(command)
        conn.commit()

def update():
    preference = input("What do you would like to update phone or name:")
    old = input("Write the data which you would like to change :")
    new = input("Write the new data: ")
    command = f"UPDATE contacts SET {preference} = %s WHERE {preference} = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new, old))
        conn.commit()
    print(f"{old} have updated to {new} \n")

def insert_from_csv():
     with conn.cursor() as cur:
        command = "INSERT INTO contacts(name, phone) VALUES(%s, %s)"
        with open("contacts.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                name, phone = row
                cur.execute(command, (name, phone))
            conn.commit()
        print(f"Imported contacts from contacts.csv")

def get_all_contacts(choice):
    command = f"SELECT * FROM contacts ORDER BY {choice}"
    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()
    
def print_contacts(contacts):
    if not contacts:
        print("  (no contacts)")
        return
    for c in contacts:
        print(f"  [{c[0]}] {c[1]} - {c[2]}")

def delete():
    preference = input("How do you would like to delete by phone or by name:")
    old = input("Write the data which you would like to delete :")
    command = f"DELETE FROM contacts WHERE {preference} = %s"
    with conn.cursor() as cur:
        cur.execute(command, (old, ))
        conn.commit()
    print(f"{old} have been deleted from contacts \n")

while True:
    command = int(input("""Choose the option:
                        >1. Create table contacts
                        >2. Insert from console
                        >3. Insert from csv
                        >4. Update a contact's first name or phone number
                        >5. Show the table
                        >6. Delete a contact by username or phone number
Write here:"""))
    if command == 1:
        create_table()
    elif command == 2:
        insert_from_console()
    elif command == 3:
        insert_from_csv()
    elif command == 4:
        update()
    elif command == 5:
        choice = input("Choose the choise: id|name|number: ")
        print_contacts(get_all_contacts(choice))
    elif command == 6:
        delete()
    elif command == 0:
        drop_table()
        break 
    
conn.close()
print("See ya!")


