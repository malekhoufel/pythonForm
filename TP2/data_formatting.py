class DataFormatting:
    @staticmethod
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
    