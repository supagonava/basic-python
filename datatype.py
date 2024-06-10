x = "x"
print("x is", type(x), "value =", x)

y = 10
print("y is", type(y), "value =", y)

z = 11.23
print("z is", type(z), "value =", z)

xy: list = ["a", "b", "c"]
print("xy is", type(xy), "value =", xy)

xy.pop()  # ["a", "b"]
print(xy)

xy.append("c")  # ["a", "b", "c"]
print(xy)

xy.insert(1, "d")  # ["a", "d", "b", "c"]
print(xy)

xy.pop(1)
print(xy)  # ["a", "b", "c"]

xyz: dict = {"name": "supakorn", "last_name": "emch"}
print('xyz.get("name")', xyz.get("name"))
print('xyz.get("last_name")', xyz.get("last_name"))

xyz["last_name"] = "emchananon"
print('xyz.get("last_name")', xyz.get("last_name"))
xyz.update({"last_name": "emememem"})
print(xyz)

print("xyz is", type(xyz), "value =", xyz)

xy1: list = ["a", 1, 22.22]
print("xy1 is", type(xy1), "value =", xy1)

xy2: list[dict] = [xyz for d in range(2)]
print("xy2 is", type(xy2), "value =", xy2)

def get_x():
    return x