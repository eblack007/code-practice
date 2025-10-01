def add_two_nums(a, b):
    return a + b

print(add_two_nums(3, 5))

def add_three_nums(a, b, c):
    return a + b + c

print(add_three_nums(1, 2, 3))

def join_names(name1, name2, name3):
    return f"Joined names: {name1}{name2}{name3}"

print(join_names("Alice", "Bob", "Charlie"))

def weeks_in_seconds(weeks):
    return weeks * 7 * 24 * 60 * 60

print(weeks_in_seconds(5))

def superify(name):
    return f'super{name}'
# Don't edit below this line.

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"

