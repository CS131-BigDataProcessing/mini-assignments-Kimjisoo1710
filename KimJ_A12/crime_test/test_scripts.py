import unittest
import pandas as pd
from validate_functions import validate
from stats_function import calculate_mean, calculate_median

class CrimeTest(unittest.TestCase):

    def setUp(self):
        # Set up a valid DataFrame with different values
        self.df = pd.DataFrame({
            'Vict sex': ['F', 'M', 'F', 'M', 'M'],
            'Vict age': [22, 45, 37, 33, 50]
        })

    def test_valid_sex_column(self):
        # Test with all valid values for 'Vict sex'
        self.assertTrue(validate(self.df))

    def test_invalid_sex_column(self):
        invalid_df = self.df.copy()
        # Introduce invalid values for 'Vict sex'
        invalid_df['Vict sex'] = ['A', 'M', 'M', None, 'F']
        self.assertFalse(validate(invalid_df))
        # More invalid cases
        invalid_df['Vict sex'] = [None, 'Z', 'X', 'M', 'F']
        self.assertFalse(validate(invalid_df))

    def test_valid_age_column(self):
        # Test with all valid values for 'Vict age'
        self.assertTrue(validate(self.df))

    def test_invalid_age_column(self):
        invalid_df = self.df.copy()
        # Introduce negative values for 'Vict age'
        invalid_df['Vict age'] = [22, -10, 30, 100, 45]
        self.assertFalse(validate(invalid_df))
        # Out-of-range values
        invalid_df['Vict age'] = [101, 20, 50, 70, 80]
        self.assertFalse(validate(invalid_df))
        # Null values
        invalid_df['Vict age'] = [22, 45, None, 35, 50]
        self.assertFalse(validate(invalid_df))

    def test_average_age(self):
        # Test the mean age calculation
        expected_mean = 37.4  # Adjusted based on new data
        self.assertAlmostEqual(calculate_mean(self.df), expected_mean, places=1)

    def test_median_age(self):
        # Test the median age calculation
        expected_median = 37
        self.assertEqual(calculate_median(self.df), expected_median)

    def test_empty_dataframe(self):
        # Test edge case with an empty DataFrame
        empty_df = pd.DataFrame({'Vict sex': [], 'Vict age': []})
        self.assertTrue(pd.isna(calculate_mean(empty_df)))
        self.assertTrue(pd.isna(calculate_median(empty_df)))


if __name__ == '__main__':
    unittest.main()

