from enum import Enum

class StatusTarefa(Enum):
    PENDENTE = "Pendente"
    CONCLUIDA = "Concluida"

class Prioridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
