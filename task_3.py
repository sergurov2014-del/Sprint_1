
world_champions = {
    2002: "Бразилия",
    2006: "Италия",
    2010: "Испания",
    2014: "Германия",
    2018: "Франция",
}
world_champions[2022] = "Аргентина"
country = "Италия"
flag = False
for key, value in world_champions.items():
    print(f"{key} - {value}")
    if value == country:
        flag = True
if flag:
    print(f"{country} cтановилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country } не выигрывала чемпионат мира по футболу в 21 веке.")