import unittest
import pandas as pd
from src.retail_validation import validate_retail_data


class RetailValidationTests(unittest.TestCase):
    def setUp(self):
        self.cols = dict(product_id="product_id", price="price", inventory="inventory", transaction_id="transaction_id")

    def test_retail_sample_flags_all_expected_rules(self):
        df = pd.read_csv("sample_files/sample_retail_data.csv")
        original = df.copy(deep=True)
        issues = validate_retail_data(df, self.cols)
        self.assertEqual(len(issues), 6)
        self.assertEqual(issues["rule"].value_counts().to_dict(), {
            "invalid_inventory": 2, "invalid_price": 2,
            "missing_product_id": 1, "duplicate_transaction_id": 1,
        })
        pd.testing.assert_frame_equal(df, original)

    def test_clean_data(self):
        df = pd.DataFrame({"product_id": ["A", "B"], "price": [0, "1,200"],
                           "inventory": [0, "5"], "transaction_id": ["T1", "T2"]})
        self.assertTrue(validate_retail_data(df, self.cols).empty)

    def test_blank_and_decimal_handling(self):
        df = pd.DataFrame({"product_id": [" ", "TBD"], "price": [" ", -1],
                           "inventory": [None, 2.5], "transaction_id": [None, None]})
        issues = validate_retail_data(df, self.cols)
        self.assertEqual(len(issues), 6)
        self.assertFalse((issues["rule"] == "duplicate_transaction_id").any())

    def test_missing_column_mapping_raises(self):
        with self.assertRaises(ValueError):
            validate_retail_data(pd.DataFrame({"price": [1]}), {"price": "other"})

    def test_skipped_rules(self):
        df = pd.DataFrame({"price": [-5]})
        issues = validate_retail_data(df, {"price": "price", "inventory": None})
        self.assertEqual(issues["rule"].tolist(), ["invalid_price"])


if __name__ == "__main__":
    unittest.main()
