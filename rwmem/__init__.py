import psutil
import logging
import win32process
import ctypes
import ctypes.wintypes

import rwmem.exception
import rwmem.memory

from typing import Optional

__version__ = "0.0.1"
__author__ = "duel"
__date__ = "23/12/2021"


PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_ALL_ACCESS = 0x1f0fff


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())


class Rwmem(object):
    """Initialize the RWMem class.
    If process_name or process_id is given, will open the running process.
    
    Parameters
    ----------
    process_name: str
        The name of the process to be opened.
    process_id: int
        The identifier of the local process to be opened.
    """
    
    def __init__(self, process_name: Optional[str]=None, *, process_id: Optional[int]=None):
        self.process_name = process_name
        self.process_id = process_id
        self.process_handle = None
        self.base_address = None
        if process_name is not None:
            self.find_process_from_name(process_name=process_name)
        elif process_id is not None:
            self.find_process_from_id(process_id=process_id)
            
    def __repr__(self):
        return f"<RWMem Instance: {self.process_name}>"
    
    def open_process(self, process_id, inherit_handle=True, process_access=PROCESS_ALL_ACCESS):
        """Open the process with all access on default and returns process handle
        
        Parameters
        ----------
        process_id: int
            The PID of the process
        inherit_handle: bool
            Processes created by this process will inherit the handle.
        process_access: int
            The access to the process object.
        """
        self.process_handle = ctypes.windll.kernel32.OpenProcess(process_access, inherit_handle, process_id)
        if self.process_handle:
            return self.process_handle
        raise rwmem.exception.CouldNotOpenProcess(process_id)
    
    def set_process_info(self, process):
        """Initialize process's information listed below
        
        process_name, process_id, process_handle, process_base_address
        """
        self.process_name = process.name()
        self.process_id = process.pid
        self.open_process(self.process_id, False, PROCESS_ALL_ACCESS)
        self.base_address = self.get_base_addr()
    
    def find_process_from_name(self, process_name: str):
        """Get the process by the process name and open the process.
        
        Parameters:
        -----------
        process_name: str
            The name of the process to be opened.
        
        Returns True if the handle exists
        """
        if process := [p for p in psutil.process_iter(attrs=['pid', 'name']) if process_name.lower() in p.name().lower()]:
            self.set_process_info(process[0])
            if self.process_handle:
                return True
        raise rwmem.exception.ProcessNotFound(process_name)
        
    def find_process_from_id(self, process_id: int):
        """Get the process by the process PID and open the process.
        
        Parameters:
        -----------
        process_id: str
            The identifier of the local process to be opened.
        
        Returns True if the handle exists
        """
        if process := [p for p in psutil.process_iter(attrs=['pid', 'name']) if process_id == p.pid]:
            self.set_process_info(process[0])
            if self.process_handle:
                return True
        raise rwmem.exception.CouldNotOpenProcess(process_id)
    
    def get_base_addr(self):
        """Get the process base address.
        
        Returns
        int(base_address)
            Process's base address
        """
        try:
            base_addr = win32process.EnumProcessModules(self.process_handle)[0]
        except Exception:
            base_addr = None
        return base_addr
    
    def close_process(self):
        """Closes an open object handle.
        
        Returns True if the closure is succeeded
        """
        if not self.process_handle:
            return
        result = ctypes.windll.kernel32.CloseHandle(self.process_handle)
        return result != 0
    
    def read_bytes(self, address: int, length: int=60):
        if not self.process_handle:
            raise rwmem.exception.ProcessError('You must open a process before calling this method')
        try:
            value = rwmem.memory.read_bytes(self.process_handle, address, length)
        except Exception as e:
            print(e)
        else:
            return value
        
    def read_int(self, address: int):
        if not self.process_handle:
            raise rwmem.exception.ProcessError('You must open a process before calling this method')
        try:
            value = rwmem.memory.read_int(self.process_handle, address)
        except Exception as e:
            print(e)
        else:
            return value
        
    def read_float(self, address: int):
        if not self.process_handle:
            raise rwmem.exception.ProcessError('You must open a process before calling this method')
        try:
            value = rwmem.memory.read_float(self.process_handle, address)
        except Exception as e:
            print(e)
        else:
            return value
        
    def read_string(self, address: int, length: int=60):
        if not self.process_handle:
            raise rwmem.exception.ProcessError('You must open a process before calling this method')
        try:
            result = self.read_bytes(address, length)
        except Exception as e:
            print(e)
        else:
            return "".join([chr(int(hex, 16)) for hex in result if int(hex, 16) != 0])
        
    def write_string(self, address: int, value: str):
        if not self.process_handle:
            raise rwmem.exception.ProcessError('You must open a process before calling this method')
        try:
            result = rwmem.memory.write_string(self.process_handle, address, value)
        except Exception as e:
            print(e)
        else:
            return result
