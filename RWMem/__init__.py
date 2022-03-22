import psutil
import logging
import win32process
import ctypes
import ctypes.wintypes

import exception


__version__ = "0.0.1"
__date__ = "23/12/2021"


PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_ALL_ACCESS = 0x1f0fff


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())


class RWMem(object):
    
    def __init__(self, process_name: str = None):
        self.process_name = process_name
        self.process_id = None
        self.process_handle = None
        self.base_address = None
        self.hwnd = None
        if process_name is not None:
            self.find_process_from_name(process_name=process_name)
            
    def __repr__(self):
        return f"<RWMem Instance: {self.process_name}>"
    
    def set_process_info(self, process):
        self.process_name = process.name()
        self.process_id = process.pid
        self.process_handle = ctypes.windll.kernel32.OpenProcess(
            PROCESS_ALL_ACCESS, False, self.process_id
        )
        self.base_address = self.get_base_addr()
    
    def find_process_from_name(self, process_name: str):
        if process := [p for p in psutil.process_iter(attrs=['pid', 'name']) if process_name.lower() in p.name().lower()]:
            self.set_process_info(process[0])
            if self.process_handle:
                return self
        raise exception.ProcessNotFound
        
    def find_process_from_id(self, process_id: int):
        if process := [p for p in psutil.process_iter(attrs=['pid', 'name']) if process_id == p.pid]:
            self.set_process_info(process[0])
            if self.process_handle:
                return self
        raise exception.ProcessNotFound
    
    def get_base_addr(self):
        base_addr = win32process.EnumProcessModules(self.process_handle)
        return base_addr[0]
