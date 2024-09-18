import math
import datetime
from haversine import haversine
from collections import Counter
import numpy as np
import random
from lab_lib import Student, Lab
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import re
from faker import Faker
import morse_code
import os

class Lab1(Lab):
    @staticmethod
    def part1(value=None):
        if not value:
            value = input("enter value")
        try:
            v = int(value)
        except ValueError:
            print("ValueError")
            return
        res = 1 / 4 - 1 / 4 * (math.sin((5 / 2 * math.pi) - 8 * v))
        print(f"1/4-1/4*(math.sin((5/2*math.pi) - 8*v)) = {res:.3f}")
        return res

    @staticmethod
    def part2():
        v = [input("Введіть а:"), input("Введіть b:"), input("Введіть c:")]
        v = map(int, v)
        try:
            a, b, c = v
        except ValueError:
            print("ValueError")
            return
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f"Площа трикутника дорівнює {s:.3f}")
        return s

    def part3(self):
        value = input("Введіть шестизначний номер:")
        if self._validate_input_for_digits(value) or len(value) != 6:
            print("Невірний номер")
            return
        res = sum(map(int, value[:3])) == sum(map(int, value[3:]))
        print(f"Щасливий квиток {value}? {res}")
        return res

    def part4(self, value=None):
        if value is None:
            value = input("Значення  у хвилинах:")
        if self._validate_input_for_digits(value):
            print("Невірний номер")
            return
        value = int(value)
        print(f"{value // 60} годин {value % 60} хвилин")

    def part5(self, value=None):
        if value is None:
            value = input("birth у форматі день-місяць-рік")
        try:
            day, month, year = map(int, (value.split("-")))
            date = datetime.date(year, month, day)
        except ValueError:
            print("Невірний ввід")
            return
        now = datetime.datetime.now().date()
        res = now - date
        print(f"{res.days // 365}")

    def practice_1(self, value=None, scale=None):
        if value is None:
            value = input("input temperature:")
            scale = input("input C for Celsius or F for Fahrenheit")
        if self._validate_input_for_digits(value) or scale not in ["C", "F"]:
            print("Невірний ввід")
            return
        value = int(value)
        if scale == "C":
            print(value * (9 / 5) + 32)
            return
        print((value - 32) * (5 / 9))

    def practice_2(self, value=None):
        if value is None:
            value = input("Значення швидкості")
        if self._validate_input_for_digits(value):
            print("Невірний ввід")
            return
        value = int(value)
        km_h = value * 3600 / 1000
        m_s = value / 3600 * 1000
        print(f"{value} кілометрів за годину (км/год) = {m_s} метри за секунду (м/с)",
              f"{value} метри за секунду (м/с) = {km_h} кілометрів за годину (км/год)")

    def practice_3(self, value1=None, value2=None):
        if not value1 and not value2:
            value1 = input("lat1, lon1 – широта та довгота першого міста")
            value2 = input("lat2, lon2 – широта та довгота другого міста")
        try:
            coord_1 = map(float, value1.split(","))
            coord_2 = map(float, value2.split(","))
            res = haversine(coord_1, coord_2)
            print(f"{res}")
        except ValueError:
            print("Невірний ввід")

    def practice_4(self, value=None):
        if not value:
            value = input("Введіть верхню межу діапазону")
        if self._validate_input_for_digits(value):
            print("Невірний ввід")
            return
        value1 = int(value)
        primes = []
        for i in range(2, value + 1):
            for j in range(2, i // 2, 2):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        print(f"Прості числа у діапазоні від 1 до {value}: {' '.join(map(str, primes))}")

    def practice_5(self, value=None):
        box_size = 6
        if not value:
            value = input("кількість яблук")
        if self._validate_input_for_digits(value):
            print("Невірний ввід")
            return
        value = int(value)
        print(f"кількість повних упаковок, які можна заповнити цими яблуками = {value // box_size}, "
              f" кількість яблук, які залишаться поза упаковками = {value % box_size}")


class Lab2(Lab):
    def part1(self):
        x, y = input("X:"), input("Y:")
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print("Невірний ввід")
            return
        print(abs(x) + abs(y) / 2 <= 1)

    def part2(self):
        number = input("Введіть чотиризначне число:")
        try:
            map(int, number)
            if len(number) != 4:
                raise ValueError
        except ValueError:
            print("Невірний ввід")
            return

        print(f'Число {"не " if "5" not in number else ""}містить цифру 5')
        print(f'складається лише з {"не" if all(map(lambda x: int(x) % 2 != 0, number)) else ""}парних чисел;')
        print(f'сума його цифр {"більша" if sum(map(int, number)) > 10 else "менша"} за число 10;')

        s = sum(map(int, number[0:2])) > sum(map(int, number[2:]))
        print(f"сума його перших двох цифр {'більша' if s else 'не більша'} за суму наступних двох цифр")

    @staticmethod
    def part3():
        sides = [input("Введіть а:"), input("Введіть b:"), input("Введіть c:")]
        try:
            sides = list(map(int, sides))
            sides.sort(reverse=True)
            c, a, b = sides
        except ValueError:
            print("Невірний ввід")
            return
        perimetr = sum(sides)
        if c >= b + a:
            print("трикутника з такими сторонами не існує.")
        elif c ** 2 == b ** 2 + a ** 2:
            print("прямокутний трикутник")
        elif c > b ** 2 + a ** 2:
            print("тупокутний трикутник")
        elif c > b ** 2 + a ** 2:
            print("гострокутний трикутник;")

    @staticmethod
    def part4():
        board = [["*" for _ in range(8)] for j in range(8)]
        moves = input("Приклад вхідних і вихідних даних 1 1 5 5     :").split()
        try:
            moves = list(map(int, moves))
            if any(map(lambda x: 0 > x > 8, moves)) or len(moves) != 4:
                raise ValueError
        except ValueError:
            print("Невірний ввід")
            return
        if (moves[0] == moves[2] or moves[1] == moves[3]) and not (moves[0] == moves[2] and moves[1] == moves[3]):
            print("YES")
        else:
            print("NO")
        board[moves[0]][moves[1]] = "\u2656"
        board[moves[2]][moves[3]] = "\u2656"
        for i in board:
            print("  ".join(i))

    @staticmethod
    def part5():
        x = 0.2
        sum_for = 0
        for j in range(1, 11):
            for i in range(1, 6):
                sum_for += (i ** 2 * x ** i + 1) / (math.factorial(j) * i ** 2)

        sum_while = 0
        j = 1
        while j <= 10:
            i = 1
            while i <= 5:
                sum_while += (i ** 2 * x ** i + 1) / (math.factorial(j) * i ** 2)
                i += 1
            j += 1

        if sum_for == sum_while:
            print(sum_for)

    @staticmethod
    def practice1():
        sides = [input("Введіть а:"), input("Введіть b:"), input("Введіть c:"), input("Введіть а:"),
                 input("Введіть b:"), input("Введіть c:")]
        try:
            sides = list(map(int, sides))
            first_sides, second_sides = list(sides[:3]), list(sides[3:])
            first_sides.sort(), second_sides.sort()
            if len(first_sides) != 3 or len(second_sides) != 3:
                raise ValueError
        except ValueError:
            print("Невірний ввід")
            return
        a1, b1, c1, = first_sides
        a2, b2, c2, = second_sides
        if first_sides == second_sides:
            print("коробки однакові")
            return
        elif a1 > a2 and b1 > b2 and c1 > c2:
            print("другу коробку можна покласти в першу;")
            return
        elif a2 > a1 and b2 > b2 and c2 > c1:
            print("першу коробку можна покласти в другу")
            return
        else:
            print("коробки не розміщуються одна в одну.")

    @staticmethod
    def practice2():
        sides = [input("Введіть а:"), input("Введіть b:"), input("Введіть c:"), input("Введіть d:")]
        try:
            sides = list(map(int, sides))
            if len(sides) != 4:
                raise ValueError
            sides.sort()
        except ValueError:
            print("Невірний ввід")
            return
        if sides[0] == sides[1] and sides[2] == sides[3]:
            print("YES")
        else:
            print("NO")

    def practice3(self):
        n = input("Введіть число")
        if self._validate_input_for_digits(n):
            return
        n = int(n)
        result = 1
        for i in range(1, n + 1, 2):
            result *= i
        print(result)

    @staticmethod
    def practice4():
        for i in range(0, 11, 1):
            print(f"sin({i / 10}) = {math.sin(i / 10):.3f}")

    def practice5(self):
        n = input("введіть n:")
        try:
            sequence = [int(input()) for _ in range(int(n))]
        except ValueError:
            print("Невірний ввід")
            return
        print(f"MAX = {max(sequence)}")
        print(f"MIN = {min(sequence)}")
        count = Counter(sequence)
        common = count.most_common()
        print(f"мода = {common}")
        sequence.sort()
        if len(sequence) % 2 != 0:
            median = sequence[len(sequence) // 2]
        print(f"медіана = {np.median(sequence)}")
        sigma = np.std(sequence)
        s_arif = sum(sequence) / len(sequence)
        result = [i for i in sequence if 3 * sigma + s_arif > i < 3 * sigma - s_arif]
        if result:
            print(f" елементи, які виходять за межі правила 3 сігм (правило 3-sigma rule):{result}")


class Lab3(Lab):

    def part1(self, sequence=None):
        if sequence is None:
            sequence = [random.randint(0, 100) for _ in range(10)]
        print(min(sequence))
        print(min(sequence) + max(sequence))
        print(max(sequence))

    def part2(self, sequence=None):
        if sequence is None:
            sequence = [random.randint(1, 9) for _ in range(100)]
        count = Counter(sequence)
        print(count)
        print(f"діапазон [1, 3] = {sum(count[i] for i in range(1, 4))},"
              f"[4, 6] = {sum(count[i] for i in range(4, 7))}, "
              f"[7, 9] = {sum(count[i] for i in range(7, 10))}")

    def part3(self, sequence=None):
        if sequence is None:
            sequence = [random.randint(1, 100) for _ in range(50)]
        print(max(sequence))
        del sequence[3]
        one_more_sequence = sorted(sequence)
        one_more_sequence = one_more_sequence[:3] + [11111] + one_more_sequence[3:]
        print(one_more_sequence)
        one_more_sequence = list(map(lambda x: x * 3 if x > 10 else x, one_more_sequence))
        print(one_more_sequence)
        print(sequence)

    def part4(self, sequence=None, prnt=False):
        print("Processing...")
        if sequence is None:
            sequence = tuple([Student() for _ in range(106)])
        if prnt:
            for student in sequence:
                print(student.name, student.middle_name, student.surname)
        male, female = [], []
        for student in sequence:
            if student.gender == "male":
                male.append(student.name)
            else:
                female.append(student.name)
        print(Counter(male).most_common(1))
        print(Counter(female).most_common(1))
        ages = [student.age for student in sequence]
        age, count = Counter(ages).most_common(1)[0]
        ind = 0
        # small chase of ValueError
        for i in range(count):
            index = ages.index(age, ind)
            student = sequence[index]
            ind = index + 1
            print(student.name, student.middle_name[0] + ".", student.surname[0] + ".")

    def part5(self):
        sequence = "".join([str(random.randint(0, 1)) for _ in range(100)])
        res = None
        for i in range(1, len(sequence)):
            indexes = sequence.find(i * "1")
            if indexes == -1:
                break
            res = i * "1", indexes, indexes + i
        print(res)

    def practice1(self):
        coords_x = [random.randint(-150, 150) for _ in range(100)]
        coords_y = [random.randint(-150, 150) for _ in range(100)]
        counter = 0
        max_counter = 0
        max_coords = None
        radius = 50
        step = 5
        max_points_list = []
        for y in range(-150, 151, step):
            for x in range(-150, 151, step):
                point_list = []
                counter = 0
                for c_x, c_y in zip(coords_x, coords_y):
                    if (x - c_x) ** 2 + (y - c_y) ** 2 <= radius ** 2:
                        counter += 1
                        point_list.append((c_x, c_y))
                if counter > max_counter:
                    max_counter = counter
                    max_coords = x, y
                    max_points_list = point_list

        circle = Circle(max_coords, radius, fill=False, label='circle')
        fig, sp = plt.subplots()
        sp.add_patch(circle)
        sp.scatter(coords_x, coords_y)
        sp.grid(True)
        print(max_coords, max_counter, max_points_list)
        plt.show()

    def practice2(self, original_sentence=None):
        if original_sentence is None:
            original_sentence = \
                ("Installing collected packages: pyparsing, pillow, packaging kiwisolver, fonttools, cycler, "
                 "contourpy, matplotlib")
        sentence = re.sub(r"[,:!?]", '', original_sentence)
        sentence = sentence.split()
        sentence.sort(key=len)
        print(f"найкоротше слово речення{sentence[0], original_sentence.find(sentence[0]), len(sentence[0])}")
        print(f"найдовше слово речення {sentence[-1], original_sentence.find(sentence[-1]), len(sentence[-1])}")
        volves = []
        for i in sentence:
            word = []
            for j in i:
                if j in "AEIOUaeiou":
                    word.append(j)
            volves.append(word)
        position = volves.index(sorted(volves)[-1])
        print(f"слово, що містить найбільшу кількість голосних літер:{sentence[position]}")

    def practice3(self, c=None):
        # it ON**2 i gues it is better solution
        if c is None:
            fake = Faker('uk_UA')
            addresses = [fake.address() for _ in range(10)]
            c = [[fake.last_name(), fake.city(), random.choice(addresses)] for i in range(15)]

        result = []
        for index, data1 in enumerate(c):
            for index1, data2 in enumerate(c):
                _, city, address = data1
                __, city1, address1 = data2
                if city != city1 and address1 == address and index != index1:
                    if ((__, city1, address1), (_, city, address)) not in result:
                        result.append(((_, city, address), (__, city1, address1)))
        for line in result:
            print(line)

    def practice4(self, students=None):
        if students is None:
            fake = Faker('uk_UA')
            names = [fake.last_name() for i in range(10)]
            groups = ["RT"+str(random.randint(1,50)) for i in range(10)]
            grades = [3,4,5,None]
            students = []
            for i in range(25):
                student = {"Name":random.choice(names), "group":random.choice(groups),
                           "grades":[random.choice(grades) for i in range(3)]}
                students.append(student)

        zaborg = []
        good_st = []
        grd = [0,0,0]
        for student in students:
            counter = 0
            for order, grade in enumerate(student["grades"]):
                if grade is None:
                    zaborg.append(student["Name"])
                else:
                    grd[order] += grade
                    if grade == 4 or grade == 5:
                        counter += 1
            if counter == 3:
                good_st.append(student["Name"])

        print(f"Найкраще здали предмет номер { grd.index(max(grd)) + 1}")
        print(f"заборговоності у студентів {zaborg})")
        print(f"Здали на  4-5 {good_st}")

    def practice5(self, numbers=None):
        if numbers is None:
            numbers = [random.randint(1,9999) for i in range(10000)]
        f1 = 1
        f2 = 1
        i= 0
        fbn=[]
        while i < 15000:
            fibonachi = f1 + f2
            fbn.append(fibonachi)
            f1 = f2
            f2 = fibonachi
            i += f1
        res = []
        for ind, num in enumerate(numbers):
            if num in fbn:
                res.append(num)
        print(f"числа фібоначі із ряду {res}")
        print(f"порядок чисел {[fbn.index(i) for i in res]}")




class Lab4(Lab):
    def part1(self,numbers = None):
        if numbers is None:
            numbers = [random.randint(1, 100) for _ in range(100)]
        print(f"максимальне значення = {max(numbers)}, мінімальне значення = {min(numbers)}")
        print(f"среднє значення = {sum(numbers)/len(numbers)}")

    def part2(self):
        res = []
        for i in range(0,10):
            for j in range(0,10):
                for k in range(0,10):
                    for q in range(0,10):
                        for w in range(0,10):
                            for e in range(0,10):
                                if i + j + k == q + w + e:
                                    r = "".join(map(str,[i,j,k,q,w,e]))
                                    res.append(r)
        print(res)
        def sum_of_3(number):
            res = 0
            for i in range(3):
                res += number % 10
                number -= number % 10
                number //= 10
            return res

    def part3(self, value=None):
        if value is None:
            value = "safdjkghlghfdkjghfdkjlakfkdj"
        res = morse_code.encrypt(value)
        print(res)

    def part3_1(self, value=None):
        if value is None:
            value = ".-. ----. . -.-. .. .--- ..-. --. -.- ..-. --. . -.-. .--- .. ..-. "
        res = morse_code.decrypt(value)
        print(res)

    def part4(self, data=None, key=None):
        if key is None:
            key = "gsljjsdlalfalafdsgdsgsd"
        if data is None:
            data = "README.md"
        with open(data, "r") as file:
            data = file.read()
            while len(key) < len(data):
                key += key
            res = []
            for ch, k in zip(key, data):
                symb = int(ord(k)) ^ int(ord(ch))
                res.append(chr(symb))
        with open ("encrypted", "w") as file:
            file.write("".join(res))

    def part4_1(self, key =None):
        if key is None:
            key = "gsljjsdlalfalafdsgdsgsd"

        with open("encrypted", "r") as file:
            data = file.read()
            while len(key) < len(data):
                key += key
            res = []
            for ch, k in zip(key, data):
                symb = int(ord(k)) ^ int(ord(ch))
                res.append(chr(symb))
            print("".join(res))

    def part5(self, number="568596840", minimum = 11, maximum = 0, summa = 0):
        if len(number) > 0:
            current = int(number[0])
            summa += current
            if current < minimum:
                minimum = current
            if current > maximum:
                maximum = current
            self.part5(number[1:], minimum, maximum, summa)
        if len(number) == 0:
            print(minimum, maximum, summa)

    def practice1(self):
        def deco(func):
            def wrapper(*args):
                for i in args:
                    if type(i) is not int:
                        raise ValueError
                return func(*args)
            return wrapper
        @deco
        def func(*args):
            print(args)

        func(1,"a",3)

    def practice2(self, number=28):
        counter = 0
        for i in range(1,number):
            if number % i == 0:
                counter += i
        print(number == counter)

    def practice3(self):
        def deco(func):
            try:
                func()
            except Exception as E:
                print(E)


    def practice4(self):
        def paskal(number=10, row=[1]):
            for i in range(number):
                print(row)
                row = [sum(x) for x in zip([0] + row, row + [0])]
                yield row
        for i in paskal():
            print(i)

    def practice5(self, url="https://www.google.com/search?q=test&oq=test&gs_lcrp=EgZjaHJv"
                            "bWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIHCAMQABiPAtIBCTE4NzRqMGo"
                            "xNagCCLACAQ&sourceid=chrome&ie=UTF-8"):
        url = url.split("//")
        res = {"proto":url[0]}
        url = url[1].split("/")
        site = url[0].split(".")
        res["site"] = [i for i in site]
        res["tail"] = url[1]
        print(res)

    def practice6(self, students=None):
        if students is None:
            fake = Faker('uk_UA')
            names = [fake.last_name() for i in range(10)]
            groups = ["RT"+str(random.randint(1,50)) for i in range(10)]
            grades = [3,4,5,None]
            students = []
            for i in range(25):
                student = {"Name":random.choice(names), "group":random.choice(groups),
                           "grades":[random.choice(grades) for i in range(3)], "age":random.randint(16, 100)}
                students.append(student)
        min_age = 101
        res = None
        d = {}
        for st in students:
            if st["age"] < min_age:
                res = st
                min_age = st["age"]
            d[st["age"]] = st
        print(res)
        print(d)

    def pratice7(self, path="/home/easyktk/", s="deb"):
        for r, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(s):
                    print(name)





class Lab5(Lab):
    pass


class Lab6(Lab):
    pass


if __name__ == "__main__":
    pass
    # Lab2()()
    # lab3 = Lab4()
    # lab3.pratice7()
