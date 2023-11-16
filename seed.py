from actions import create_data_table, create_mob

#DATABASE SEEDING AND REGENERATIVE POPULATION

mobs = []
mob_1 = {
    "name": "Zombie",
    "hit_points": 20,
    "damage": 2,
    "speed": 1,
    "is_hostile": True
}
mob_2 = {
    "name": "Villager",
    "hit_points": 30,
    "damage": 1,
    "speed": 1,
    "is_hostile": False
}
mob_3 = {
    "name": "Enderman",
    "hit_points": 40,
    "damage": 4,
    "speed": 2,
    "is_hostile": False
}
mob_4 = {
    "name": "Cave Spider",
    "hit_points": 12,
    "damage": 2,
    "speed": 2,
    "is_hostile": True
}
mob_5 = {
    "name": "Blaze",
    "hit_points": 8,
    "damage": 3,
    "speed": 1,
    "is_hostile": True
}
mob_6 = {
    "name": "Iron Golem",
    "hit_points": 50,
    "damage": 6,
    "speed": 1,
    "is_hostile": False
}

mobs.append(mob_1)
mobs.append(mob_2)
mobs.append(mob_3)
mobs.append(mob_4)
mobs.append(mob_5)
mobs.append(mob_6)

create_data_table()

for mob in mobs:
    print(create_mob(mob))