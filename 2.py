def filter_data(data, predicate):
    """
    Фільтрує список або кортеж, залишаючи тільки елементи, які задовольняють умову.

    Параметри:
    - data: список або кортеж
    - predicate: функція, яка повертає True або False

    Повертає:
    - нова колекція з потрібними елементами
    """
    try:
        if not callable(predicate):
            raise TypeError("predicate має бути функцією")

        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        else:
            raise TypeError("Підтримуються лише список і кортеж")
    except Exception as e:
        return f"Помилка в filter_data: {e}"
