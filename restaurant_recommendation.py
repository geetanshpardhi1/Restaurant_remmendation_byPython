from geopy.distance import geodesic
#used geopy for geological computations

#used list of dictionary for better efficiency
restaurant_data = [
    {"name": "Chings chinese", "cuisine": "Chinese", "rating": 4.1, "location": (40.7128, -74.0060)},
    {"name": "Chinese Paradise", "cuisine": "Chinese", "rating": 3.4, "location": (40.7309, -73.9872)},
    {"name": "China-town", "cuisine": "Chinese", "rating": 3.0, "location": (40.7397, -74.0028)},
    {"name": "Radission", "cuisine": "Indian", "rating": 4.0, "location": (34.0522, -118.2437)},
    {"name": "Royal rasoi", "cuisine": "Indian", "rating": 4.3, "location": (34.0522, -118.2653)},
    {"name": "Guru kripa", "cuisine": "Indian", "rating": 4.1, "location": (34.0522, -118.2780)},
    {"name": "Sushi center", "cuisine": "Japanese", "rating": 4.6, "location": (35.6895, 139.6917)},
    {"name": "Ramen house", "cuisine": "Japanese", "rating": 4.4, "location": (35.6895, 139.6917)},
    {"name": "Uzumaki's Choice", "cuisine": "Japanese", "rating": 4.7, "location": (35.6895, 139.6917)},
]

#used this function to calculate proximity score for better sorting of restaurants
def calculate_proximity_score(user_location, restaurant_location):
    return geodesic(user_location, restaurant_location).kilometers


def restaurant_recommendations():
    
    cuisine_preferences_input = input("Enter your preferred cuisines (comma-separated,or press Enter for any): ")
    cuisine_preferences = cuisine_preferences_input.lower().split(',') if cuisine_preferences_input else []

    min_rating_input = input("Enter the minimum rating you prefer(press Enter for any): ")
    try:
        min_rating = float(min_rating_input) if min_rating_input else 0.0
    except ValueError:
        print("Invalid rating input. Please enter a valid numerical value or press Enter for any.")
        return [] #returns empty list so that program exits

    #setting user preference 
    user_preferences = {
        'cuisine': [c.strip() for c in cuisine_preferences],
        'min_rating': min_rating
    }

    
    user_latitude_input = input("Enter your latitude: ")
    user_longitude_input = input("Enter your longitude: ")

    try:
        user_latitude = float(user_latitude_input)
        user_longitude = float(user_longitude_input)
    except ValueError:
        print("Invalid latitude or longitude input. Please enter valid numerical values.")
        return [] #returns empty list so that program exits

    user_location = (user_latitude, user_longitude)

    # Filterd restautants according to user preferences
    filtered_restaurants = [
        restaurant for restaurant in restaurant_data if
        (not user_preferences['cuisine'] or restaurant['cuisine'].lower() in user_preferences['cuisine']) and
        (not user_preferences['min_rating'] or restaurant['rating'] >= user_preferences['min_rating'])
    ]

    #if no restaurant meet preferences it exits
    if not filtered_restaurants:
        print("Sorry, no restaurants match your criteria.")
        return []

    #Calculate proximity score of each filtered restaurant
    for restaurant in filtered_restaurants:
        restaurant['proximity_score'] = calculate_proximity_score(user_location, restaurant['location'])

    #last and final step sortin of restaurants according to ratings and proximity
    recommended_restaurants = sorted(
        filtered_restaurants,
        key=lambda x: (x['rating'], x['proximity_score']),
        reverse=True
    )

    return recommended_restaurants[:5]  #Return the top 5 restaurants





recommended_restaurants = restaurant_recommendations()

#Display recommended restaurants
if recommended_restaurants:
    print("\nRecommended Restaurants:")
    for restaurant in recommended_restaurants:
        print(f"{restaurant['name']} - Cuisine: {restaurant['cuisine']}, Rating: {restaurant['rating']}, Proximity: {restaurant['proximity_score']:.2f} kilometers")
