users_data = {"id":[1, 2, 3], "name":["Maria", "Ivan", "Asen"],\
"number":["+39587111111","+39587222222","+39587333333"]}
users_bills = {"id":[1, 2, 3], "bill":[25.50, 30.48, 5.98]}

for i, l in enumerate(users_data["id"]):
    if l in users_bills['id']:
        if list(users_bills["bill"])[i] == max(users_bills['bill']):
            print(f"The user with highest bill - {max(users_bills['bill'])} is {list(users_data['name'])[i]}")
        elif list(users_bills["bill"])[i] == min(users_bills['bill']):
            print(f"The user with lowest  bill - {min(users_bills['bill'])} is {list(users_data['name'])[i]}")
