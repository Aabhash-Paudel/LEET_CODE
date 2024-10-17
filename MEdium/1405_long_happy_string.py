a, b, c = 7, 1, 0
s = []

def assign_order():
    global a, b, c
    order = {"high": None, "mid": None, "low": None}
    values = sorted([a, b, c], reverse=True)
    order["high"] = "a" if values[0] == a else "b" if values[0] == b else "c"
    order["mid"] = "a" if values[1] == a else "b" if values[1] == b else "c"
    order["low"] = "a" if values[2] == a else "b" if values[2] == b else "c"
    return order

def decrement_variable(var):
    global a, b, c
    if var == "a":
        a -= 1
    elif var == "b":
        b -= 1
    elif var == "c":
        c -= 1

lent = a
for i in range(lent):
    order = assign_order()
    s.append(order["high"])
    decrement_variable(order["high"])
    if i > 0 and s[i] == s[i-1]:
        s.append(order["mid"])
        decrement_variable(order["mid"])
        mid_value = eval(order["mid"])
        if mid_value == 0:
            s.append(order["low"])

print(s)