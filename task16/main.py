def flatten_list(nested_list):
    stack = list(nested_list)
    copied_list = []
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            copied_list.append(item)
    return copied_list


def main():
    nested = [[1, 2, [3, 4,[300,400]],[100,200]],
              [5, 6],
              [9,8],
              [10,11,12],
              7,
              [13,14],
              [1, 2, [3, 4]],
              [5, 6],
              7]
    print("The Nested List before flattening is: ")
    for i in nested:
        print(i)
    print("The Nested List after flattening is: ")
    res = flatten_list(nested)
    print(res)

if __name__ == '__main__':
    main()