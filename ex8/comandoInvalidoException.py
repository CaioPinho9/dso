class ComandoInvalidoException(Exception):
    def __init__(self):
        super().__init__("O comando esta invalido!")
