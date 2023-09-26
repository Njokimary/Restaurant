
                        Restaurant Review System

The system allows you to manage customers, restaurants, and reviews. Below are the key deliverables and methods for each class:

Customer
Initializer: Customer __init__(given_name: str, family_name: str)

Initialize a customer with a given name and family name (first and last name).
Readers:

given_name() -> str: Returns the customer's given name.
family_name() -> str: Returns the customer's family name.
full_name() -> str: Returns the full name of the customer (given name and family name concatenated).
Writers:

given_name(): Can change after the customer is created.
family_name(): Can change after the customer is created.
all() -> List[Customer]: Returns all customer instances.

restaurants() -> List[Restaurant]: Returns a unique list of all restaurants a customer has reviewed.

add_review(restaurant: Restaurant, rating: int): Creates a new review and associates it with the customer and restaurant.

num_reviews() -> int: Returns the total number of reviews authored by the customer.

Class Methods:

find_by_name(name: str) -> Optional[Customer]: Returns the first customer whose full name matches the given string.
find_all_by_given_name(name: str) -> List[Customer]: Returns a list containing all customers with the given name.
Restaurant
Initializer: Restaurant __init__(name: str)

Initialize a restaurant with a name as a string.
Readers:

name() -> str: Returns the restaurant's name.
reviews() -> List[Review]: Returns a list of all reviews for that restaurant.

customers() -> List[Customer]: Returns a unique list of all customers who have reviewed a particular restaurant.

average_star_rating() -> float: Returns the average star rating for a restaurant based on its reviews. Calculation: Sum of ratings divided by the number of ratings.

Review
Initializer: Review __init__(customer: Customer, restaurant: Restaurant, rating: int)

Initialize a review with a customer, restaurant, and a rating (a number).
Readers:

rating() -> int: Returns the rating for a restaurant.
all() -> List[Review]: Returns all reviews.

customer() -> Customer: Returns the customer object for that review.

restaurant() -> Restaurant: Returns the restaurant object for that given review.

