# BestBuy

## This project is meant to work as a simple engine for a fictional tech shop called BestBuy.

This project was built as a training exercise after my first deep dive into OOP programming, Source control and Testing.

Using this program, you can list products and simulate placing an order, via the command line user interface. 

### Objects

#### Product

The Product class represents a specific type of product available in the store. It encapsulates information about the product, including its name and price.

Additionally, the Product class includes an attribute to keep track of the total quantity of items of that product currently available in the store. When someone will purchase it, the amount will be modified accordingly.

#####  Class Specification

| Instance variables | type  |
|--------------------|:-----:|
| Name               |  str  |
| Price              | float |
| Quantity           |  int  |
| Active             | bool  |
| Promotion          | class |

 #### Promotion
Products can have only one promotion at a given time.
The current existing promotions are: 
* Percentage discount
* Second item at half price
* Buy 2, get 1 free

Promotions are implemented in a way that allows us to add promotions to a product instance and remove them. We are also want to be able to add the same promotion to multiple products without repeating code.

#### Store
The store class connects all the instances of Product together, allowing the user to make a purchase of multiple products at once.

The Store class only contains one variable - a list of products that exist in the store. It exposes the following methods:
* add_product(self, product)
* remove_product(self, product) - Removes a product from store.
* get_total_quantity(self) -> int - Returns how many items are in the store in total.
* get_all_products(self) -> List[Product] - Returns all products in the store that are active.
* order(self, shopping_list) -> float - Gets a list of tuples, where each tuple has 2 items:
Product (Product class) and quantity (int).
Buys the products and returns the total price of the order.

## Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository or download the script file:

   ```bash
   git clone https://github.com/inesfolha/BestBuy.git
   
If you downloaded a ZIP archive, extract its contents to a directory of your choice.

2. Change to the script's directory:

 ```bash
   cd main.py
```
3. To run the script, open your terminal and execute the following command:
```bash
python main.py
```

### Usage
[Watch Demo](https://www.youtube.com/watch?v=-f04Epudo7E)

### Limits

* This tool does not have any database or any other kind of storage implemented, so all changes, such as stock changes or any other changes performed while running the program will be lost once you exit the program. 


* Placing the order is also simply a simulation that calculates the order total and reduces the product quantity by the purchased amount, after quiting the program, no order info is saved anywhere. 


* To create new products or promotions, you need to do it directly in the script, there is no functionality implemented to do it through the command line interface. 
