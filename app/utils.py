def convert_category_to_num(default_category_str):
    if default_category_str is not "":
        if default_category_str == "Promotion pitch":
            return 0
        elif default_category_str == "Pickup lines":
            return 1
        elif default_category_str == "Interview pitch":
            return 2
        elif default_category_str == "Product pitch":
            return 3
        else:
            return -1


def convert_num_to_category(default_category_str):
    if default_category_str >= 0:
        if default_category_str == 0:
            return "Promotion pitch"
        elif default_category_str == 1:
            return "Pickup lines"
        elif default_category_str == 2:
            return "Interview pitch"
        elif default_category_str == 3:
            return "Product pitch"
        else:
            return "All"

