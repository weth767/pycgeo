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
        # common errors
        C_MS01 = "Invalid data type"
        C_MS02 = "Value wasn't found between the valid values"
        # canvas errors
        CV_MS01 = "Width and Height are necessary to create a screen"
    else:
        SP_MS01 = "Pontos e Segmentos não podem ser nulos ao mesmo tempo"
        SP_MS02 = "Segmentos não podem ser nulos"
        SP_MS03 = "Pontos não podem ser nulos"

        C_MS01 = "Tipo de dado inválido"
        C_MS02 = "O valor não foi encontrado entre os valores válidos"
        CV_MS01 = "O comprimento e largura são necessários para criar a tela"
