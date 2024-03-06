import random

def random_name():
    name_length = random.randrange(8, 12)

    first_name = []
    for i in range(name_length):
        temp=random.choice("abcdefghijklmnopqrstuvwxyz")
        first_name.append(temp) 
    fname = ''.join(first_name)

    last_name = []
    for j in range(name_length):
        temp=random.choice("abcdefghijklmnopqrstuvwxyz")
        last_name.append(temp)
    lname = ''.join(last_name)

    return fname.capitalize(), lname.capitalize()


def random_age():
	# Return a random number between 18 and 81
    age = random.randrange(8, 81)
    return age


def random_person():
	first_name, last_name = random_name()
	result = {
		"first_name": first_name,
		"last_name": last_name,
		"age": random_age()
	}

	return result


def getlist(num_people):
	# return a list of unique random_people of length = num_people
    people=[]
    for i in range(num_people):
        people.append(random_person())
    
    sorted_data = sorted(people, key=lambda x: x['age'], reverse=True)
    unique = {i['first_name']: i for i in sorted_data}
    print (list(unique.values()))
    return unique

test = getlist(5)