
# example instruciton
# MIF R1 200

import re

match_object = re.match(r'(MIF) R[0-16] ([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])', 'MIF R1 25')

print(match_object.group())