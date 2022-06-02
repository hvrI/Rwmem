import os, sys
my_lib_path = os.path.abspath('p:\Python\Rwmem')
sys.path.append(my_lib_path)

import logging
import rwmem

logging.getLogger('rwmem').setLevel(logging.WARNING)

rwm = rwmem.Rwmem("explorer")
string = rwm.read_int(0xe00798)
print(string)


