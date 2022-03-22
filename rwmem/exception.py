
class ProcessNotFound(Exception):
    def __init__(self, process_name):
        message = f'Could not find process: {process_name}'
        super(ProcessNotFound, self).__init__(message)
        
class CouldNotOpenProcess(Exception):
    def __init__(self, process_id):
        message = f'Could not open process: {process_id}'
        super(CouldNotOpenProcess, self).__init__(message)
        
class ProcessError(Exception):
    def __init__(self, message):
        super(ProcessError, self).__init__(message)
