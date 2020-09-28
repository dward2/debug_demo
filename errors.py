def open_my_file(filename):
    try:
        input_fn = filename + ".txt"
        in_file = open(input_fn, 'r')
    except TypeError:
        return False
    except FileNotFoundError:
        return False
    print(input_fn)
    x = in_file.readlines()
    return x


def main():
    x = open_my_file("data")
    if x is False:
        print("Fix the file name")
        return
    print(x)

def pick_a_direction(choice=None):
    directions = ["n", "s", "e", "w"]
    if choice is None:
        choice = input("Pick a direction: ")
    if choice not in directions:
        raise ValueError("You picked an invalid direction")
    print("You chose {}".format(choice))
    return choice


def add_two_numbers(a, b):
    from warnings import warn
    warn("This is under development")
    if type(a) is not int or type(b) is not int:
        raise TypeError("Inputs must be python ints")
    if a < 0 or b < 0:
        raise ValueError("Cannot enter negative numbers")
    return a + b



if __name__ == '__main__':
    add_two_numbers(1, 3)

