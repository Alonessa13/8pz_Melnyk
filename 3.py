def combine_values(*args, separator="", initial=None):
    """
    Об'єднує рядки або числа, в залежності від типу першого аргументу.

    Параметри:
    - *args: значення для об'єднання
    - separator: роздільник для рядків
    - initial: початкове значення для чисел

    Повертає:
    - результат об'єднання
    """
    try:
        if not args:
            return None

        first = args[0]

        if isinstance(first, str):
            return separator.join(str(arg) for arg in args)
        elif isinstance(first, (int, float)):
            result = initial if initial is not None else 0
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise ValueError("Усі аргументи мають бути числами")
                result += arg
            return result
        else:
            raise TypeError("Перший аргумент має бути рядком або числом")
    except Exception as e:
        return f"Помилка в combine_values: {e}"
