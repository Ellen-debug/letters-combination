# stage 1
data = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def show_results(numbers_list, index, output, length):
    if index == length:
        for item in output:
            print(item, end='')
        print(' ', end='')
        return

    for j in range(len(data[numbers_list[index]])):
        output.append(data[numbers_list[index]][j])
        show_results(numbers_list, index + 1, output, length)
        output.pop()


number = input('Please enter a list of integers: ')
numbers = []
for i in number:
    if i.isdigit():
        if i != '1' and i != '0':    # 把输入域的0和1过滤掉 因为这两个数字没有任何输出
            numbers.append(int(i))
n = len(numbers)
show_results(numbers, 0, [], n)


# stage 2
data = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def show_results(numbers_list, index, output, length):
    if index == length:
        for item in output:
            print(item, end='')
        print(' ', end='')
        return

    for j in range(len(data[numbers_list[index]])):
        output.append(data[numbers_list[index]][j])
        show_results(numbers_list, index + 1, output, length)
        output.pop()


number = input('Please enter a list of integers: ')
numbers = []
for i in number:
    if i != '1' and i != '0':    # 把输入域的0和1过滤掉 因为这两个数字没有任何输出
        numbers.append(int(i))
n = len(numbers)
show_results(numbers, 0, [], n)





