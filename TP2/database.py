import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("pokemon.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY,
                name TEXT,
                height INTEGER,
                weight INTEGER,
                base_experience INTEGER,
                types TEXT,
                bmi REAL
            );
            """
            self.connection.execute(query)
            self.connection.commit()
        except Exception as e:
            print(f"Error creating database table: {e}")
            
            
    def save_pokemon(self, formatted_data):
        try:
            query = """
            INSERT INTO pokemon (id, name, height, weight, base_experience, types, bmi)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """
            self.connection.execute(query, (
                formatted_data["id"],
                formatted_data["name"],
                formatted_data["height"],
                formatted_data["weight"],
                formatted_data["base_experience"],
                formatted_data["types"],
                formatted_data["bmi"]
            ))
            self.connection.commit()
            return 0  
        except Exception as e:
            print(f"Error : {e}")
            return -1            