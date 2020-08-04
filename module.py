def get_new_york_ric():
    id = 1
    yield str(id)+".n"
    id += 1

def get_london_ric():
    id = 1
    yield str(id)+".l"
    id += 1

def get_ric(exchange):
    if exchange == "n":
        return get_new_york_ric()
    else:
        return get_london_ric()

r = get_ric("l")
print(next(r))
r = get_ric("n")
print(next(r))
print(next(r))
