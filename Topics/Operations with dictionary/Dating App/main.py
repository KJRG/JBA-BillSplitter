REQUIRED_MIN_AGE = 31
REQUIRED_HOBBY = "art"
REQUIRED_CITY = "Berlin"


def is_matching_person(person):
    is_matching_age = person["age"] >= REQUIRED_MIN_AGE
    is_matching_hobby = REQUIRED_HOBBY in person["hobbies"]
    is_matching_city = person["city"] == REQUIRED_CITY
    return is_matching_age and is_matching_hobby and is_matching_city


def select_dates(potential_dates):
    names_list = [person["name"] for person in potential_dates if is_matching_person(person)]
    return ', '.join(names_list)
