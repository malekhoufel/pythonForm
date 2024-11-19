class DataCleaning:
    
    @staticmethod
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