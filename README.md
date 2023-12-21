# E-Commerce API

Welcome to the E-Commerce API, a robust backend solution for managing products, categories, user carts, and more. This API is designed to power your e-commerce platform with essential features.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [API Endpoints](#api-endpoints)
4. [Contributing](#contributing)

## Features
- Manage Products and Product Reviews
- Categories for better organization
- User Cart functionality for a seamless shopping experience
- User Registration and Authentication
- Token-based Authentication for secure API access

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/lebelokamogelo/ecommerce-api.git
    cd ecommerce-api
    ```

2. Create and activate a virtual environment:
```bash
    python -m venv venv
    
    On Windows, you might use: python -m venv venv
    Activate the virtual environment:
    On Windows: .\venv\Scripts\activate
    On Unix or MacOS: source venv/bin/activate
```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```
Ensure the API is running, and you can start making requests to the provided endpoints. The API supports various operations, including product management, category operations, user cart actions, and user authentication.

## API Endpoints
- **Products**
  - `GET /products/`: Retrieve all products
  - `GET /products/<str:pk>/`: Retrieve, Update, or Delete a specific product
  - `GET /products/<str:pk>/reviews/`: Retrieve reviews for a product
  - `GET /products/?category=<str:name>`: Retrieve all products for a specific category
- **Reviews**
  - `GET /reviews/`: Retrieve all reviews
  - `POST /reviews/`: Create a new review
  - `GET /reviews/<int:pk>/`: Retrieve, Update, or Delete a specific review
- **Categories**
  - `GET /category/`: Retrieve all categories
  - `GET /category/<str:name>/`: Retrieve or Update a specific category
- **User Cart**
  - `GET /cart/`: Retrieve the user's cart
  - `POST /cart/`: Add a product to the cart
  - `DELETE /cart/delete/<str:pk>/`: Remove a specific item from the cart
  - `DELETE /cart/delete/`: Remove all items from the cart

## Contributing

Contributions are welcome! Feel free to open issues, create pull requests, or suggest improvements.
