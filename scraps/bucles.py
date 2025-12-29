# range(start,stop,step)

for num in range(10, 0, -1):
    print(f"Bucle {num}")

print("Fin bucle")

# ----

colors = ["Pink", "Purple", "Orange", "Blue"]

print("---- COLORS ----")

for color in colors:
    if color == "Purple":
        print("Color Purple passed.")
        continue
    print(f"{color}")

# ----

i = 10
while i > 0:
    print(f"Num {i}")
    i -= 1

# ----

# equal to do-while
while True:
    q = input("Type 'exit' to quit.\n").lower()
    if q == 'exit':
        break
