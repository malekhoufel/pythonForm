import requests
import sqlite3
from contextlib import contextmanager


@contextmanager
def db_connection(database="pokemon.db"):
    connection = sqlite3.connect(database)
    try:
        yield connection
    finally:
        connection.close()
        
API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
def get_pokemon_data(pokemon_name):
        response = requests.get(f"{API_BASE_URL}{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()  # Retourne les données JSON
        else:
            print(f"Pokemon {pokemon_name} not found.")
            return None   
        
def clean_data(data):
        info_importantes= {
                "id": data.get("id"),
                "name": data.get("name"),
                "height": data.get("height"),
                "weight": data.get("weight"),
                "base_experience": data.get("base_experience"),
                "types": data.get("types")
            }
        return info_importantes 

def format_data(cleaned_data): 
        height = cleaned_data.get("height")
        weight = cleaned_data.get("weight")
        
        types = cleaned_data.get("types")
        print ("+"*40)
        print (types)
        
        typesNames=""
        for type in types:
            typesNames+=(type["type"]["name"]+",")
        typesNames=typesNames.rstrip(",")    
        print(typesNames)
        
        bmi = weight / (height ** 2)
        cleaned_data["types"]=typesNames
        cleaned_data["bmi"] = bmi 
        return cleaned_data   
    
def save_to_database(connection, pokemon_data):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY,
                name TEXT,
                height INTEGER,
                weight INTEGER,
                base_experience INTEGER,
                types TEXT,
                bmi REAL
        )
    """)
    try:
        cursor.execute("""
            INSERT OR IGNORE INTO pokemon (id, name, height, weight, bmi)
            VALUES (?, ?, ?, ?, ?)
        """, (pokemon_data["id"], pokemon_data["name"], pokemon_data["height"], pokemon_data["weight"], pokemon_data["bmi"]))
        connection.commit()
        print("seccess")
    except sqlite3.IntegrityError as e:
        print(f"Erreur : {e}")
                  
        
if __name__ == "__main__":
    
    data = get_pokemon_data("squirtle")
    #print(data)
    print("="*40)
    data_cleaned= clean_data(data)  
    print(data_cleaned)  
    print("="*40)
    data_formatted=format_data(data_cleaned)  
    print(data_cleaned) 
    print("="*40)
    with db_connection() as connection:
        save_to_database(connection,data_formatted) 
    