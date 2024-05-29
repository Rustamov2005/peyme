import Classes_inherten
import kamunal
import uzbek_service


def user_page(phone_number1, card_number1):
    xizmat = input(f"""
              Payme ilovasiga xush kelibsiz
                bizning xizmatlarimiz>>>>
                   1. Pul o'tkazish
                   2. Balansni ko'rish
                   3. Kommunal to'lovlar
                   0. Orqaga
                       >>> """)
    if xizmat == "1":
        return Classes_inherten.Users.pul_otkaz(phone_number1 ,card_number1)
    elif xizmat == "2":
        return Classes_inherten.Users.balanc(phone_number1, card_number1)
    elif xizmat == "3":
        return kamunal.kamunal(phone_number1, card_number1)
    elif xizmat == "0":
        return uzbek_service.uzbek_service()
    else:
        print("Bunday xizmat mavjud emas!")
        return user_page(phone_number1, card_number1)