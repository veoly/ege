f=open('nomer3.txt')
a=f.readline()  #открываю файл A и считываю данные
a=a.split(' ') #"разбиваю" строку по пробелу,чтобы далее проверить наличие
               #каждого символа из алфавита А в файле В

f=open('nomer4.txt')
s=f.readline()    #открываю файл В и считываю данные

c=0    #счетчик длины подцепочки
m=0    #максмальная длина из всех подцепочек

for i in range(len(s)):   #прохожу по всей цепочке
    if s[i] in a:     #проверяем подряд каждый символ, если символ есть в
                      #алфавите, увеличиваем с на 1
        c=c+1
        m=max(c, m)   #запоминаем длину максимальной подцепочки
    else:
        c=0           #если цепочка прервалась, т.е. мы встретили символ,
                      #которого нет в алфавите, обнуляем с (мы нашли длину
                      #одной из подцепочек)
print(m)       #в ответ выводим длину максимальной подцепочки 







    






    
