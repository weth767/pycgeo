import locale

from enum import Enum


class Languages(Enum):
    PT_BR = 'pt_BR'
    EN_US = 'en_US'
    ES_ES = 'es_ES'


class ErrorCodes(Enum):
    ERROR = 0
    # Errors
    ERROR_INVALID_PARAMETER_VALUE = 1
    ERROR_INVALID_PARAMETER_TYPE = 2
    ERROR_INVALID_PARAMETER_SIZE = 3
    ERROR_INVALID_PARAMETER_FORMAT = 4
    ERROR_INVALID_PARAMETER_RANGE = 5
    ERROR_INVALID_PARAMETER_UNIQUE = 6
    ERROR_INVALID_PARAMETER_REQUIRED = 7
    ERROR_INVALID_PARAMETER_NOT_EMPTY = 8


class Messages:

    __tip_messages__ = {
        ErrorCodes.ERROR: {
            Languages.PT_BR: 'Verique os parâmetros e saída e tente novamente.',
            Languages.EN_US: 'Verify the parameters and output and try again.',
            Languages.ES_ES: 'Verifique los parámetros y salida y intente de nuevo.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_VALUE: {
            Languages.PT_BR: 'O valor do parâmetro "{parameter_name}" não é válido.',
            Languages.EN_US: 'The value of the parameter "{parameter_name}" is invalid.',
            Languages.ES_ES: 'El valor del parámetro "{parameter_name}" no es válido.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_TYPE: {
            Languages.PT_BR: 'O tipo do parâmetro "{parameter_name}" não é válido.',
            Languages.EN_US: 'The type of the parameter "{parameter_name}" is invalid.',
            Languages.ES_ES: 'El tipo del parámetro "{parameter_name}" no es válido.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_SIZE: {
            Languages.PT_BR: 'O tamanho do parâmetro "{parameter_name}" não é válido.',
            Languages.EN_US: 'The size of the parameter "{parameter_name}" is invalid.',
            Languages.ES_ES: 'El tamaño del parámetro "{parameter_name}" no es válido.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_FORMAT: {
            Languages.PT_BR: 'O formato do parâmetro "{parameter_name}" não é válido.',
            Languages.EN_US: 'The format of the parameter "{parameter_name}" is invalid.',
            Languages.ES_ES: 'El formato del parámetro "{parameter_name}" no es válido.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_RANGE: {
            Languages.PT_BR: 'O valor do parâmetro "{parameter_name}" não está dentro do intervalo válido.',
            Languages.EN_US: 'The value of the parameter "{parameter_name}" is not within the valid range.',
            Languages.ES_ES: 'El valor del parámetro "{parameter_name}" no está dentro del intervalo válido.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_UNIQUE: {
            Languages.PT_BR: 'O valor do parâmetro "{parameter_name}" não é único.',
            Languages.EN_US: 'The value of the parameter "{parameter_name}" is not unique.',
            Languages.ES_ES: 'El valor del parámetro "{parameter_name}" no es único.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED: {
            Languages.PT_BR: 'O parâmetro "{parameter_name}" é obrigatório.',
            Languages.EN_US: 'The parameter "{parameter_name}" is required.',
            Languages.ES_ES: 'El parámetro "{parameter_name}" es obligatorio.'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_NOT_EMPTY: {
            Languages.PT_BR: 'O parâmetro "{parameter_name}" não pode ser vazio.',
            Languages.EN_US: 'The parameter "{parameter_name}" cannot be empty.',
            Languages.ES_ES: 'El parámetro "{parameter_name}" no puede estar vacío.'
        }
    }
    __error_messages__ = {
        ErrorCodes.ERROR: {
            Languages.PT_BR: 'Erro desconhecido',
            Languages.EN_US: 'Unknown error',
            Languages.ES_ES: 'Error desconocido'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_VALUE: {
            Languages.PT_BR: 'Valor inválido para o parâmetro',
            Languages.EN_US: 'Invalid value for parameter',
            Languages.ES_ES: 'Valor inválido para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_TYPE: {
            Languages.PT_BR: 'Tipo inválido para o parâmetro',
            Languages.EN_US: 'Invalid type for parameter',
            Languages.ES_ES: 'Tipo inválido para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_SIZE: {
            Languages.PT_BR: 'Tamanho inválido para o parâmetro',
            Languages.EN_US: 'Invalid size for parameter',
            Languages.ES_ES: 'Tamaño inválido para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_FORMAT: {
            Languages.PT_BR: 'Formato inválido para o parâmetro',
            Languages.EN_US: 'Invalid format for parameter',
            Languages.ES_ES: 'Formato inválido para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_RANGE: {
            Languages.PT_BR: 'Valor fora do intervalo para o parâmetro',
            Languages.EN_US: 'Value out of range for parameter',
            Languages.ES_ES: 'Valor fuera del intervalo para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_UNIQUE: {
            Languages.PT_BR: 'Valor único para o parâmetro',
            Languages.EN_US: 'Unique value for parameter',
            Languages.ES_ES: 'Valor único para el parámetro'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_REQUIRED: {
            Languages.PT_BR: 'Parâmetro obrigatório',
            Languages.EN_US: 'Required parameter',
            Languages.ES_ES: 'Parámetro obligatorio'
        },
        ErrorCodes.ERROR_INVALID_PARAMETER_NOT_EMPTY: {
            Languages.PT_BR: 'Parâmetro não pode ser vazio',
            Languages.EN_US: 'Parameter cannot be empty',
            Languages.ES_ES: 'Parámetro no puede estar vacío'
        },
    }

    @staticmethod
    def get_message(error_code: ErrorCodes):
        return Messages.__error_messages__[error_code][Languages[Messages.locale().upper()]]

    @staticmethod
    def get_tip_message(error_code: ErrorCodes, parameter_name=''):
        return Messages.__tip_messages__[error_code][Languages[Messages.locale().upper()]].format(parameter_name=parameter_name)

    @staticmethod
    def locale():
        return locale.getdefaultlocale()[0]


class BaseException(Exception):
    def __init__(self, message=Messages.get_message(ErrorCodes.ERROR), error_code=ErrorCodes.ERROR, tip=Messages.get_tip_message(ErrorCodes.ERROR, '')):
        self.message = message
        self.error_code = error_code
        self.tip = tip

    def __str__(self):
        return self.message


class GeometryException(BaseException):
    pass


class ArithmeticException(BaseException):
    pass
