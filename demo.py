print("Hello World")

## comments
# dit gewoon stuk tekst

"""
This is multi-
line comment field
dus hier meer tekst
"""
## variables
name = "Kevin"
print(name)

## data types (bool, int, float, string)
b = False
i = 1
f = 0.42
s = "Your Name Here!"

## libraries :
import datetime

## define main function:
# def main() :
#     timeNow = datetime.datetime.now()
#     print(timeNow)

# if __name__ == "__main__":
#     main()

## error handling
def main() :
    try:
        if b == True: # if b: 
            div = 10 / i
            print(div)
        else:
            raise Exception("Boolean not TRUE!")

        return 0 # succes!

    except Exception as e:
        print(f"Error encountered: {str(e)}")
        return 1 # failure!

    finally:
        print("Do some final clean up")
        # like close API connections etc.

if __name__ == "__main__":
    main()




































## Open file and read line by line with for loop:
# with open("data/inputData.txt", "r") as inputFile:
#     for line in inputFile:
#         print(line.strip())

## Lists:
# list = ["Kevin", "Apple", 3]
# print(list[0]) # zero-based counting in lists!
# for item in list:
#     print(item)

## Dicts: Key : Value pairs
# user = {
#     "name": "Kevin",
#     "email": "kevin@example.com"
# }
# print(user["email"])

## JSON / TOML files are basically Dicts with Lists inside them