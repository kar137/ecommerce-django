# eBay Clone - Django E-commerce Platform

## 📌 Project Overview

This is a full-featured **eBay Clone** built using **Django**. It provides a marketplace where users can list products, place bids in auctions, buy items instantly, communicate with sellers, and make secure payments. The project follows **Django's best practices** and implements core e-commerce functionalities.

## 🚀 Features

### 🔑 **User Authentication**

✅ User registration & login (Django authentication system)
✅ Password reset feature
✅ User profile management (profile picture, address, payment details)

### 🛒 **Product Listings & Auctions**

✅ Add, edit, and delete product listings
✅ Auction-based bidding system with automatic expiry
✅ "Buy Now" option for instant purchases
✅ Product categories & filtering

### 💰 **Payment Integration**

✅ Esewa/Khalti payment gateways
✅ Secure checkout process

### 💬 **Messaging System**

✅ Buyer-seller chat for direct communication
✅ Real-time messaging with WebSockets (Django Channels)

### ⭐ **Order & Review System**

✅ Order history tracking
✅ Product reviews & ratings
✅ Seller reputation system

### ⚙️ **Admin Panel**

✅ Manage users, products, and transactions
✅ Moderate reported listings

## 🏗️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL / MySQL
- **Frontend:** HTML, CSS, Tailwind
- **Real-time Features:** Django Channels, WebSockets
- **Payments:** Esewa / Khalti
- **Deployment:** AWS / Heroku

## 📂 Installation & Setup

```bash
1️⃣ Clone the Repository
git clone https://github.com/your-username/ebay-clone.git
cd ebay-clone

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database
Set up PostgreSQL or MySQL

Update DATABASES settings in settings.py
5️⃣ Apply Migrations
python manage.py migrate

6️⃣ Run Development Server
python manage.py runserver

```

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Contributing

Contributions are welcome! Follow these steps:

-Fork the repository(Don't forget to star)
-Create a new branch (feature-xyz)
-Commit changes & push to GitHub
-Open a Pull Request

## 📬 Contact

For questions or collaborations, reach out via bistakaran89@gmail.com or open an issue.
