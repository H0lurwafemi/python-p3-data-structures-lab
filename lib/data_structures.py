spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


new_spicy_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 7,
}

# Function Definition
def get_names(spicy_foods):
    names = []  
    for food in spicy_foods:
        names.append(food["name"])  
    return names

# Function Call
get_names(spicy_foods)



# Function Definition
def get_spiciest_foods(spicy_foods):
    spiciest_foods = []  
    for food in spicy_foods:
        if food["heat_level"] > 5:  
            spiciest_foods.append(food) 
    return spiciest_foods

# Function Call
get_spiciest_foods(spicy_foods)


# Function Definition
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# Function Call
print_spicy_foods(spicy_foods)
# Output:


# Function Definition
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:  
            return food

# Function Calls
get_spicy_food_by_cuisine(spicy_foods, "American")


get_spicy_food_by_cuisine(spicy_foods, "Thai")



# Function Definition
def print_spiciest_foods(spicy_foods):
    spicy_foods = get_spiciest_foods(spicy_foods)  # Use the previously defined function
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

# Function Call
print_spiciest_foods(spicy_foods)
# Output:




# Function Definition
def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]  # Sum up heat levels
    average_heat = total_heat / len(spicy_foods)  # Calculate average
    return int(average_heat)  # Return as an integer

# Function Call
get_average_heat_level(spicy_foods)
# Output: 6


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)  # Add the new spicy_food dictionary to the spicy_foods list
    return spicy_foods  # Return the updated list of spicy_foods