def complex_function(func, *args):
    for arg in args:
        print(f'Resultado de la multiplicación es: {func(5, arg):^20.2f}')


complex_function(lambda num2, num3: num2 * num3, 10, 20, 30, 50, 12)