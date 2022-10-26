INPUT_ARRAY = []

def commonPrefix(inputs):
    # Loop that iterates through the input array.
    sum_list = []
    for item in inputs:
        sum_list.append(prefix_sum(item))

    return sum_list

def check_common_prefix_length(str1, str2):
    # Zips two strings together and then iterates through every
    # character until a character from both strings do not match.
    # A counter is incremented every time characters match.
    i = 0
    for x, y in zip(str1, str2):
        if x == y:
            i += 1
        else:
            break

    return i

def prefix_sum(input_str):
    comp_val = [] # The array that stores the common prefix sum

    for i in range(len(input_str)):
        suffix = input_str[i:] # Get a suffix for the current point in the string
        comp_val.append(check_common_prefix_length(suffix, input_str))

    return sum(comp_val)


if __name__ == '__main__':
    print(commonPrefix(INPUT_ARRAY))
