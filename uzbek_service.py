import language_page
import Classes_inherten


def uzbek_service():
    temp = input(f"""
            Paymedan oldin foydalanganmisiz:
                 1. Ha
                 2. Yo'q
                 0. Orqaga
                    >>> """)
    if temp == "1":
        return Classes_inherten.Users.uzbek_service()
    elif temp == "2":
        return Classes_inherten.Users.uzbek_service_new()
    elif temp == "0":
        return language_page.languages()
    else:
        print("Bunday Xizmat mavjud emas")
        return uzbek_service()