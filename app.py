from flask import Flask, render_template
import random

app = Flask(__name__)

def generate_products(count=1500):
    products = []
    brands = ["Apple", "Samsung", "Sony", "Bose", "Dell", "HP", "Lenovo", "Asus", "Nike", "Adidas", 
              "Zara", "Gucci", "Prada", "Rolex", "Casio", "Canon", "Nikon", "GoPro", "DJI", "Xiaomi"]
    
    categories = ["Electronics", "Fashion", "Home & Kitchen", "Sports", "Beauty", "Toys", "Automotive", "Books"]
    
    product_types = {
        "Electronics": ["Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch", "Camera", "Drone", "Speaker"],
        "Fashion": ["Shoes", "T-Shirt", "Jeans", "Jacket", "Watch", "Sunglasses", "Bag", "Hat"],
        "Home & Kitchen": ["Mixer", "Toaster", "Blender", "Cooker", "Knife Set", "Dinner Set", "Lamp"],
        "Sports": ["Shoes", "T-shirt", "Ball", "Racket", "Gloves", "Protector", "Bag"],
        "Beauty": ["Perfume", "Cream", "Makeup Kit", "Shampoo", "Oil", "Face Wash", "Trimmer"],
        "Toys": ["Action Figure", "Board Game", "Puzzle", "Remote Car", "Drone", "Doll", "LEGO"],
        "Automotive": ["Tyre", "Battery", "Oil", "Cover", "Cleaner", "Light", "Horn"],
        "Books": ["Novel", "Comic", "Magazine", "Biography", "Cookbook", "Dictionary"]
    }
    
    for i in range(count):
        brand = random.choice(brands)
        category = random.choice(categories)
        ptype = random.choice(product_types[category])
        
        # Realistic pricing based on category
        if category == "Electronics":
            price = round(random.uniform(20, 2500), 2)
        elif category == "Fashion":
            price = round(random.uniform(15, 800), 2)
        elif category == "Automotive":
            price = round(random.uniform(25, 500), 2)
        else:
            price = round(random.uniform(10, 400), 2)
        
        rating = round(random.uniform(3.5, 5.0), 1)
        
        # Demand based on rating
        if rating >= 4.5:
            demand = random.randint(80, 98)
        elif rating >= 4.0:
            demand = random.randint(65, 85)
        else:
            demand = random.randint(45, 70)
        
        competition = random.choice(["Low", "Medium", "High"])
        if competition == "Low":
            profit = random.randint(35, 60)
        elif competition == "Medium":
            profit = random.randint(20, 40)
        else:
            profit = random.randint(10, 25)
        
        products.append({
            "name": f"{brand} {ptype} {random.choice(['Pro', 'Max', 'Ultra', 'Plus', 'Elite'])} {random.randint(100, 999)}",
            "price": f"${price:.2f}",
            "rating": rating,
            "demand": f"{demand}%",
            "profit": f"{profit}%",
            "competition": competition,
            "category": category
        })
    return products

@app.route('/')
def home():
    products = generate_products(1500)
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run()
