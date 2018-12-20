class General():
    @staticmethod
    def required(request_data, *validation_args):
        error_msg = 'This field is required'

        if request_data is None :
            return {'status': False, 'message': error_msg}
            
        if not isinstance(request_data, int):
            if len(request_data) == 0:
                return {'status': False, 'message': error_msg}
        
        return {'status': True}

    @staticmethod
    def max(request_data, *validator_args):
        error_msg = 'This field must not be greater than {args}'.format(
            args=validator_args[0])
        if isinstance(request_data, int):
            if request_data > int(validator_args[0]):
                return { 'status': False, 'message': error_msg}
        else:
            if len(request_data) > int(validator_args[0]):
                return {'status': False, 'message': error_msg}
        return {'status': True}

    @staticmethod
    def min(request_data, *validator_args):
        error_msg = 'This field must not be less than {args}'.format(
            args=validator_args[0])
        if isinstance(request_data, int):
            if request_data < int(validator_args[0]):
                return {'status': False, 'message': error_msg}
        else:
            if len(request_data) < int(validator_args[0]):
                return {'status': False, 'message': error_msg}
        return {'status': True}
    
    @staticmethod
    def alpha(request_data, *validator_args):
        error_msg = 'This field must contain on alphabets (A-Za-z)'
        if not request_data.isalpha()  :
            return {'status': False, 'message': error_msg}
        return {'status': True}

    @staticmethod
    def alphanumeric(request_data, *validator_args):
        error_msg = 'This field must contain both alphabets and numbers (A-Za-z0-9)'
        if not request_data.isalnum():
            return {'status': False, 'message': error_msg}
        return {'status': True}
    
    @staticmethod
    def list(request_data, *validator_args):
        print(validator_args)
        error_msg = 'This field must be a list'
        if not isinstance(request_data, list):
            return {'status': False, 'message': error_msg}
        if validator_args:
            if validator_args[0] and len(request_data) != validator_args[0]:
                error_msg += ' with length of {arg}'.format(arg=validator_args[0])
                return {'status': False, 'message': error_msg}
        
        return {'status': True}
    
    @staticmethod
    def boolean(request_data, *validator_arg):
        error_msg = 'This field must be a boolean value (True/False) or (1/0)'

        if isinstance(request_data, bool) or (request_data == 0) or request_data == 1:
            return {'status': True}
        
        return {'status': False, 'message': error_msg}
    