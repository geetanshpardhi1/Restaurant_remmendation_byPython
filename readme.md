# Restaurant Recommendation System

## Overview

The Restaurant Recommendation System is a Python application that suggests restaurants based on user preferences, ratings of restaurants, and their proximity to the user's location. The system takes into account the user's preferred cuisines, minimum rating criteria, and geographical location to provide personalized recommendations.

## Features

- **User Input:**
  - Users can input their preferred cuisines (comma-separated) or leave it empty for any cuisine.
  - Users can specify a minimum rating for the recommended restaurants.

- **Location-based Recommendations:**
  - The system calculates proximity scores for each restaurant based on the user's provided latitude and longitude.

- **Sorting and Display:**
  - The recommended restaurants are sorted based on a combination of rating and proximity scores.
  - The top 5 recommendations are displayed to the user.

## Dependencies

- Python 3.x
- [geopy](https://pypi.org/project/geopy/): Used for geocoding and distance calculations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/geetanshpardhi1/Restaurant_remmendation_byPython.git
   ```

2. Install the required dependencies:

   ```bash
   pip install geopy
   ```

3. Run the application:

   ```bash
   python restaurant_recommendation.py
   ```

## Usage

1. Run the application.
2. Enter your preferences when prompted:
   - Preferred cuisines (comma-separated) or press Enter for any.
   - Minimum rating or press Enter for any.
   - Latitude and longitude of your location.
3. Receive personalized restaurant recommendations.

## Example

```plaintext
Enter your preferred cuisines (comma-separated, or press Enter for any): Indian,Chinese
Enter the minimum rating you prefer (press Enter for any): 4.0
Enter your latitude: 40.7128
Enter your longitude: -74.0060

Recommended Restaurants:
1. Restaurant A - Cuisine: Indian, Rating: 4.5, Proximity: 2.31 kilometers
2. Restaurant B - Cuisine: Chinese, Rating: 4.0, Proximity: 8.77 kilometers
3. ...

```
