def mathematical_operation(left:int, operator:str, right:int) -> None | int:
    match operator:
        case '+':
            return left + right
        case '-':
            return left - right
        case '*':
            return left * right
        case _:
            print("Only '+', '-' , '*' operations available.")
            return None


def main():
    expression = input().split(" ")
    left, operator, right = expression

    result = mathematical_operation(int(left), operator, int(right))
    print(result)


if __name__ == '__main__':
    main()