def main(input):
    input_string = input.lower()
    if len(input_string) == 0:
        print('String must be more then 0 chars')
    else:
        data = {}
        for l in input_string:
            if l in data.keys():
                data[l] += 1
            else:
                data[l] = 1
        max_char = input_string[0]
        for k, v in data.items():
            if v > data[max_char]:
                max_char = k
        return (max_char, data[max_char])


if __name__ == '__main__':
    print(main('aaaAAAbc'))  # ('a', 6)
