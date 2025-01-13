import unittest
from main import find_words_in_bounding_box, scale_to_pixel_coordinates, load_words_position_dict

class TestBoundingBoxSearch(unittest.TestCase):

    def setUp(self):
        self.words_position = [
            {"word": "FedEx", "bounding_box": [0.1439, 0.0359, 0.0328, 0.0233]},
            {"word": "Shipping", "bounding_box": [0.3, 0.05, 0.1, 0.04]}
        ]
        self.doc_width = 1263
        self.doc_height = 1644
        self.user_box = [358, 140, 498, 171]

    def test_scale_to_pixel_coordinates(self):
        result = scale_to_pixel_coordinates([0.1439, 0.0359, 0.0328, 0.0233], self.doc_width, self.doc_height)
        expected = (41.45, 38.29, 222.26, 97.25)  # Manually calculated for comparison
        self.assertAlmostEqual(result[0], expected[0], places=1)
    
    def test_find_words_in_bounding_box(self):
        result = find_words_in_bounding_box(self.words_position, self.doc_width, self.doc_height, self.user_box)
        self.assertNotIn("FedEx", result)
        self.assertIn("Shipping", result)

if __name__ == "__main__":
    unittest.main()
