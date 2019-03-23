# data source
# https://www.kaggle.com/mcdonalds/nutrition-facts
import csv
import json

FOOD_CSV = 'menu.csv'
FOOD_JSON = 'food.json'  # copy this output to js/food.js


def get_food_json():
    with open(FOOD_CSV) as f:
        res = {}
        for row in csv.DictReader(f):
            item = row["Item"].split('(')[0].strip()
            size = row["Serving Size"].rstrip(')').replace('(', '/ ')
            key = f'{item} [{size}]'
            res[key] = row["Calories"]
        return json.dumps(res)


def write_json_file(foods=None):
    if foods is None:
        foods = get_food_json()

    with open(FOOD_JSON, 'w') as f:
        f.write(foods)


if __name__ == '__main__':
    write_json_file()
