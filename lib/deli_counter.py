katz_deli = []

def line(the_line):
    length = len(the_line)
    if length == 0:
        print("The line is currently empty.")
    elif length > 0:
        words = "The line is currently:"
        index = 1
        for person in the_line:
            words += f" {index}. {person}"
            index += 1
        print(words)

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    length = len(katz_deli)
    print(f'Welcome, {new_person}. You are number {length} in line.')


def now_serving(katz_deli):
    length = len(katz_deli)
    if length > 0:
        print(f'Currently serving {katz_deli[0]}.')
        del(katz_deli[0])
    else:
        print("There is nobody waiting to be served!")
