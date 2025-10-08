import re

def wrap_expression(expr: str):
    # Найти переменные: начинаются с буквы, содержат буквы, цифры и подчёркивания
    variables = set(re.findall(r'\b[A-Za-z][A-Za-z0-9_]*\b', expr))

    # Построить f-строку с фигурными скобками
    f_expr = expr
    for var in sorted(variables, key=len, reverse=True):  # сортировка по длине — чтобы не было вложенных замен
        f_expr = re.sub(rf'\b{var}\b', f'{{{var}}}', f_expr)

    # Финальный вывод: оборачиваем всё выражение в фигурные скобки
    return f'print(f"{f_expr} = {{{expr}}}")'

# Пример
expression = input("Введите выражение:\n")
print(wrap_expression(expression))
