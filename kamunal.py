import Classes_inherten
import user_page


def kamunal(phone_number1, card_number1):
    user = input("""
      Kamunal to'lovlarni amalga oshirish>>>
            1.Gaz
            2.Suz
            3.Elektir_energetika
            0.Black
          >>>""")
    if user == "1":
        return Classes_inherten.Users.gaz(phone_number1, card_number1)

    elif user == "2":
        return Classes_inherten.Users.suv(phone_number1, card_number1)

    elif user == "3":
        return Classes_inherten.Users.elektir(phone_number1, card_number1)

    elif user == "0":
        return user_page.user_page()

    else:
        print("Bunday xizmat turi mavjud emas")
        return kamunal()