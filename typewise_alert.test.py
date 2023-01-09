import unittest
import global_vars as gv
from alert_stub import send_breach_to_target_stub

# initialize test alias in global variables
gv.send_breach_to_target = send_breach_to_target_stub

class TypewiseTest(unittest.TestCase):
  def test_comparision(self):
    from testCode.comparision import test as testComparision
    testComparision(self)

  def test_limits(self):
    from testCode.limits import test as testLimits
    testLimits(self)
    
  def test_check_limits(self):
    from testCode.check_limits import test as testCheckLimits
    testCheckLimits(self)
    
  def test_typewise_alert(self):
    from testCode.typewise_alert import test as testTestTypewiseAlert
    testTestTypewiseAlert(self)

if __name__ == '__main__':
  unittest.main()
