import unittest
import temperature_tracker


class TestTempTracker(unittest.TestCase):
    tracker = temperature_tracker.TempTracker()
    test_input = [24, 55, 66.5, 87, 30, 95.5]
    for i in test_input:
            temperature = float(i)
            tracker.insert(temperature)

    def test_min_pass(self):
        self.assertEqual(self.tracker.get_min(), 24.00)

    def test_min_fail(self):
        self.assertEqual(self.tracker.get_min(), 87.00)

    def test_max_pass(self):
        self.assertEqual(self.tracker.get_max(), 95.50)

    def test_max_fail(self):
        self.assertEqual(self.tracker.get_max(), 55.00)

    def test_mean_pass(self):
        self.assertEqual(self.tracker.get_mean(), 60.00)

    def test_mean_fail(self):
        self.assertEqual(self.tracker.get_mean(), 55.00)

if __name__ == "__main__":
    unittest.main()
