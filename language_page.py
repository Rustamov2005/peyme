import uzbek_service
import russia_service
import english_service


def languages():
    til = input(f"""
                Tilni tanlang:
                  1. O'zbek tili
                  2. Rus tili
                  3. Ingliz tili
                       >>> """)
    if til == "1":
        return uzbek_service.uzbek_service()
    elif til == "2":
        return russia_service.russia_service()
    elif til == "3":
        return english_service.english_service()
    else:
        print("Bunday til mavjud emas!")
        return languages()
    
