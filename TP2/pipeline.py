from pokemon_service import PokemonService
from data_cleaning import DataCleaning
from data_formatting import DataFormatting
from database import Database

class Pipeline:
    def __init__(self):
        self.db = Database()
        pass

    def process_pokemon(self, pokemon_name):
        # Étape 1 : Récupération des données
        data = PokemonService.get_pokemon_data(pokemon_name)

        if data is None:
            return f"Could not find Pokemon {pokemon_name}."
        
        # print(data)
        
        # # Étape 2 : Nettoyage
        cleaned_data = DataCleaning.clean_data(data)
        
        print(cleaned_data)
        
        # # Étape 3 : Transformation
        formatted_data = DataFormatting.format_data(cleaned_data)
        print("====================================")
        print(formatted_data)
        
        # # Étape 4 : Sauvegarde
        result = self.db.save_pokemon(formatted_data)

        if result != 0:
            return f"Pokemon {pokemon_name} already stored in DB."

        return "success"