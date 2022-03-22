import ctypes

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
    except:
        pass
    else:
        return ascii