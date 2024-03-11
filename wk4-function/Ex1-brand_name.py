# # brand name generator basic Concat:

# print("Welcome to the band name generator.")

# city = input("Which city did you grow up in? \n")
# pet = input("What is the name of your pet? \n")
# # print("Your band name coud be " + city.capitalize() + " " + pet.capitalize())
# print(f"Your band name coud be {city.capitalize()} {pet.capitalize()}")
# ----------------------------------------------------------------------------------------------


def generate_brand_name():
    print("Let's create a unique brand name!")
    industry = input("What industry is your brand in? ")
    product = input("What is your main product or service? ")
    adjective = input("The most exiciting/elegant way when thinking of your brand: ")

    brand_name = (
        f"{adjective.capitalize()} {product.capitalize()} {industry.capitalize()}"
    )
    return brand_name


brand_name = generate_brand_name()
print("Your brand name is:", brand_name)

# ----------------------------------------------------------------------------------------------

# import random


# def generate_brand_name_list():
#     industries = ["Tech", "Fashion", "Food", "Health", "Travel"]
#     products = ["Solutions", "Style", "Bites", "Wellness", "Voyage"]
#     adjectives = ["Innovative", "Elegant", "Delicious", "Holistic", "Adventurous"]

#     industry = random.choice(industries)
#     product = random.choice(products)
#     adjective = random.choice(adjectives)

#     brand_name = f"{adjective} {product} {industry}"
#     return brand_name


# # Example usage:
# brand_name = generate_brand_name_list()
# print("Your brand name is:", brand_name)
