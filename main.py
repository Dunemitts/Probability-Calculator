def get_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")

def probabilityCalculations(numerator, denominator):
    probability = int(numerator)/int(denominator)
    percentage = probability*100
    print(f"The Probability is {numerator}/{denominator} \nThe Percentage of success is {percentage}%")
    # Print filled squares for the numerator
    for i in range(int(numerator)):
        print("🔳 ", end="") # Symbols: N: 🔳 D: ⬜
    # Print empty squares for the remaining probability
    for i in range(int(numerator), int(denominator)):
        print("⬜ ", end="")
    print("\n---------------------------------------------------------------------------------------------")
    

def main():
    numerator = get_input("Enter the numerator: ")
    denominator = get_input("Enter the denominator: ")
    probabilityCalculations(numerator, denominator)

    while True:
        changeInput = input("Did anything change? Y/N: ").lower()
        if changeInput in ["y", "yes"]:
            probabilityChangeInput = input("What number changed? N/D or B: ").lower()
            if probabilityChangeInput in ["n","numerator"]:
                numerator = get_input("Enter the numerator: ")
                denominator -= 1
            elif probabilityChangeInput in ["d","denominator"]:
                denominator = get_input("Enter the denominator: ")
            elif probabilityChangeInput in ["b","both"]:
                numerator = get_input("Enter the numerator: ")
                denominator = get_input("Enter the denominator: ")
            probabilityCalculations(numerator, denominator)
        else:
            break


if __name__ == "__main__":
    main()