import ctypes

import rwmem.exception

def read_bytes(handle: int, address: int, bytes: int):
    """Read data from process memory.
    
    Parameters:
    -----------
    handle: int
        The handle to a process.
        The handle must have the PROCESS_VM_OPERATION access right.
    address: int
        The process's pointer to be read.
    bytes:
        Number of bytes to be read.
        Default is 100
        
    Returns the raw value as bytes if succeeded.
    """
    ascii = []
    try:
        read_buffer = ctypes.c_ubyte()
        addr_buffer = ctypes.byref(read_buffer)
        n_size = ctypes.sizeof(read_buffer)
        lp_number_of_bytes_read = ctypes.c_ulong(0) 
        for i in range(bytes):
            ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(address + i), addr_buffer, n_size, lp_number_of_bytes_read)
            ascii.append(hex(read_buffer.value))
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return ascii
    
def read_int(handle: int, address: int):
    """Read 4 bytes from process memory.
    
    Parameters:
    -----------
    handle: int
        The handle to a process.
        The handle must have the PROCESS_VM_OPERATION access right.
    address: int
        The process's pointer to be read.
    
    eturns the raw value as int if succeeded.
    """
    try:
        read_buffer = ctypes.c_uint()
        addr_buffer = ctypes.byref(read_buffer)
        n_size = ctypes.sizeof(read_buffer)
        lp_number_of_bytes_read = ctypes.c_ulong(0) 
        ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(address), addr_buffer, n_size, lp_number_of_bytes_read)
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return read_buffer.value
    
def read_float(handle: int, address: int):
    """Read 4 bytes from process memory.
    
    Parameters:
    -----------
    handle: int
        The handle to a process.
        The handle must have the PROCESS_VM_OPERATION access right.
    address: int
        The process's pointer to be read.
    
    eturns the raw value as float if succeeded.
    """
    try:
        read_buffer = ctypes.c_float()
        addr_buffer = ctypes.byref(read_buffer)
        n_size = ctypes.sizeof(read_buffer)
        lp_number_of_bytes_read = ctypes.c_ulong(0) 
        ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(address), addr_buffer, n_size, lp_number_of_bytes_read)
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return read_buffer.value
    
def read_double(handle: int, address: int):
    try:
        read_buffer = ctypes.c_double()
        addr_buffer = ctypes.byref(read_buffer)
        n_size = ctypes.sizeof(read_buffer)
        lp_number_of_bytes_read = ctypes.c_ulong(0)
        ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(address), addr_buffer, n_size, lp_number_of_bytes_read)
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return read_buffer.value
    
def write_int(handle: int, address: int, value: str):
    try:
        for x in value:
            write_buffer = ctypes.c_uint(int(x))
            addr_buffer = ctypes.byref(write_buffer)
            n_size = ctypes.sizeof(write_buffer)
            lp_number_of_bytes_read = ctypes.c_ulong(0)
            res = ctypes.windll.kernel32.WriteProcessMemory(handle, ctypes.c_void_p(address), addr_buffer, n_size, lp_number_of_bytes_read)
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return bool(res)
    
def write_string(handle: int, address: int, value: str):
    try:
        write_buffer = ctypes.create_string_buffer(value.encode())
        addr_buffer = ctypes.byref(write_buffer)
        n_size = ctypes.sizeof(write_buffer)
        lp_number_of_bytes_read = ctypes.c_size_t()
        res = ctypes.windll.kernel32.WriteProcessMemory(handle, ctypes.c_void_p(address), addr_buffer, n_size, lp_number_of_bytes_read)
    except (TypeError, ValueError, BufferError) as e:
        raise rwmem.exception.WinAPIError(e) from e
    else:
        return bool(res)
