#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else

    # conditional statements let you use "a if C else b"
    result = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "one"

if __name__ == "__main__":
    main()
