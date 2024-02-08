# Cafe App

Welcome to the Cafe App! This application allows you to manage your cafe's products, couriers, orders, and customers.

#### Table of Contents

1. Overview
2. Installation
3. Usage
4. Project Completion
5. Future Plans

---

#### Overview

This Cafe App is designed to streamline cafe management tasks such as adding new products to the menu, managing couriers for deliveries, tracking customer orders, and maintaining customer information.

The application connects to a MySQL database to store and retrieve data related to products, couriers, orders, and customers. It provides a user-friendly interface to perform various operations such as viewing, adding, updating, and deleting records.

---

#### Installation

To run the Cafe App locally, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

   ```
   git clone https://github.com/your-username/cafe-app.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using the following command:

   ```
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**: Create a MySQL database and update the database configuration details in the `app.py` file:

   ```python
   connection = pymysql.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="cafe_database"
   )
   ```

4. **Run the Application**: Execute the `app.py` file to start the Cafe App:

   ```
   python app.py
   ```

5. **Access the App**: Open your web browser and navigate to `http://localhost:5000` to access the Cafe App.

---

#### Usage

1. **Main Menu Options**

   - **Exit App**: Exit the Cafe App.
   - **Product Menu**: Access options related to managing products.
   - **Courier Menu**: Access options related to managing couriers.
   - **Order Menu**: Access options related to managing orders.
   - **Customer Menu**: Access options related to managing customers.

2. **Product Menu Options**

   - **Display Product Catalogue**: View all products in the catalogue.
   - **Create Product**: Add a new product to the catalogue.
   - **Update Product**: Update details of an existing product.
   - **Delete Product**: Remove a product from the catalogue.

3. **Courier Menu Options**

   - **Display Courier Catalogue**: View all couriers in the catalogue.
   - **Create Courier**: Add a new courier to the catalogue.
   - **Update Courier**: Update details of an existing courier.
   - **Delete Courier**: Remove a courier from the catalogue.

4. **Order Menu Options**

   - **Display Order Catalogue**: View all orders in the catalogue.
   - **Create Order**: Place a new order.
   - **View Order Status Table**: View the order status table.
   - **Update Order Status**: Update the status of an existing order.
   - **Update Order**: Update details of an existing order.
   - **Delete Order**: Remove an order from the catalogue.

5. **Customer Menu Options**

   - **Display Customer Catalogue**: View all customers in the catalogue.
   - **Create Customer**: Add a new customer to the catalogue.
   - **Update Customer**: Update details of an existing customer.
   - **Delete Customer**: Remove a customer from the catalogue.

---
#### Project Completion

The Cafe App is fully functional according to the specified user stories. It allows users to manage products, couriers, orders, and customers efficiently. However, there is room for improvement and future enhancements.

---
#### Future Plans

- Implement authentication and authorization for secure access to the application.
- Enhance user interface with better error handling and validation.
- Add functionality for generating reports and analytics.
- Integrate with external services for payment processing and delivery tracking.
- Improve database schema for better data organization and scalability.
