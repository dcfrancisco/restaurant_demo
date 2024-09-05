from models.restaurant import Restaurant

restaurants = []


def find_all():
    return restaurants


def find_by_id(restaurant_id: str):
    return next((r for r in restaurants if r.id == restaurant_id), None)


def save(restaurant: Restaurant):
    restaurants.append(restaurant)
    return restaurant


def delete_by_id(restaurant_id: str):
    global restaurants
    restaurants = [r for r in restaurants if r.id != restaurant_id]


def exists_by_id(restaurant_id: str):
    return any(r.id == restaurant_id for r in restaurants)
