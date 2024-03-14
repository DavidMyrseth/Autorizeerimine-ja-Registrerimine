import MyModule
    
MyModule.kasutajad_väljund()

while True:
    print("Valikud")
    print("1.Registreerimine")
    print("2.Autoriseerimine")
    print("3.Parooli muutmine")
    print("4.Unustasin parooli")
    print("5.Lõpeta")
    valik = input("Vali tegevus (1-5): ")
    if valik == "1":  # Регистрация
        nimi = input("Введите имя пользователя: ")
        parool_valik = input("Хотите создать свой пароль (введите 'ja') или сгенерировать его автоматически (введите 'ei')? ")
        if parool_valik.lower() == "да":
            parool = input("Введите пароль: ")
        else:
            parool = None
        print(MyModule.registreeri_kasutaja(nimi, parool))
    elif valik == "2":  # Авторизация
        nimi = input("Введите имя пользователя: ")
        parool = input("Введите пароль: ")
        if MyModule.autoriseeri_kasutaja(nimi, parool):
            print("Авторизация успешна!")
        else:
            print("Авторизация не удалась. Проверьте ваши данные.")
    elif valik == "3":  # Изменить пароль
        nimi = input("Введите имя пользователя: ")
        vana_parool = input("Введите старый пароль: ")
        uus_parool = input("Введите новый пароль: ")
        print(MyModule.muuda_parool(nimi, vana_parool, uus_parool))
    elif valik == "4":  # Забыли пароль
        nimi = input("Введите имя пользователя: ")
        print(MyModule.unusta_parool(nimi))
    elif valik == "5":  # Выход
        print("Программа завершает работу.")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")
    

