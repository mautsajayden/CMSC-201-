def print_favorite_numbers(who, favorites):
    """
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """
    # Check if the person exists in the dictionary
    if who in favorites:
        print(favorites[who])
    else:
        print(f"{who} has no favorite numbers yet.")


def add_favorite_number(who, number, favorites):
    """
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """

    number_found = False
    found_in = None
    for person in favorites:
        if number in favorites[person]:
            number_found = True
            found_in = person
            break

    if who not in favorites:
        favorites[who] = []

    if number_found:
        print(f"{number} was found in {found_in}'s favorites")
    else:
    
        if number in favorites[who]:
            print(f"{number} was found in {who}'s favorites")
        else:
            favorites[who].append(number)
            print(f"{number} added to {who}'s favorites")


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            who, num = in_string.split()
            num = int(num)
            add_favorite_number(who, num, favorites)

        in_string = input('What do you want to do (add favorite number), or quit? ')
