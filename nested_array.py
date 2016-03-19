def flatten(array_in):
    result_recursive = []
    result_recursive = flatten_nested_array_recursive(array_in, result_recursive)

    print "recursive: "
    print result_recursive

    result_iterative = []
    result_iterative = flatten_nested_array_iterative(array_in)

    print "iterative: "
    print result_iterative

    return result_iterative


def flatten_nested_array_recursive(array_in, result):
    for i in array_in:
        if isinstance(i, list):
            flatten_nested_array_recursive(i, result)
        elif i is not None:
            result.append(i)

    return result


def flatten_nested_array_iterative(array_in):
    output = []

    while len(array_in) > 0:
        element = array_in.pop(0)
        if isinstance(element, list):
            for index, item in enumerate(element):
                array_in.insert(index, item)
        else:
            if element is not None:
                output.append(element)

    return output


if __name__ == '__main__':
    array_in = input("input an array: ")
    flatten(array_in)

    items = [1, [7, [8, 9]]]

    print flatten_iter_two(items, list)
