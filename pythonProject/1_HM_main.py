name_1 = 'Rimma' #String
i = 7 #Integer
f = 7.7 #Float
b = bytes(3) #Bytes
l = [1, 2.0, 'list', 4] #List
t = (10, 20, 30) #Tuple
s = {1, 2, 3} #Set
fr = frozenset({'R', 'i', 'm', 'a'}) #Frozen set
d = {"name": 'R'} #Dict

name_2 = 'Rimma' #String
age = '32' #String
summ = name_2 + age

print("Вывести в консоль все выше перечисленные переменные с добавлением типа данных:")
print(name_1 , type(name_1))
print(i , type(i))
print(f , type(f))
print(b , type(b))
print(l , type(l))
print(t , type(t))
print(s , type(s))
print(fr , type(fr))
print(d , type(d))
print()

print("Вывести в консоль (2 переменные String, создать переменную в которой сканкатенируете эти переменные):")
print (summ)
print()

print("Вывести в одну строку переменные типа String и Integer используя “,” (Запятую):")
print(name_1, i, name_2, age)
print()

print("Вывести в одну строку переменные типа String и Integer используя “+” (Плюс):")
print(str(name_1) + str(i) + str(name_2) + str(age))
