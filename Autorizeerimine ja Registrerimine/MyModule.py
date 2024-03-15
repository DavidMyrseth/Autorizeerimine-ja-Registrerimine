import random
import string


def kasutajad_väljund(kasutajad, paroolid, valid):
    for i in range(5):
        print(f"{kasutajad[i]}, {valid[i]}, {paroolid[i]}")

def registreerimine(kasutajad, paroolid, valid):
    nimi = input("Введите имя пользователя: ")
    if nimi not in kasutajad:
        email=input("Sisesta email: ")
        parool_valik = input("Хотите создать свой пароль (введите 'ja') или сгенерировать его автоматически (введите 'ei')? ")
        if parool_valik.lower() == "ja":
            parool = input("Введите пароль: ")
            paroolid.append(parool)
            valid.append(email)
            kasutajad.append(nimi)
            print("Пользователь зарегистрирован!")
        else:
            parool = genereeri_parool()
            paroolid.append(parool)
            valid.append(email)
            kasutajad.append(nimi)
            print("Пользователь зарегистрирован!")
            print("Новый пороль: ", parool)

def autoriseeri_kasutaja(nimi, parool, kasutajad, paroolid):
    if nimi in kasutajad:
        if paroolid[kasutajad.index(nimi)] == parool:
            return True
    return False

def muuda_parool(nimi, vana_parool, uus_parool, kasutajad, paroolid):
    if autoriseeri_kasutaja(nimi, vana_parool):
        paroolid[kasutajad.index(nimi)] = uus_parool
        return "Пароль успешно изменен."
    return "Авторизация не удалась. Проверьте ваши данные."

def unusta_parool(nimi, kasutajad, paroolid):
    if nimi in kasutajad:
        indeks = kasutajad.index(nimi)
        uus_parool = genereeri_parool()
        paroolid[indeks] = uus_parool 
        print("Сгенерирован новый пароль: " + uus_parool)
    print("Такого пользователя не существует")

def genereeri_parool(pikkus=8):
    parool = ''.join(random.choices(string.ascii_letters + string.digits, k=pikkus))
    return parool

