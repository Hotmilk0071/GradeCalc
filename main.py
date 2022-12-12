import time
print("Калькулятор оценок!")
time.sleep(1)
print("(Для выхода нажмите ctrl+c)")
time.sleep(0.1)
def ask():
        print("Вычислить еще? (Да или нет)")
        try:
                now = str(input())
        except KeyboardInterrupt:
                                    ask()
        except:
                ask()
        now = now.replace(" ", "")
        now = now.title()
        if now =='Да':
            time.sleep(1)
            calc()
        elif now == 'Нет':
            print('Спасибо за использование! Завершение работы через 5 секунд...')
            time.sleep(5)
            exit(0)
        else:
            print('Неккоректное значение, попробуйте еще раз!')
            time.sleep(2)
            ask()
def calc():
    try:
            ratings = list(map(int, input('Введите ваши оценки:').split()))
    except KeyboardInterrupt:
                                    print("Выход...")
                                    time.sleep(1)
                                    exit(0)
    except:
            print('Можно вводить только числа!')
            time.sleep(1)
            calc()
    ratings =  [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    count = len(ratings)
    summa = sum(ratings)
    average = summa / count
    average = round(average, 2)
    whole = round(average)
    time.sleep(1)
    print('Количество оценок:', count)
    time.sleep(1)
    print('Сумма оценок:', summa)
    time.sleep(1)
    print('Средний балл:', average)
    time.sleep(1)
    print('В триместре выйдет:', whole)
    time.sleep(1)
    ask()
calc()

