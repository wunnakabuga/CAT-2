import requests
import json

BASE_URL = 'http://127.0.0.1:8000/products'

def add_product(name, description, price):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Error:", response.json())

def get_all_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", json.dumps(response.json(), indent=4))
    else:
        print("Error:", response.json())

if __name__ == '__main__':
    add_product("Laptop", "A high-performance laptop", 999.99)
    get_all_products()
if __name__ == "__main__":
    # Example usage of the add_product function
    add_product("Laptop", "High-performance laptop", 1200.00)
add_product("Phone", "Latest smartphone with great features", 800.00)


