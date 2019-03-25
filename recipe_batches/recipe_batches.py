#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch = {}
    for k, v in recipe.items():
        if k not in ingredients:
            return 0
        batch[k] = ingredients[k] // v
    return min(batch.values())


print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
      'milk': 198, 'butter': 52, 'cheese': 10}))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
