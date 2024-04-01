import sqlite3

def query_person(cursor, person_id):
    cursor.execute('SELECT * FROM person WHERE id=?', (person_id,))
    person = cursor.fetchone()
    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old")
        return True
    else:
        print("Person not found.")
        return False

def query_pets(cursor, person_id):
    cursor.execute('''
    SELECT pet.name, pet.breed, pet.age, pet.dead
    FROM pet
    JOIN person_pet ON pet.id = person_pet.pet_id
    WHERE person_pet.person_id=?
    ''', (person_id,))

    pets = cursor.fetchall()
    if pets:
        for pet in pets:
            status = "is alive" if pet[3] == 0 else "has passed away"
            print(f"Owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old. Status: {status}")
    else:
        print("This person has no pets registered.")

def main():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        try:
            person_id_input = input("Please enter a person's ID number (or '-1' to exit): ")
            person_id = int(person_id_input)
            if person_id == -1:
                break

            if query_person(cursor, person_id):
                query_pets(cursor, person_id)
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
    conn.close()

if __name__ == "__main__":
    main()