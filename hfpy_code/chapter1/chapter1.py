__author__ = 'Roger'
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)


for each_item in movies:
    print(each_item)


for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)


for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)


for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    if isinstance(deeper_item, list):
                        for deepest_item in deeper_item:
                            print(deepest_item)
                    else:
                        print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)


def print_lol(a_list):
    for each_item2 in a_list:
        if isinstance(each_item2, list):
            print_lol(each_item2)
        else:
            print(each_item2)
print_lol(movies)