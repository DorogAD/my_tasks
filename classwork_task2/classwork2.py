#2 classwork
'''
Даны две строки, написать функцию для проверки того, содержится ли вторая строка в первой,
вернуть индекс начала подстроки при положительном результате, -1 при отрицательном.
Пример: 
in ('testtesttest', 'test') -> 0
in ('test', 'ntest') -> 1
in ('test', 'ntnest') -> -1
'''
def exist(str1, str2):#первый аргумент - исходная строка, второй аргумент - искомая строка
    l1 = len(str1)#находим длину исходной строки
    l2 = len(str2)#находим длину искомой строки
    end = l1 - l2#находим где завершать перебор
    for i in range(0, end + 1):#перебираем значения
        sliced = str1[i:i + l2]#делаем срез равный по длине искомой строке
        if i == end and sliced != str2:#если мы достигли конца списка и не нашли искомое значение
            return '-1'#возвращаем минус один
        elif sliced != str2:#если текущий срез не равен искомому значению
            i += 1#новая итерация    
        elif sliced == str2:#если текущий срез равен искомому значению
            return i#возвращаем индекс первого элемента
            
print(exist('testtesttest', 'test'))
print(exist('ntest', 'test'))
print(exist('ntnest', 'test'))
