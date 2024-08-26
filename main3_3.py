def print_params(a=1, b='строка', c=True):
    print(f"a: {a}, b: {b}, c: {c}")

print_params()  
print_params(10)
print_params(10, "другая строка")
print_params(10, "другая строка", False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [42, "новая строка", False]

values_dict = {
    'a': 99,
    'b': "еще одна строка",
    'c': [True, False]
}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [55, "распаковка списка"]
print_params(*values_list_2, 42)

