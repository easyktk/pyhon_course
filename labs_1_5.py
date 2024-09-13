import math
import datetime
from haversine import haversine
from collections import Counter
import numpy as np
import random
from lab_lib import Student, Lab
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

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
        res = 1/4-1/4*(math.sin((5/2*math.pi) - 8*v))
        print(f"1/4-1/4*(math.sin((5/2*math.pi) - 8*v)) = {res:.3f}")
        return res

    @staticmethod
    def part2(value=None):
        v = [input("Введіть а:"), input("Введіть b:"), input("Введіть c:")]
        v = map(int, v)
        try:
           a, b, c = v
        except ValueError:
            print("ValueError")
            return
        p = (a + b + c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print(f"Площа трикутника дорівнює {s:.3f}")
        return s

    def part3(self, value=None):
        value =input("Введіть шестизначний номер:")
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
        print(f"{value//60} годин {value % 60} хвилин")

    def part5(self, value=None):
        if value is None:
            value = input("birthd у форматі день-місяць-рік")
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
            print(value*(9/5)+32)
            return
        print((value - 32)*(5/9))

    def practice_2(self, value=None):
        if value is None:
            value = input("Значення швидкості")
        if self._validate_input_for_digits(value):
            print("Невірний ввід")
            return
        value = int(value)
        km_h = value * 3600 / 1000
        m_s = value / 3600 * 1000
        print(f"{value } кілометрів за годину (км/год) = {m_s} метри за секунду (м/с)",
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
            value = input("Введіть верню межу діапазону")
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
        print(f"Прості числа у діапазоні від 1 до {value}: {" ".join(map(str, primes))}")

    def practice_5(self, value=None):
        box_size = 6
        if not value:
            value = input("кількість яблук")
        if self._validate_input_for_digits(value):
            print("Невірний ввід")
            return
        value = int(value)
        print(f"кількість повних упаковок, які можна заповнити цими яблуками = {value//box_size}, "
              f" кількість яблук, які залишаться поза упаковками = {value%box_size}")


class Lab2(Lab):
    def part1(self):
        x, y = input("X:"), input("Y:")
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print("Невірний ввід")
            return
        print(abs(x) + abs(y)/2 <= 1)

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
        print(f'складається лише з {"не" if all(map(lambda x: int(x) % 2 != 0,  number)) else ""}парних чисел;')
        print(f'сума його цифр {"більша" if sum(map(int,number)) > 10 else "менша"} за число 10;')

        s = sum(map(int, number[0:2])) > sum(map(int, number[2:]))
        print(f"сума його перших двох цифр {"більша" if s else "не більша"} за суму наступних двох цифр")

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
        elif c**2 == b**2 + a**2:
            print("прямокутний трикутник")
        elif c > b**2 + a**2:
            print("тупокутний трикутник")
        elif c > b**2 + a**2:
            print("гострокутний трикутник;")

    @staticmethod
    def part4():
        board = [["*"for i in range(8)] for j in range(8)]
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
                sum_for += (i**2 * x**i + 1)/(math.factorial(j) * i**2)

        sum_while = 0
        j = 1
        while j <= 10:
            i = 1
            while i <= 5:
                sum_while += (i**2 * x**i + 1)/(math.factorial(j) * i**2)
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
        a1, b1, c1,  = first_sides
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
        for i in range(1, n+1, 2):
            result *= i
        print(result)

    @staticmethod
    def practice4():
        for i in range(0, 11, 1):
            print(f"sin({i/10}) = {math.sin(i/10):.3f}")

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
        s_arif = sum(sequence)/len(sequence)
        result = [i for i in sequence if 3*sigma + s_arif > i < 3*sigma - s_arif]
        if result:
            print(f" елементи, які виходять за межі правила 3 сігм (правило 3-sigma rule):{result}")



    def __hash__(self):
        return hash((self.name, self.middle_name, self.surname, self.gender, self.age, self.course))

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.__hash__() == other.__hash__():
                return True
        return False

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
        print(f"діапазон [1, 3] = {sum(count[i] for i in range(1,4))},"
                f"[4, 6] = {sum(count[i] for i in range(4,7))}, "
              f"[7, 9] = {sum(count[i] for i in range(7,10))}")

    def part3(self, sequence=None):
        if sequence is None:
            sequence = [random.randint(1, 100) for _ in range(50)]
        print(max(sequence))
        del sequence[3]
        one_more_sequence = sorted(sequence)
        one_more_sequence = one_more_sequence[:3] + [11111] + one_more_sequence[3:]
        print(one_more_sequence)
        one_more_sequence = list(map(lambda x: x*3 if x > 10 else x, one_more_sequence))
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
        #small chase of ValueError
        for i in range(count):
            index = ages.index(age, ind)
            student = sequence[index]
            ind = index + 1
            print(student.name, student.middle_name[0] + ".", student.surname[0] + ".")


    def part5(self):
        sequence = "".join([str(random.randint(0, 1)) for _ in range(100)])
        res = None
        for i in range(1, len(sequence)):
            indexes = sequence.find(i*"1")
            if indexes == -1:
                break
            res = i*"1", indexes, indexes + i
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
                    if (x - c_x)**2 + (y - c_y)**2 <= radius**2:
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












class Lab4(Lab):
    pass
class Lab5(Lab):
    pass

class Lab6(Lab):
    pass



if __name__ == "__main__":
    pass
    #Lab2()()
    lab3 = Lab3()
    lab3.practice1()
