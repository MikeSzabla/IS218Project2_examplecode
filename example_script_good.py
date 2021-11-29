"""
## example_script_good.py ##
script containing print_list method and a quick test to show its usage.
"""


def print_list(input_list):
    """print_list: takes in a list as a parameter and prints each element out on a new line.

    input_list: list of elements
    """
    for item in input_list:
        print(item)


list_to_print = ["I", "want", "these", "printed"]
print_list(list_to_print)
