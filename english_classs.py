

import json
import user_page
import random
import datetime

from datetime import datetime


class Users():
    def __init__(self, card_number: str, birth_date: str):
        self.birth_date = birth_date
        self.create_time = f"{datetime.date()}"
        self.__card_number = card_number

    def __str__(self) -> str:
        return f"{super().__str__()} {self.birth_date} {self.create_time}"

    @staticmethod
    def gaz(phone_number1, card_number1):
        print("Gaz uchun to'lov qilish:")
        gaz = input("Gaz uchun to'lov raqamini kiriting>>>")
        if len(gaz) == 10:
            with open("kamunal.json", encoding="utf-8") as file:
                data = json.load(file)
            datax = data['kamunal']
            son = datax[0]
            if son["gaz_number"] == int(gaz):
                my = son
                with open("datas.json", encoding="utf-8") as f:
                    data1 = json.load(f)
                    miqdors = data1['users']
                    for users in miqdors:
                        if users["phone_number"] == phone_number1:
                            new_users = users
                            miqdor = int(input("Gaz uchun to'lov miqdorin kiriting>>>"))
                            if miqdor <= users["balanc"]:
                                balance = users["balanc"] - miqdor
                                balance2 = my["balanc"] + miqdor
                                new_users["balanc"] = balance
                                my['balanc'] = balance2
                                miqdors.remove(users)
                                miqdors.append(new_users)
                                datax.remove(son)
                                datax.append(my)
                                data['kamunal'] = datax
                                data1['users'] = miqdors
                                with open("kamunal.json", "w") as fales:
                                    json.dump(data, fales, indent=6)
                                with open("datas.json", "w") as fales:
                                    json.dump(data1, fales, indent=6)
                                print('muvofaqqiyatli tolov')
                                print(f"sizning hisobingizdagi qoldiq >>>{balance}")
                                return user_page.user_page(phone_number1, card_number1)
                            else:
                                print("kartada mablag' yetarli emas")
                                return Users.gaz(phone_number1, card_number1)
            else:
                print('Bundan malumot topilmadi')
                return Users.gaz(phone_number1, card_number1)
        else:
            print("xatolik yuzberdi qayta urinib ko'ring")
            return Users.gaz(phone_number1, card_number1)

    @staticmethod
    def suv(phone_number1, card_number1):
        print("Suv uchun to'lov qilish:")
        suv = input("Suv uchun to'lov raqamini kiriting>>>")
        if len(suv) == 10:
            with open("water_payment.json", encoding="utf-8") as file:
                data = json.load(file)
            datax = data['kamunal']
            son = datax[0]
            if son["suv_number"] == int(suv):
                my = son
                with open("datas.json", encoding="utf-8") as f:
                    data1 = json.load(f)
                    miqdors = data1['users']
                    for users in miqdors:
                        if users["phone_number"] == phone_number1:
                            new_users = users
                            miqdor = int(input("Suv uchun to'lov miqdorin kiriting>>>"))
                            if miqdor <= users["balanc"]:
                                balance = users["balanc"] - miqdor
                                balance2 = my["balanc"] + miqdor
                                new_users["balanc"] = balance
                                my['balanc'] = balance2
                                miqdors.remove(users)
                                miqdors.append(new_users)
                                datax.remove(son)
                                datax.append(my)
                                data['kamunal'] = datax
                                data1['users'] = miqdors
                                with open("water_payment.json", "w") as fales:
                                    json.dump(data, fales, indent=6)
                                with open("datas.json", "w") as fales:
                                    json.dump(data1, fales, indent=6)
                                print('muvofaqqiyatli tolov')
                                print(f"sizning hisobingizdagi qoldiq >>>{balance}")
                                return user_page.user_page(phone_number1, card_number1)
                            else:
                                print("kartada mablag' yetarli emas")
                                return Users.gaz(phone_number1, card_number1)
            else:
                print('Bundan malumot topilmadi')
                return Users.gaz(phone_number1, card_number1)
        else:
            print("xatolik yuzberdi qayta urinib ko'ring")
            return Users.gaz(phone_number1, card_number1)

    @staticmethod
    def elektir(phone_number1, card_number1):
        print("Elektir uchun to'lov qilish:")
        elektir = input("Elektir uchun to'lov raqamini kiriting>>>")
        if len(elektir) == 10:
            with open("power_payment.json", encoding="utf-8") as file:
                data = json.load(file)
            datax = data['kamunal']
            son = datax[0]
            if son["elektr_energetika_number"] == int(elektir):
                my = son
                with open("datas.json", encoding="utf-8") as f:
                    data1 = json.load(f)
                    miqdors = data1['users']
                    for users in miqdors:
                        if users["phone_number"] == phone_number1:
                            new_users = users
                            miqdor = int(input("Elektir uchun to'lov miqdorin kiriting>>>"))
                            if miqdor <= users["balanc"]:
                                balance = users["balanc"] - miqdor
                                balance2 = my["balanc"] + miqdor
                                new_users["balanc"] = balance
                                my['balanc'] = balance2
                                miqdors.remove(users)
                                miqdors.append(new_users)
                                datax.remove(son)
                                datax.append(my)
                                data['kamunal'] = datax
                                data1['users'] = miqdors
                                with open("power_payment.json", "w") as fales:
                                    json.dump(data, fales, indent=6)
                                with open("datas.json", "w") as fales:
                                    json.dump(data1, fales, indent=6)
                                print('muvofaqqiyatli tolov')
                                print(f"sizning hisobingizdagi qoldiq >>>{balance}")
                                return user_page.user_page(phone_number1, card_number1)
                            else:
                                print("kartada mablag' yetarli emas")
                                return Users.gaz(phone_number1, card_number1)
            else:
                print('Bundan malumot topilmadi')
                return Users.gaz(phone_number1, card_number1)
        else:
            print("xatolik yuzberdi qayta urinib ko'ring")
            return Users.gaz(phone_number1, card_number1)

    @staticmethod
    def uzbek_service():
        phone_number1 = input("Ulangan raqamingizni kiriting: ")
        with open("datas.json", encoding="utf-8") as file:
            data = json.load(file)
            for users in data["users"]:
                if users["phone_number"] == phone_number1:
                    card_number1 = users["card_number"]
                    a = random.randint(1000, 9999)
                    print(f"Ushbu kodni hech kimga aytmang! {a}")
                    while True:
                        b = input("Kodni kiriting: ")
                        if b == str(a):
                            return user_page.user_page(phone_number1, card_number1)
                        else:
                            print("Jo'natilgan kodni kiriting")
                else:
                    continue
            print("Bunday foydalanuchi topilmadi!")
            return Users.uzbek_service()

    @staticmethod
    def uzbek_service_new():
        with open("datas.json", encoding="utf-8") as file:
            date = json.load(file)
        first_name1 = input("Ismingizni kiriting: ")
        last_name1 = input("Familiyangizni kiriting: ")
        phone_number1 = input("Raqamingizni kiriting: +998 >>> ")
        card_number1 = input("Karta raqam kiriting: ")
        bith_date = input("Tugilgan kuningizni kiriting(yil-oy-kun): ")
        new_user = {
                        "first_name": f"{first_name1}",
                        "last_name": f"{last_name1}",
                        "phone_number": f"{phone_number1}",
                        "card_number": f"{card_number1}",
                        "balanc": 0,
                        "birth_date": f"{bith_date}",
                        "create_time": f"{datetime.now()}"
                    }
        date["users"].append(new_user)
        a = random.randint(1000, 9999)
        print(f"Ushbu kodni hech kimga aytmang! {a}")
        b = input("Kodni kiriting: ")
        for users in date["users"]:
            if str(a) == str(b):
                if len(phone_number1) == 9:
                    if len(card_number1) == 16:
                        if users["phone_number"] != phone_number1:
                            with open("datas.json", "w") as f:
                                json.dump(date, f, indent=6)
                            print("Muvafaqqiyatli ro'yhatdan o'tdingiz! ")
                            return user_page.user_page(phone_number1, card_number1)
                        else:
                            print("Bunday foydalanuvchi mavjud! ")
                            return Users.uzbek_service_new()
                    else:
                        print("Karta raqam 16 xonadan iborat bo'lishi kerak! ")
                        return Users.uzbek_service_new()
                else:
                    print("Telefon raqam 9 xonalik son bo'lishi kerak! ")
                    return Users.uzbek_service_new()
            else:
                print("Jo'natilgan kodni kiriting")
                return Users.uzbek_service_new()

    @staticmethod
    def balanc(phone_number, card_number):
        with open("datas.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["card_number"] == card_number:
                    balans = user["balanc"]
                    print(f"Sizning balansingiz: {balans}")
                    return user_page.user_page(phone_number, card_number)

    @staticmethod
    def pul_otkaz(phone_number1, card_number1):
        kimga = input("Qabul qiluvchi karta raqamini kiriting: ")
        if len(kimga) == 16:
            with open("datas.json", encoding="utf-8") as file:
                data1 = json.load(file)
                data = data1["users"]
                for user in data:
                    if user["card_number"] == kimga:
                        for myuser in data:
                            if myuser["card_number"] == card_number1:
                                my = myuser
                                miqdor = int(input("o'tkazma miqdorini kriting: "))
                                if my["balanc"] >= miqdor:
                                    balance = my["balanc"] - miqdor
                                    balance2 = user["balanc"] + miqdor
                                    data_x = my
                                    data.remove(my)
                                    data_x['balanc'] = balance
                                    data.append(data_x)
                                    data1["users"] = data
                                    with open("datas.json", "w") as f:
                                        json.dump(data1, f, indent=6)
                                    data_y = user
                                    data.remove(user)
                                    data_y['balanc'] = balance2
                                    data.append(data_y)
                                    data1["users"] = data
                                    with open("datas.json", "w") as f:
                                        json.dump(data1, f, indent=6)
                                        print("O'tkazma muvofaqqiyatli yakunlandi")
                                        print(f"Sizning balansingizdagi summa>>>{balance}")
                                    return user_page.user_page(phone_number1, card_number1)
                                else:
                                    print("kartada mablag' yetarli emas qaytadan urinib ko'ring")
                                    return user_page.user_page(phone_number1, card_number1)
                        return Users.pul_otkaz(phone_number1, card_number1)
                print('bunday foydalanuvchi mavjud emas')
                ask = input(f"""
                1. orqaga
                2. qayta urunish
                >>>>> """)
                if ask == '1':
                    return user_page.user_page(phone_number1, card_number1)
                elif ask == '2':
                    return Users.pul_otkaz(phone_number1, card_number1)
                else:
                    print(" ERROR")
                    return Users.pul_otkaz(phone_number1, card_number1)

        else:
            print("karta raqamni 16 xonali son bo'lishi kerak")
            return Users.pul_otkaz(phone_number1, card_number1)




