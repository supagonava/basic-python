# Condition
a, b = 10, 10
if a == b:
    print("a equal b")

a += 1
if a > b:
    print("a greater than b")
else:
    print("a is not greater than b")


score = 81
if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 60:
    print("Grade C")
elif score >= 50:
    print("Grade D")


# Looping
# -> While
a = 0
print("Loop while")
while a < 10:
    print("a", a)
    a += 1

print("Loop for")
for a in range(10):
    print("a", a)


print("Loop for in list of dict")
students = [
    {"id": "73857", "name": "Kyle Montgomery"},
    {"id": "67648", "name": "Laura Valdez"},
    {"id": "59650", "name": "Elva Griffin"},
    {"id": "39980", "name": "Bobby Sutton"},
    {"id": "13265", "name": "Winnie Estrada"},
    {"id": "44410", "name": "Clara Harris"},
    {"id": "40835", "name": "Genevieve Vaughn"},
    {"id": "15006", "name": "Nettie Lindsey"},
    {"id": "29563", "name": "Adam Holloway"},
    {"id": "62708", "name": "Lida Lyons"},
]
for st in students:
    print(st.get("id"), st.get("name"))
