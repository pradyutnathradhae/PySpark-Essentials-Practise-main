#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1
print("Hey! Your friend Band Name Generator this side.")
print("Please input below things")
city_name = input("What's the city you born in?\n")
pet_name = input("Enter the Pet's name\n")
alphabet_to_letters = {
    0:"Empty",
    1:"Oneth",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    10:"Deca"
}
brand_name = "The {} {}".format(alphabet_to_letters[len(city_name)] if len(city_name)<=10 else "Dazzling",pet_name)

print("Your Brand name could be: \n"+brand_name)
