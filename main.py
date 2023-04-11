class StringArray:


 def __init__ (self,length):
        self.length = length
        self.array = ['' for _ in range(length)]

 def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Выход за пределы массива')
        return self.array[index]

 def set(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError('Выход за пределы массива')
        self.array[index] = value

 def concat(self, array2):
        if not isinstance(array2, StringArray) or array2.length != self.length:
            raise TypeError('Несовместимые типы')
        result = StringArray(self.length)
        for i in range(self.length):
            result.set(i, self.get(i) + array2.get(i))
        return result

 def merge(self, array2):
        if not isinstance(array2, StringArray) or array2.length != self.length:
            raise TypeError('Несовместимые типы')
        result = StringArray(self.length)
        for i in range(self.length):
            if self.get(i) not in result.array:
                result.set(i, self.get(i))
            if array2.get(i) not in result.array:
                result.set(i, array2.get(i))
        return result

 def print(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Выход за пределы массива')
        print(self.get(index))

 def printAll(self):
        for i in range(self.length):
            print(self.get(i))


#Пример использования класса:

# Создание двух массивов строк
array1 = StringArray(3)
array2 = StringArray(3)

# Заполнение массивов
import random
import string

array1.set(0, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
array1.set(1, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
array1.set(2, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))

array2.set(0, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
array2.set(1, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
array2.set(2, ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))


def __print_header__(header):
    print(f'\n{header}\n{"-" * len(header)}');


# Проверка работы методов
__print_header__('array1:')
array1.printAll()

__print_header__('array2:')
array2.printAll()

print('array1[1]:'), array1.get(1)

array1.concat(array2).printAll()

array1.merge(array2).printAll()
array1.merge(array2).printAll()