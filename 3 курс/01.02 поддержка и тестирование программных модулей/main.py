test_list = ['20.11.2000', '20.1.202000', '2010200000','198.20.235','а1.10.2к15','32.12.1999','31.13.2000']

for count, test in enumerate(test_list):
    dug_report = ''

    if len(test) == 10:
        print('есть 10 символов')
        a = test.split('.')
        if len(a) == 3:
            day,month,years = a
            print('точки на месте')
            if len(day)==2 and len(month)==2 and len(years)==4:
                print("правильное количество символов")
                if day.isdigit() and month.isdigit() and years.isdigit():
                    print('нету букв')
                    if int(day) <= 31:
                        print("правильный день")
                        if int(month) <= 12:
                            print("правильный месяц")
                        else:
                            dug_report = "неправильный месяц"
                    else:
                        dug_report = "неправильный день"
                else:
                    dug_report = "есть буквы"
            else:
                dug_report = "неправильный количество символов в месяце,дне,годе"
        else:
            dug_report = "неправильный точки"
    else:
        dug_report = "неправильный количество символов"

    with open('dug_report.txt', 'a', encoding='utf-8') as file: 
        file.write(str(count) + ' ' + test + ' ' + dug_report + ' ' + 'средний приоритет' + ' ' + 'среднее влияние' +  '\n') 