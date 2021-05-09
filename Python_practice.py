counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list")
else:
    print("El Paso is NOT in the list")


if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe and El Paso is in the list of counties")
else:
    print("Arapahoe or el paso is not in the list of counties")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)