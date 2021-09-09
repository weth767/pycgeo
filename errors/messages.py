import locale

from enum import Enum


class Languages(Enum):
    PT_BR = 'pt_BR'


class Messages:
    _locale = locale.getdefaultlocale()
    if _locale[0] != Languages.PT_BR.value:
        # segments and points errors
        SP_MS01 = "Segments and points do not can be None on same time"
        SP_MS02 = "Segments do not can be None"
        SP_MS03 = "Points do not can be None"
        SP_MS04 = "Segments must be connected"
        SP_MS05 = "Leastwise two points must be connected or be equal"
        # common errors
        C_MS01 = "Invalid data type"
    else:
        print('entrou nesse')
        SP_MS01 = "Pontos e Segmentos não podem ser nulos ao mesmo tempo"
        SP_MS02 = "Segmentos não podem ser nulos"
        SP_MS03 = "Pontos não podem ser nulos"
        SP_MS04 = "Os segmentos devem estar conectados"
        SP_MS05 = "Pelo menos dois pontos devem estar conectados ou serem iguais"

        C_MS01 = "Tipo de dado inválido"
