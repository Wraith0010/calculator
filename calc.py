while True:
    print ("\033[1;35;48m      +     \n")
    print ("\033[1;31;48m     - -     \n")
    print ("\033[1;32;48m    *   *     \n")
    print ("\033[1;36;48m   /      \     \n")
    print ("\033[1;34;48m  **      **     \n")
    print ("\033[1;34;48m ~~~~~~~~~~~~~    \n")

    choose = input("\033[1;37;48m choose +,-,*,/,** \n")
    choose1 = input("choose int or float ")

    total = None

    if choose1 == "int":
        if choose == "+":
            num1 = int(input("\033[1;35;48m choose first number: \n"))
            num2 = int(input("choose second number: "))
            total = num1 + num2
        elif choose == "-":
            num1 = int(input("\033[1;31;48m choose first number: \n"))
            num2 = int(input("choose second number: "))
            total = num1 - num2
        elif choose == "*":
            num1 = int(input("\033[1;32;48m choose first number: \n"))
            num2 = int(input("choose second number: "))
            total = num1 * num2
        elif choose == "/":
            num1 = int(input("\033[1;36;48m choose first number: \n"))
            num2 = int(input("choose second number: "))
            total = num1 / num2
        elif choose == "**":
            num1 = int(input("\033[1;34;48m choose first number: \n"))
            num2 = int(input("choose second number: "))
            total = num1 ** num2
    elif choose1 == "float":
        if choose == "+":
            num1 = float(input("\033[1;35;48m choose first number: \n"))
            num2 = float(input("choose second number: "))
            total = num1 + num2
        elif choose == "-":
            num1 = float(input("\033[1;31;48m choose first number: \n"))
            num2 = float(input("choose second number: "))
            total = num1 - num2
        elif choose == "*":
            num1 = float(input("\033[1;32;48m choose first number: \n"))
            num2 = float(input("choose second number: "))
            total = num1 * num2
        elif choose == "/":
            num1 = float(input("\033[1;36;48m choose first number: \n"))
            num2 = float(input("choose second number: "))
            total = num1 / num2
        elif choose == "**":
            num1 = float(input("\033[1;34;48m choose first number: \n"))
            num2 = float(input("choose second number: "))
            total = num1 ** num2

    if total is not None:
        if total == 44:
            print("\033[1;32;48m 101100 \n")
        elif total == 111:
            print("\033[1;32;48m 1101111 \n")
        else:
            print(f"Your answer is {total}")
    else:
        print("Error")
    
    input("\nPress Enter to restart...\n")
