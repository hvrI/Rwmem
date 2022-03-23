import os, sys
my_lib_path = os.path.abspath('p:\Python\Rwmem')
sys.path.append(my_lib_path)

import logging
import rwmem

logging.getLogger('rwmem').setLevel(logging.WARNING)

rwm = rwmem.Rwmem("Minecraft.Windows.exe")

ptr = rwm.get_pointer_addr(rwm.base_address+0x82DD40, [0x74, 0x2C, 0xC7, 0x45, 0xB8, 0x00, 0x00, 0xE0, 0x40])
print(ptr)


