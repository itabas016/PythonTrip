""" This is the "nester.py" module and it provide one function called print_lol()
    which prints lists that may or may not include nested lists."""

def print_lol(the_list, level = 0):
    """ This function takes one positional argument called "the_list", which
        is any Python list (of - possibly - nested lists). Each data item in
        the provided list is (recursively) printed to the screen on it's own line."""

    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t")
            print(each_item)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print_lol(movies)