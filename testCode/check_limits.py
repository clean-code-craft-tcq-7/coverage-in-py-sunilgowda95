def test(self):
    import check_limits
    self.assertTrue(check_limits.check_lower_breach(1,2))
    self.assertFalse(check_limits.check_lower_breach(2,2))
    self.assertFalse(check_limits.check_lower_breach(2,1))
    self.assertEqual(check_limits.check_higher_breach(2,1), 'TOO_HIGH')
    self.assertEqual(check_limits.check_higher_breach(2,2), 'NORMAL')
    self.assertEqual(check_limits.check_higher_breach(1,2), 'NORMAL')
    self.assertEqual(check_limits.infer_breach(6,0,5), 'TOO_HIGH')
    self.assertEqual(check_limits.infer_breach(-1,0,5), 'TOO_LOW')
    self.assertEqual(check_limits.infer_breach(0,0,5), 'NORMAL')
    self.assertEqual(check_limits.infer_breach(2,0,5), 'NORMAL')
    self.assertEqual(check_limits.infer_breach(5,0,5), 'NORMAL')
    