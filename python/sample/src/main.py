import classes.calc

def main():
    ariOpeObj = classes.calc.arithmeticOperations()
    add_num1 = 12
    add_num2 = 18
    add_result = ariOpeObj.addition(add_num1, add_num2)
    print(add_result)

if __name__ == '__main__':
    main()