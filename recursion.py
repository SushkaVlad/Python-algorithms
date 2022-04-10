def sum_of_digits(num):
    if num in {i for i in range(0, 10)}:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)


print(sum_of_digits(567))
