import sqlite3

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY, 
        first_name TEXT, 
        last_name TEXT, 
        age INTEGER
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        breed TEXT, 
        age INTEGER, 
        dead INTEGER
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER, 
        pet_id INTEGER
    );
    ''')

def insert_data(cursor):
    # Insert data into the person table
    person_data = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]
    cursor.executemany('INSERT INTO person VALUES (?,?,?,?)', person_data)
    
    # Insert data into the pet table
    pet_data = [
        (1, 'Rusty', 'Dalmatian', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    cursor.executemany('INSERT INTO pet VALUES (?,?,?,?,?)', pet_data)
    
    # Insert data into the person_pet table
    person_pet_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]
    cursor.executemany('INSERT INTO person_pet VALUES (?,?)', person_pet_data)

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    create_tables(cursor)
    
    # Insert the data
    try:
        insert_data(cursor)
        conn.commit()  # Commit the changes to the database
        print("Data loaded successfully.")
    except sqlite3.IntegrityError:
        print("Data already exists in the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
