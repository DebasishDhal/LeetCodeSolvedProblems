'''
Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.
'''
#Initial solution which produced the correct result but suffered from timeout error
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[self.foods.index(food)] = newRating

    def highestRated(self, cuisine: str) -> str:
        max_rating = 0 # Initialize with negative infinity
        max_rated_food = ""
        
        for food, rating, cuisine_temp in zip(self.foods, self.ratings, self.cuisines):
            if cuisine_temp == cuisine and rating >= max_rating:
                if rating==max_rating:
                    max_rating = rating
                    max_rated_food = min(max_rated_food, food)
                else:
                    max_rating = rating
                    max_rated_food = food

        return max_rated_food
      

#Optimized solution, although beats 22% users only. It doesn't use heaps, but sortedlist
from sortedcontainers import SortedList
class FoodRatings:
    
    # from containers import defaultdict

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = {}
        self.cuisine_dict = defaultdict(SortedList) #Sorted list append works by .add method
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_dict[food] = (rating, cuisine)
            self.cuisine_dict[cuisine].add((-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating_or,cuisine = self.food_dict[food]
        print(f"cuisine = {cuisine}, rating_or = {rating_or}, rating_new = {newRating}")
        # print(rating_or,cuisine_or)
        self.food_dict[food] = (newRating,cuisine)
        self.cuisine_dict[cuisine].discard((-rating_or,food))
        self.cuisine_dict[cuisine].add((-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        max_rated_food = self.cuisine_dict[cuisine][0][1]
        return max_rated_food



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
