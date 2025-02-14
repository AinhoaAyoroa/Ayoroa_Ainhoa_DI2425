"""fichero a testear"""


class SaldoInsuficiente(Exception):
    """pasará si el saldo es insuficiente"""
    pass

class Cartera(object):
    """clase cartera"""
    def __init__(self, saldo_inicial=0):
        if isinstance(saldo_inicial, int) > 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0

    def gastar(self, cantidad):
        """funcion para restar el saldo cuando es gastado"""
        if self.saldo < cantidad:
            raise SaldoInsuficiente(
                                    f"No tienes dinero suficiente. Saldo actual: {cantidad}")

        self.saldo -= cantidad

    def ingresar(self, cantidad):
        """función para ingresar dinero"""
        self.saldo += cantidad
