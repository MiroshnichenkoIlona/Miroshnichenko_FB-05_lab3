import time


def timer(func):
    def inner(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        print("time is: ", time.time() - begin)
        return result
    return inner


class GaloisFieldNumber:
    def __init__(self, number: str, field_size: int, field_generator: str):
        self.value = number
        self.field_size = field_size
        self.field_generator = field_generator

    def __str__(self):
        return self.value

    @timer
    def __add__(self, other):
        first_number = self.value
        second_number = other.value
        if len(first_number) > len(second_number):
            size = len(first_number)
        else:
            size = len(second_number)
        result_bin = ''
        for i in range(size):
            temp = int(first_number[i]) + int(second_number[i])
            result_bin += str(temp % 2)

        return self.__class__(result_bin, self.field_size, self.field_generator)

    @timer
    def __mul__(self, other):
        results = []
        for i in reversed(other.value):
            sub_result = []
            for a in self.value:
                sub_result.append(int(i) * int(a))
            results.append(sub_result)

        pre_matrix = []
        for i in range(len(self.value)):
            pre_list = []
            for j in range(2 * len(self.value) - 1):
                pre_list.append(0)
            pre_matrix.append(pre_list)

        counter = 0
        size = 2 * len(self.value) - 1
        for k in pre_matrix:
            k[size - len(self.value) - counter:size - counter] = results[counter]
            counter += 1

        final = ''
        for res in range(size):
            num = 0
            for i in pre_matrix:
                num += i[res]
            final += str(num % 2)
        return self.__class__(final, self.field_size, self.field_generator)

    @staticmethod
    def trace(field, num):
        counter_n = 1
        while field != 3:
            field //= 3
            counter_n += 1
        answer = bin(counter_n * int(num, 2) % 3)

        return answer

    @timer
    def __pow__(self, power, modulo=None):
        result = self.__class__(self.value, self.field_size, self.field_generator)
        for i in range(power):
            result = result * result
        return result


first = GaloisFieldNumber('00100110000111011110011011000110111110011111110100110101001110110110010010001101010100110101010111111111011001110111110101101101000011011101010111010010001101111100001101110001010', 1, '1')
print(f"First is: {first}")

second = GaloisFieldNumber('10011100000001001001111011011111010100101100110001011000100110110111010000101000000001000011000011000110110110011101001010111010101111100101111001101101110001011110101100100010100', 1, '1')
print(f"Second is:{second}")
print(f"Addition:{first + second}")

third = GaloisFieldNumber('10', 1, '1')
print(f"Third is:{third}")
forth = GaloisFieldNumber('11', 1, '1')
print(f"Forth is:{forth}")
print(f"Multiplication:{third * forth}")


trace = GaloisFieldNumber.trace(27, '10')
print(f"Trace in the field:{trace}")

print(first ** 3)