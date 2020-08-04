import pyfiglet
msg = input("what would you like to print?")
color = input("what color?")

ascii = pyfiglet.figlet_format(msg)
print(ascii)
