from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_products(count=2000):
    products = []
    brands = ["Apple", "Samsung", "Sony", "Bose", "Dell", "HP", "Lenovo", "Asus", "Nike", "Adidas",
              "Zara", "Gucci", "Prada", "Rolex", "Casio", "Canon", "Nikon", "GoPro", "DJI", "Xiaomi",
              "Microsoft", "Logitech", "Razer", "Corsair", "AMD", "Intel", "NVIDIA", "Tesla", "SpaceX"]

    categories = ["Electronics", "Fashion", "Home & Kitchen", "Sports", "Beauty", "Toys", "Automotive", "Books", "Gaming", "Health"]

    product_types = {
        "Electronics": ["Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch", "Camera", "Drone", "Speaker", "TV", "Monitor"],
        "Fashion": ["Shoes", "T-Shirt", "Jeans", "Jacket", "Watch", "Sunglasses", "Bag", "Hat", "Belt", "Scarf"],
        "Home & Kitchen": ["Mixer", "Toaster", "Blender", "Cooker", "Knife Set", "Dinner Set", "Lamp", "Vacuum", "Fridge", "Microwave"],
        "Sports": ["Shoes", "T-shirt", "Ball", "Racket", "Gloves", "Protector", "Bag", "Bike", "Treadmill", "Dumbbells"],
        "Beauty": ["Perfume", "Cream", "Makeup Kit", "Shampoo", "Oil", "Face Wash", "Trimmer", "Hair Dryer", "Straightener", "Nail Polish"],
        "Toys": ["Action Figure", "Board Game", "Puzzle", "Remote Car", "Drone", "Doll", "LEGO", "Robot", "Video Game", "Stuffed Toy"],
        "Automotive": ["Tyre", "Battery", "Oil", "Cover", "Cleaner", "Light", "Horn", "Seat Cover", "Dash Cam", "GPS"],
        "Books": ["Novel", "Comic", "Magazine", "Biography", "Cookbook", "Dictionary", "Atlas", "Encyclopedia", "Textbook", "Journal"],
        "Gaming": ["Console", "Game", "Controller", "Headset", "Chair", "Mouse", "Keyboard", "Monitor", "Graphics Card", "VR Headset"],
        "Health": ["Fitness Tracker", "Scale", "Massager", "Supplements", "Yoga Mat", "Resistance Bands", "Protein Powder", "Vitamins", "First Aid", "Thermometer"]
    }

    for i in range(count):
        brand = random.choice(brands)
        category = random.choice(categories)
        ptype = random.choice(product_types[category])

        # Realistic pricing based on category
        if category == "Electronics" or category == "Gaming":
            price = round(random.uniform(20, 3500), 2)
        elif category == "Fashion":
            price = round(random.uniform(10, 1200), 2)
        elif category == "Automotive":
            price = round(random.uniform(15, 800), 2)
        else:
            price = round(random.uniform(5, 500), 2)

        rating = round(random.uniform(3.2, 5.0), 1)

        # Demand based on rating
        if rating >= 4.7:
            demand = random.randint(90, 99)
            trending = random.random() > 0.7  # 30% chance
        elif rating >= 4.2:
            demand = random.randint(75, 92)
            trending = random.random() > 0.8  # 20% chance
        elif rating >= 3.8:
            demand = random.randint(60, 80)
            trending = False
        else:
            demand = random.randint(40, 65)
            trending = False

        competition = random.choice(["Low", "Medium", "High"])
        if competition == "Low":
            profit = random.randint(35, 65)
        elif competition == "Medium":
            profit = random.randint(20, 45)
        else:
            profit = random.randint(8, 28)

        # High margin product (profit > 40%)
        high_margin = profit > 40

        # Generate realistic name
        if i % 5 == 0:
            name = f"{brand} {ptype} {random.choice(['Elite', 'Premium', 'Luxury', 'Pro Max', 'Ultra'])} {random.randint(100, 9999)}"
        else:
            name = f"{brand} {ptype} {random.choice(['Pro', 'Max', 'Plus', 'Lite', 'Core'])} {random.randint(100, 999)}"

        products.append({
            "id": i,
            "name": name,
            "price": f"${price:.2f}",
            "rating": rating,
            "demand": f"{demand}%",
            "profit": f"{profit}%",
            "competition": competition,
            "category": category,
            "trending": trending,
            "high_margin": high_margin
        })

    # Shuffle to make it realistic
    random.shuffle(products)
    return products

# Generate products once at startup (for performance)
PRODUCTS = generate_products(2000)

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

@app.route('/api/products')
def api_products():
    """API endpoint for dynamic filtering"""
    category = request.args.get('category', 'all')
    min_profit = request.args.get('min_profit', 0, type=int)
    trending_only = request.args.get('trending', 'false') == 'true'
    high_margin_only = request.args.get('high_margin', 'false') == 'true'

    filtered = PRODUCTS
    if category != 'all':
        filtered = [p for p in filtered if p['category'] == category]
    if min_profit > 0:
        filtered = [p for p in filtered if int(p['profit'][:-1]) >= min_profit]
    if trending_only:
        filtered = [p for p in filtered if p['trending']]
    if high_margin_only:
        filtered = [p for p in filtered if p['high_margin']]

    return jsonify(filtered[:100])  # Return max 100 for performance

if __name__ == '__main__':
    app.run()
