#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Объявляем функцию  c 4мя переменными
def step(n, L,z,o):
        if n == 0:
            a = []
            #Запись 1 слагаемого
            a.append(int(L[1]))
            #Запись остальных слагаемых 
            for i in L[2:]: 
                a.append(int(format(i)))
                #Проверяем слагаемые на соответствие ввода, выводим слагаемые
                if len(a) == z and sum(a) == o:
                    print a
        else:
            p = 0
            if n >= L[len(L)-1]:
                #Поиск варианта разложения. Цикл работает до тех пор, пока сумма не станет равна 'n'
                for i in range(max(1, L[len(L)-1]), n + 1):
                    #Делаем следующий шаг 
                    step(n - i, L + [i],z,o) 
#Вводим слагаемое n 
n = input('Введите число n: ')
if n > 150: 
    print u'Ошибка! Должна быть n < 150'
 #Вводим слагаемое k 
z = input('Введите число k: ') 
if z > 150: 
    print u'Ошибка! Должна быть k < 150'
o = n
print ' '
print step(n,[0],z,o)
print ' '

