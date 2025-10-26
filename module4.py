def main():
    """Program that reads N numbers, then finds X among them."""

    # Ask for N
    N = int(input("Please enter a positive integer N:\n"))

    # Read N numbers one by one
    numbers = []
    for i in range(1, N + 1):
        num = int(input(f"Please enter number #{i}:\n"))
        numbers.append(num)

    # Ask for X
    X = int(input("Please enter X:\n"))

    # Find X in the list
    if X in numbers:
        index = numbers.index(X) + 1  # +1 for 1-based index
        print(index)
    else:
        print(-1)


# Run the program
if __name__ == "__main__":
    main()
