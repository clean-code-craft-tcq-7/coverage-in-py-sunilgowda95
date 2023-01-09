def test(self):
    import global_vars as gv
    self.assertEqual(gv.temperature_limits['PASSIVE_COOLING']['LOW'], 0)
    self.assertEqual(gv.temperature_limits['PASSIVE_COOLING']['HIGH'], 35)
    self.assertEqual(gv.temperature_limits['HI_ACTIVE_COOLING']['LOW'], 0)
    self.assertEqual(gv.temperature_limits['HI_ACTIVE_COOLING']['HIGH'], 45)
    self.assertEqual(gv.temperature_limits['MED_ACTIVE_COOLING']['LOW'], 0)
    self.assertEqual(gv.temperature_limits['MED_ACTIVE_COOLING']['HIGH'], 40)
    