def arithmetic(a: float,b:float,c=str):
    """Lihtne kalkulaator
    + - liitamine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Aritmeetiline tehing
    :rtype float:
   """
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c=="/":
        if b!=0:
            r=a/b
        else:
            r="div/0"
    else:
        r="tundmatu sym"       
    return r
def is_year_leap(year:int):
    """Возвращает значение true, если год слишком короткий, и значение Flase, если нет
        :param int year:esimene arv
    :rtype str
    """
    if year%4==0:
        t=True      
    else:
        t=False
    return("")
def square(kv:float):
    """Мы пишем сторону квадрата, и программа выдает нам площадь квадрата, периметр и диагональ 
     :param int kv:esimene arv
    :rtype float
    """

    return(4*kv, kv**2, (2*kv**2)**.5)
    return("")
def season(kuu:int):
    """Мы пишем от 1 до 12 месяцев, и программа устанавливает сезон по месяцам
    parem float a месяц
   :param int kuu: esimene arv
    :rtype str"""
    
    if kuu==12:
        res="Зима"
    elif 0<kuu<3:
        res="Зима"
    elif 2<kuu<6:
        res="Весна"
    elif 5<kuu<9:
        res="Лето"
    elif 8<kuu<12:
        res="Осень"
    else:
        res="Viga!"
    return res 
def bank(a:float,years:int):
    """Мы кладем деньги на баланс и ждем n лет
    """
    for _ in range(years):
        a=((1.1*1/100)*a)*100
    print("Ваш баланс:",a)
    return("")
def is_prime(a:int):
    """Мы записываем число от 0 до 1000 и возвращаем true, если оно простое, и false в противном случае.
    """
    b=2
    while a%b!=0:
        b+=1
    return b==a
def xor_cipher(string:str, key:str)->str:
    """Обычное кодирование слов
    """
    result=""
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i])
        for j in range(len(key)):
            temp^=ord(key[j])
        result+=chr(temp)
    return result
def xor_uncipher(string:str, key: str)->str:
    """кодирование декодированного текста
    """
    result = ""
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result
def date(day:int, month:int, year:int):
    set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
    else:
        return False