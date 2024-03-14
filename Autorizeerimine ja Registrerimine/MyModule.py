import random
import string
# Массивы для хранения пользователей и паролей"

kasutajad = ["Nikita", "Edgar", "Sasha", "Artem", "Vsevolod"]
valid = ["nikita228@tthk.ee", "edgarbaran22@tthk.ee", "sashakasha32@tthk.ee", "Artemsosa@tthk.ee", "vsevolod@tthk.ee"]
paroolid = ["Secret123", "Password987", "Security456", "User321", "Protection789"]

def kasutajad_väljund():
    for i in range(5):
        print(f"{kasutajad[i]}, {valid[i]}, {paroolid[i]}")
    
def registreeri_kasutaja(nimi, parool=None):
    if nimi in kasutajad:
        return "Имя пользователя уже занято. Пожалуйста, выберите другое."
    if parool is None:
        parool = genereeri_parool()
    kasutajad.append(nimi)
    paroolid.append(parool)
    return "Пользователь зарегистрирован. Пожалуйста, запомните свой пароль: " + parool
def autoriseeri_kasutaja(nimi, parool):
    if nimi in kasutajad:
        if paroolid[kasutajad.index(nimi)] == parool:
            return True
    return False
def muuda_parool(nimi, vana_parool, uus_parool):
    if autoriseeri_kasutaja(nimi, vana_parool):
        paroolid[kasutajad.index(nimi)] = uus_parool
        return "Пароль успешно изменен."
    return "Авторизация не удалась. Проверьте ваши данные."
def unusta_parool(nimi):
    if nimi in kasutajad:
        indeks = kasutajad.index(nimi)
        uus_parool = genereeri_parool()
        paroolid[indeks] = uus_parool
        return "Сгенерирован новый пароль: " + uus_parool
    return "Такого пользователя не существует"
def genereeri_parool(pikkus=8):
    parool = ''.join(random.choices(string.ascii_letters + string.digits, k=pikkus))
    return parool


