from selenium.webdriver import Keys

# print(Keys.ESCAPE)
#
# print(ascii(27))
# print(ascii(chr(27)))
#
# print(chr(27))
# print(ord(chr(27)))

at = [(name, value) for name, value in vars(Keys).items() if not name.startswith('_')]
l2 = [name for name, value in vars(Keys).items() if not name.startswith('_')]
# l3 = [Ke for i in l2]

# print(at)
print(l2)
print(l3)


