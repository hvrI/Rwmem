import os, sys
my_lib_path = os.path.abspath('p:\Python\Rwmem')
sys.path.append(my_lib_path)

import logging
import rwmem

logging.getLogger('rwmem').setLevel(logging.WARNING)

rwm = rwmem.Rwmem("explorer")
print(rwm.read_string(0x556c11a))


