from temperature_breach import check_classify_temperature_breach
import global_vars as gv

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    check_classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  gv.send_breach_to_target(alertTarget, breachType)



