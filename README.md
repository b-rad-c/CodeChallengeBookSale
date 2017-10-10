## Book Store Code Challenge

**The bookstore.py module was created in response to the following code challenge prompt:**

You wish to buy books from a famous bookstore. Usually, all books are sold at the same price, dollars. However, they are planning to have a sale for Halloween next month in which you can buy books at a cheaper rate. Specifically, the first book you buy during the sale will be sold at an initial price of exactly x dollars, but every subsequent book you buy will be sold at a discount of exactly y dollars less than the previous bought book’s cost. This will continue until the cost becomes less than or equal to a floor price of z dollars, after which every book  will cost you z dollars each.

Eg: Every book has an initial price of 50 dollars.
Every subsequent book will be sold at a discount of  4 dollars less. This will continue till cost becomes less than or equal to the floor price of 25 dollars. The price of the books will be then decrease as follows:

50 46 42 38 34 30 26 25 25 25 25 25

Let’s say you have 300 dollars in your budget. How many books can you buy during the sale?
Expected answer : 8 books, $9 remaining


## Usage

### CLI
	$ ./bookstore.py -h
	usage: bookstore.py [-h] initial_price discount floor_price budget

	Find the total number of books that can be purchased at the given discount
	parameters

	positional arguments:
	  initial_price  Initial price of the books
	  discount       Discount applied to each additional purchase
	  floor_price    The lowest discounted price available
	  budget         Find how many books can be purchased given this amount

	optional arguments:
  	-h, --help     show this help message and exit
  	
Example:

	$ ./bookstore.py 50 4 25 300
	8 books purchased with $9.00 remaining
	
### Import
	import bookstore
	bookstore.num_books_in_budget(50, 4, 25, 300)
	# return: (8, 9.0)
	
### Version
Tested in python 2.7 and 3.6