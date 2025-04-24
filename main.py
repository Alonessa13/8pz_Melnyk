from process_data import process_data
from filter_data import filter_data
from combine_values import combine_values

# Тестування process_data
print("=== process_data ===")
print(process_data([1, 2, 3], lambda x: x + 10))
print(process_data((5, 6), lambda x: x * 2))
print(process_data({'a': 1, 'b': 2}, lambda x: x * 100, dict_part='values'))

# Тестування filter_data
print("\n=== filter_data ===")
print(filter_data([10, 15, 20], lambda x: x > 12))
print(filter_data((1, 2, 3), lambda x: x % 2 == 1))

# Тестування combine_values
print("\n=== combine_values ===")
print(combine_values(1, 2, 3, initial=10))
print(combine_values("Hello", "GPT", separator=" - "))
