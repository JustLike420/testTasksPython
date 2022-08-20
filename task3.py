def main(order):
    for el in order:
        if el != '(' and el != ')':
            return False
    return True


if __name__ == "__main__":
    print(main('(((()((*&(*)'))  # False
    print(main('((()))()('))  # True
