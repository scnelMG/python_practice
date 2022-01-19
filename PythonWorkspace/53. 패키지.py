# import practice53_travel.Thailand
# #import practice53_travel.Thailand.ThailandPackage
# trip_to = practice53_travel.Thailand.ThailandPackage()
# trip_to.detail()

# from practice53_travel.Thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from practice53_travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from practice53_travel import * 
# trip_to = vietnam.VietnamPackage()
# trip_to = Thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(Thailand))

