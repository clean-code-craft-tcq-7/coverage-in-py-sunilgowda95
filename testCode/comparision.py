def test(self):
    import comparison
    self.assertTrue(comparison.check_greater(2,1))
    self.assertFalse(comparison.check_greater(2,2))
    self.assertFalse(comparison.check_greater(1,2))
    self.assertTrue(comparison.check_lesser(1,2))
    self.assertFalse(comparison.check_lesser(2,2))
    self.assertFalse(comparison.check_lesser(2,1))