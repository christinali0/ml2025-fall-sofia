class NumberList:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def search_number(self, x):
        try:
            index = self.numbers.index(x)
            return index + 1
        except ValueError:
            return -1


def main():
    # Step 1: Read N
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("N must be a positive integer. Try again.")
        except ValueError:
            print("Invalid input. Enter a valid integer.")

    # Step 2: Read N numbers
    number_list = NumberList()
    print(f"Enter {N} numbers:")
    for i in range(N):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                number_list.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Enter a valid integer.")

    # Step 3: Read X
    while True:
        try:
            X = int(input("Enter the number X to search for: "))
            break
        except ValueError:
            print("Invalid input. Enter a valid integer.")

    # Step 4: Search for X and print the result
    result = number_list.search_number(X)
    print(result)


if __name__ == "__main__":
    main()
