from check_limits import infer_breach
import global_vars as gv

def get_limits_from_coolinType(coolingType):
  lowerLimit = gv.temperature_limits[coolingType]['LOW']
  upperLimit = gv.temperature_limits[coolingType]['HIGH']
  return lowerLimit, upperLimit

def check_classify_temperature_breach(coolingType, temperatureInC):
  lowerLimit, upperLimit = get_limits_from_coolinType(coolingType)
  return infer_breach(temperatureInC, lowerLimit, upperLimit)