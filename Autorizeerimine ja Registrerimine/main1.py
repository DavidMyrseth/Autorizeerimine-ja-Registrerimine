from MyModule import *
kasutajad = ["Nikita", "Edgar", "Sasha", "Artem", "Vsevolod"]
valid = ["nikita228@tthk.ee", "edgarbaran22@tthk.ee", "sashakasha32@tthk.ee", "Artemsosa@tthk.ee", "vsevolod@tthk.ee"]
paroolid = ["Secret123", "Password987", "Security456", "User321", "Protection789"]
while True:
    print("Valikud")
    print("1.Registreerimine")
    print("2.Autoriseerimine")
    print("3.Parooli muutmine")
    print("4.Unustasin parooli")
    print("5.Vaata lisatud kasutajaid")
    print("6.Lõpeta")
    valik = input("Vali tegevus (1-6): ")
    if valik == "1":  # Регистрация
        registreerimine(kasutajad, paroolid, valid)
    elif valik == "2":  # Авторизация
        nimi = input("Введите имя пользователя: ")
        parool = input("Введите пароль: ")
        if autoriseeri_kasutaja(nimi, parool, kasutajad, paroolid):
            print("Авторизация успешна!")
        else:
            print("Авторизация не удалась. Проверьте ваши данные.")
    elif valik == "3":  # Изменить пароль
        nimi = input("Введите имя пользователя: ")
        vana_parool = input("Введите старый пароль: ")
        uus_parool = input("Введите новый пароль: ")
        print(muuda_parool(nimi, vana_parool, uus_parool))
    elif valik == "4":  # Забыли пароль
        nimi = input("Введите имя пользователя: ")
        print(unusta_parool(nimi))
    elif valik == "5":  # Просмотр добавленных пользователей
        kasutajad_väljund(kasutajad, paroolid, valid)
    elif valik == "6":  # Выход
        print("Программа завершает работу.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")