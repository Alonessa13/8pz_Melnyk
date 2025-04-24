def process_data(data, operation, dict_part="values"):
    """
    Обробляє список, кортеж або словник, застосовуючи функцію до кожного елемента.

    Параметри:
    - data: колекція даних
    - operation: функція для обробки
    - dict_part: для словника ('keys', 'values', 'items')

    Повертає:
    - нова оброблена колекція
    """
    try:
        if not callable(operation):
            raise TypeError("operation має бути функцією")

        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        elif isinstance(data, dict):
            if dict_part == "keys":
                return {operation(k): v for k, v in data.items()}
            elif dict_part == "values":
                return {k: operation(v) for k, v in data.items()}
            elif dict_part == "items":
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                raise ValueError("dict_part має бути 'keys', 'values' або 'items'")
        else:
            raise TypeError("Тип даних не підтримується")
    except Exception as e:
        return f"Помилка в process_data: {e}"

