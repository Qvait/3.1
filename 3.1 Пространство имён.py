calls = (0)
b = 0
c = "aboba"
d = "aboba"
x = "abiba"
z = (str(0))
g = (str(0))
def count_calls():
    global calls
    calls = (calls + 1)
def string_info (a):
    count_calls()
    b = len(a)
    c = a.upper()
    d = a.lower()
    print(b, c, d)
def is_contains (text, list_):
    count_calls()
    return text.lower() in [item.lower() for item in list_]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
