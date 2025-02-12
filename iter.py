#1.
class GeneratorIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generate_numbers()

    def generate_numbers(self):
        for i in range(self.start, self.end):
            yield i

gen_iter = GeneratorIterator(1, 5)
for value in gen_iter:
    print(value)

#2.
def safe_calculate(func):
    def wrapper(expression):
        try:
            return func(expression)
        except ZeroDivisionError:
            return "Ошибка: деление на ноль"
        except SyntaxError:
            return "Ошибка: неправильный синтаксис"
        except Exception as e:
            return f"Неизвестная ошибка: {e}"
    return wrapper

@safe_calculate
def calculate(expression):
    return eval(expression)

print(calculate("10 / 2")) 
print(calculate("10 / 0")) 
print(calculate("10 + x"))  
print(calculate("10 * 2"))