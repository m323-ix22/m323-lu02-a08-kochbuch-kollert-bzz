"""Let him cook"""
import json


def adjust_recipe(recipe, persons):
    new_ingredients = {}
    difference = persons / recipe['servings']
    for ingredients, amount in recipe['ingredients'].items():
        new_ingredients[ingredients] = amount * difference
    new_recipe = {
        'title': recipe['title'],
        'ingredients': new_ingredients,
        'servings': persons
    }
    return new_recipe


def load_recipe(json_recipe):
    return json.loads(json_recipe)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    python_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(python_recipe, 2)
    print(f'new:\n{adjusted_recipe}')
    print(f'old:\n{python_recipe}')
