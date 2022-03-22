class ProcessNotFound(Exception):
    def __init__(self, process_name):
        message = f'Could not find process: {process_name}'
        super(ProcessNotFound, self).__init__(message)