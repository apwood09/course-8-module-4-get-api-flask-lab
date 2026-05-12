from flask import Flask, jsonify, request, abort
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message

@app.route("/")
def home():
    """return welcome message"""
    return jsonify({"message": "Welcome to the homepage!"})

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    # GET category from ?category=electronics
    category_filter = request.args.get('category')

    if category_filter: 
        # filter by category 
        filtered_products = [p for p in products if p['category'].lower() == category_filter.lower()]
        return jsonify(filtered_products)

    # category not found
    return jsonify(products)

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    # find dict with matching ID
    product = next((p for p in products if p["id"] == id), None)

    if product is None:
        # not found: 404 error
        abort(404, description="Product not found")
    
    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)
