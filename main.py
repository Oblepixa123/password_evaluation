#импортирование бибилотек




#основная часть

def get_lenght(password):#создание функции get_lenght
  if len(password) > 12:#если длина пароля больше 12 символов    
    return True#возращается значение тру

def get_number(password):#обьявление функции get_number
  return any(symbol.isdigit() for symbol in password)#цикл фор по паролю проверяющий есть ли в пароле цифра
     
def get_letter(password):#создание функции get_letter
  return any(symbol.isalpha() for symbol in password)#цикл фор по паролю проверяющий есть ли в пароле буква

def get_capital(password):#обьявление функции get_capital
  return any(symbol.isupper() for symbol in password)#цикл фор по паролю проверяющий есть ли в пароле буква с Верхним регистром
    
def get_symbol(password):#обьявление функции get_symbol
  return any(symbol.isalpha and symbol.isdigit() for symbol in password)#цикл фор по паролю проверяющий есть ли в пароле символы
    
def main():#создание функции main
    score = 0#переменная с балами рейтинга 
    password = input("Ввдеите пароль: ")#инпут с запросом пароля
    
    functions = [#список с вызовом функций
        get_lenght(password),#вызов функции get_lenght
        get_number(password),#вызов функции get_number
        get_letter(password),#вызов функции get_letter
        get_capital(password),#вызов функции get_capital
        get_symbol(password),#вызов функции get_symbol
      ]

    for function in functions:#выбираем функцию в последовательности functions
        if function :#проверяем равна ли выбраная функция тру
            score += 2#+2 к переменной с баллами рейтинга

    print("рейтинг пароля:", score,)#принт с рейтингом пароля

if __name__ == "__main__":#мейн будет работать при условии что запуск равен главному файлу
    main()#вызов функции 
