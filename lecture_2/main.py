def generate_profile(age: int) -> str:
    """
    :rtype: str
    """
    if age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teenager'
    else:
        return 'Adult'


user_name = input('Enter your full name: ')
birth_year_str = input('Enter your birth year: ')
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
while True:
    hobby = input('Enter a favorite hobby or type \'stop\' to finish: ')
    if hobby.lower() == 'stop' :
        break
    hobbies.append(hobby)

life_stage = generate_profile(current_age)
user_profile = {
    "Name": user_name,
    "Age": current_age,
    "Birth year": birth_year,
    "Life stage": life_stage,
    "Hobbies": hobbies
}
print('---', 'Profile Summary', sep='\n')
for key, value in user_profile.items():
    if key == 'Birth year':
        continue
    if key == 'Hobbies':
        if hobbies:
            print(f'Favorite hobbies ({len(hobbies)}):')
            for hobby in hobbies:
                print(f'- {hobby}')
            continue
        else:
            print('You didn\'t mention any hobbies')
            continue
    print(f'{key}: {value}')
print('---')


