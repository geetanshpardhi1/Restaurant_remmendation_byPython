import unittest
from unittest.mock import patch
from restaurant_recommendation import restaurant_recommendations

class TestRecommendations(unittest.TestCase):
    def setUp(self):
        # Example user data for testing
        self.user_data = {
            'cuisine': ['chinese', 'indian'],
            'min_rating': 3.5,
            'location': (40.7128, -74.0060),
        }
    
    #test when right input is placed
    def test_recommendations_with_input(self):
        with patch('builtins.input', side_effect=['chinese,indian', '3.5', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertTrue(len(recommended_restaurants) > 0)
    
    #test for no cuisine given by user
    def test_recommendations_no_cuisine_input(self):
        with patch('builtins.input', side_effect=['', '3.5', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertTrue(len(recommended_restaurants) > 0)

    #test for no ratings provided by user
    def test_recommendations_no_rating_input(self):
        with patch('builtins.input', side_effect=['chinese,indian', '', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertTrue(len(recommended_restaurants) > 0)

    #test for no cuisine and no rating provided 
    def test_recommendations_no_cuisine_and_rating_input(self):
        with patch('builtins.input', side_effect=['', '', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertTrue(len(recommended_restaurants) > 0)

    #test for invalid cuisine provided by user
    def test_recommendations_invalid_cuisine_input(self):
        with patch('builtins.input', side_effect=['sushi', '3.5', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertEqual(len(recommended_restaurants), 0)

    
    def test_valid_food_types(self):
        with patch('builtins.input', side_effect=['indian,chinese', '4.0', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertTrue(len(recommended_restaurants) > 0)

    def test_invalid_food_types(self):
        with patch('builtins.input', side_effect=['korean,vietnamese', '4.0', '40.7128', '-74.0060']):
            recommended_restaurants = restaurant_recommendations()
        self.assertIsNotNone(recommended_restaurants)
        self.assertEqual(len(recommended_restaurants), 0)

 

unittest.main()