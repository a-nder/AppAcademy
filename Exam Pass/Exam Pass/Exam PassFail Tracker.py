scores = {
    "Toby" : 65,
    "Randy" : 97,
    "Marge" : 73,
    "Lenny" : 44,
    "Trent" :38
}

passed_count = 0

for name, score in scores.items():
    if score >= 50:
        print(f"{name} passed with {score}")
        passed_count = passed_count + 1
    else:
        print(f"{name} failed with {score}")

print(f"{passed_count} students passed.")