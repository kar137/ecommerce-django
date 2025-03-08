# Django E-commerce Platform

## 📌 Project Overview

This is a full-featured **E-commerce Platform** built using **Django**. It provides a marketplace where users can list products, buy items instantly, communicate with sellers, and make secure payments. The project follows **Django's best practices** and implements core e-commerce functionalities.

## 🚀 Features

### 🔑 User Authentication
- User registration and login using Django's authentication system.
- Password reset functionality via email.
- User profile management (profile picture, address, payment details).

### 🛒 Product Listings & Auctions
- Add, edit, and delete product listings.
- Auction-based bidding system with automatic expiry.
- "Buy Now" option for instant purchases.
- Product categories and filtering.

### 💰 Payment Integration
- Integration with Esewa and Khalti payment gateways.
- Secure checkout process.

### 💬 Messaging System
- Real-time buyer-seller chat using WebSockets (Django Channels).

### ⭐ Order & Review System
- Order history tracking for users.
- Product reviews and ratings.
- Seller reputation system.

### ⚙️ Admin Panel
- Manage users, products, and transactions.
- Moderate reported listings.

## 🏗️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Tailwind
- **Real-time Features:** Django Channels, WebSockets
- **Payments:** Esewa / Khalti
- **Deployment:** AWS / Heroku

## 📂 Installation & Setup

```bash
1️⃣ Clone the Repository
git clone https://github.com/kar137/ecommerce-django.git
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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Contributing

Contributions are welcome! Follow these steps:

- Fork the repository(Don't forget to star)
- Create a new branch (feature-xyz)
- Commit changes & push to GitHub
- Open a Pull Request

## 📬 Contact

For questions or collaborations, reach out via bistakaran89@gmail.com or open an issue.
