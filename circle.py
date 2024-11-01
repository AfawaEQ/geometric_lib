import math

class Circle:
    def area(r):
        '''
        Принимает радиус r, возвращает площадь окружности радиуса r
        area(5) вернёт 78.53981633974483.
        '''
        return math.pi * r * r

    def perimeter(r):
        '''
        Принимает радиус r, возвращает периметр окружности радиуса r
        perimeter(5) вернёт 15.707963267948966
        '''
        return 2 * math.pi * r

