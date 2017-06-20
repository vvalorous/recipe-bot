"""
This is the test suite for methods related to querying the Yummly API.
"""
import unittest
from recipe_bot import get_search_results, create_payload

"""
Test methods related to creating dictionary of query parameters as payload
"""
class TestPayloadCreation(unittest.TestCase):

	# Test creating basic request parameters as payload:
	def test_create_basic_payload(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
		}
		payload = create_payload('onion soup')
		self.assertEqual(expected_payload, payload)

	# Test creating payload with optional allergy parameter
	def test_optional_allergy_parameter(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
			'allowedAllergy[]': 'Gluten-Free',
		}
		allergy = "Gluten-Free"
		payload = create_payload('onion soup', allergy=allergy)
		self.assertEqual(expected_payload, payload)

	# Test creating payload with optional time parameter
	def test_optional_time_parameter(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
			'maxTotalTimeInSeconds': '5400',
		}
		time = '5400'
		payload = create_payload('onion soup', time=time)
		self.assertEqual(expected_payload, payload)

	# Test creating payload with multiple optional parameters
	def test_multiple_optional_parameters(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
			'allowedAllergy[]': 'Gluten-Free',
			'maxTotalTimeInSeconds': '5400',
		}
		allergy = "Gluten-Free"
		time = '5400'
		payload = create_payload('onion soup', allergy=allergy, time=time)
		self.assertEqual(expected_payload, payload)

	# Test creating payload with multiple allergy parameters
	def test_multiple_allergy_parameters(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
			'allowedAllergy[]': ['Gluten-Free', 'Seafood-Free'],
		}
		allergy = ['Gluten-Free', 'Seafood-Free']
		payload = create_payload('onion soup', allergy=allergy)
		self.assertEqual(expected_payload, payload)

	# Test creating payload with excluded ingredient parameter
	def test_excluded_ingredient_parameter(self):
		expected_payload = {
			'q': 'onion soup',
			'maxResult': '1',
			'excludedIngredient[]': 'thyme',
		}
		excluded_ingredient = 'thyme'
		payload = create_payload('onion soup', excluded_ingredient=excluded_ingredient)
		self.assertEqual(expected_payload, payload)



"""
Test methods related to checking for successful search queries in API
"""
class TestSearchSuccess(unittest.TestCase):

	# Test simple search for onion soup
	def test_simple_search_api(self):
		expected_simple_result = 200
		simple_search_term = "onion soup"
		simple_response = get_search_results(simple_search_term)
		self.assertEqual(expected_simple_result, simple_response.status_code)

	# Test search with allergy parameter
	def test_allergy_search_api(self):
		expected_allergy_result = 200
		allergy_search_term = "onion soup"
		allergy = "Gluten-Free"
		allergy_response = get_search_results(allergy_search_term, allergy=allergy)
		self.assertEqual(expected_allergy_result, allergy_response.status_code)

	# Test search with time parameter
	def test_time_search_api(self):
		expected_time_result = 200
		time_search_term = "onion soup"
		time = "5400"
		time_response = get_search_results(time_search_term, time=time)
		self.assertEqual(expected_time_result, time_response.status_code)

	# Test search with multiple optional parameters
	def test_multiple_search_api(self):
		expected_multiple_result = 200
		multiple_search_term = "onion soup"
		allergy = "Gluten-Free"
		time = "5400"
		multiple_response = get_search_results(multiple_search_term, allergy=allergy, time=time)
		self.assertEqual(expected_multiple_result, multiple_response.status_code)

	# Test search with multiple values for an optional parameter
	def test_multiple_allergy_search_api(self):
		expected_multiple_allergy_result = 200
		multiple_allergy_search_term = "onion soup"
		multiple_allergy = ["Gluten-Free", 'Seafood-Free']
		multiple_allergy_response = get_search_results(multiple_allergy_search_term, allergy=multiple_allergy)
		self.assertEqual(expected_multiple_allergy_result, multiple_allergy_response.status_code)

	# Test search returns single recipe
	def test_single_recipe_return(self):
		single_recipe_response = get_search_results("onion soup")
		response = single_recipe_response.json()
		self.assertEqual(1, len(response['matches']))

	
	# Test parsing search results and returning highest rated query

if __name__ == '__main__':
	unittest.main()