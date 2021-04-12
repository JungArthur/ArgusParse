def find_end_bracket(source, start_index):
    print(f'find_bracket : {source}    start : {start_index}')
    cursor = 0
    find_left_list = []
    find_right_list = []
    find_comma_list = []

    # find_left_list.append( slice_source.find('(') )

    for index in range(len(source)):

        if source[index] == ',':
            # print(f', : find index = {index}')
            find_comma_list.append(index)

        if source[index] == '(':
            # print(f'( : find index = {index}')
            find_left_list.append(index)

        if source[index] == ')':
            # print(f') : find index = {index}')
            find_right_list.append(index)

        # finish Flag len( find_left_list ) == len( find_right_list ) :
        if len(find_left_list) + len(find_right_list) > 1 and len(find_left_list) == len(find_right_list):
            # print('Scuccess')

            first_args_start = find_left_list[0]
            first_args_end = find_comma_list[0]
            last_args_start = find_comma_list[len(find_comma_list) - 1]
            last_args_end = find_right_list[len(find_right_list) - 1]

            # 재귀적이였으면 허용안됨.
            first_args = source[first_args_start + 1: first_args_end]
            last_args = source[last_args_start + 1: last_args_end]

            # 여기 포함되면 Pass
            mssql_third_args = ['1', '2', '3', '4', '5', '6', '7', '24']

            return {
                'first_args': first_args.strip(),
                'last_args': last_args.strip(),
                'first_args_result': -1 != first_args.strip().upper().find('CHAR'),
                'last_args_result': last_args.strip() in mssql_third_args
            }
        # End for

        # Error if slice_source's legnth over !
        # Error if find_left == -1 ! && if find_right == -1 !
        # left > right && both != -1
        # right < left && both != -1
        # left == -1 right != -1
        # left != -1 right == -1

    # End function


def conver_args(convert_string):

    if len(convert_string) == 0:
        return

    find_index = 0

    return_value_list = []

    while convert_string.find('CONVERT(', find_index + 1) != -1:

        find_index = convert_string.find('CONVERT(', find_index + 1)

        slice_source = convert_string[find_index:len(convert_string)]

        return_value = find_end_bracket(slice_source, find_index)

        print(f'result : {return_value}')

        return_value_list.append(return_value)

    return return_value_list
