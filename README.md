# REST API for Product Management

This project demonstrates a simple REST API for managing products, built using Python's `http.server` module. 

## Features
- **GET /products**: Retrieve all products.
- **POST /products**: Add a new product (requires `name`, `description`, `price`).
- **DELETE /products/<product_name>**: Delete a product by name.

## Setup Instructions
1. Clone the repository and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
