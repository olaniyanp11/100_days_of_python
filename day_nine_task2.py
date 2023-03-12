#!/usr/bin/python3


travel_log = [
{
"country": "France",
"visits": 12,
"cities": ["paris","lilies","Djon"]
},
{
 "country": "Germany",
 "visits": 5,
 "cities": ["Berlin","Hamburg","Stuttgart"]
},
]


def add_new_country(count,visits,cities):
    """
    adds new dictionary to the list
    """
    global travel_log
    travel_log.append({})
    length = len(travel_log)
    travel_log[length - 1] = {
        "country": count,
        "visits": visits,
        "cities": cities
            }
add_new_country("Russia",2,["Moscow","Saint Petersburg"])
add_new_country("America",10,["LA","Wasionton"])
add_new_country("Japan",12,["itchi","onikawa"])
print(travel_log)
