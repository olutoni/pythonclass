guests_list = ["Eniola", "Tomide", "Tofunmi"]

for guest in guests_list:
    print(f"Hi {guest}, you are cordially invited for dinner.")

print()
print(f"{guests_list[1]} can not make it to dinner tonight.")
print()

for guest in guests_list:
    if guest != "Tomide":
        print(f"Hi {guest}, you are cordially invited for dinner.")

print()
print("I have found a bigger table and will be inviting more guests")

guests_list.insert(0, "Folake")
guests_list.insert(2, "Jimi")
guests_list.append("Kola")

print(guests_list)
print()
for guest in guests_list:
    if guest != "Tomide":
        print(f"Hi {guest}, you are cordially invited for dinner.")

print("Sorry, I can only invite two guests as the bigger table won't arrive in time")

print(f"Hi {guests_list.pop()}, I'm sorry, you are no longer invited")
print(f"Hi {guests_list.pop()}, I'm sorry, you are no longer invited")
print(f"Hi {guests_list.pop()}, I'm sorry, you are no longer invited")
print(f"Hi {guests_list.pop()}, I'm sorry, you are no longer invited")

print()
for guest in guests_list:
    print(f"Hi {guest}, you are still invited for dinner.")

del guests_list[0:2]
print(guests_list)
