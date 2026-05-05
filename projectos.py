class Cuenta_Bancaria:
 def __init__(self , saldo):
     self._saldo = saldo   
 @property
 def saldo(self):
    return self._saldo
 @saldo.setter
 def saldo(self , cantidad):
    if cantidad < 0:
        print("Saldo Negativo no admitido")
    else:
     self._saldo = cantidad
 @staticmethod
 def calcular_interes(saldo ,  tasa):
    return saldo * tasa
 @classmethod
 def cuenta_nueva(cls , titular):
  saldo = 0
  return cls(saldo)

# Probar @property y setter
cuenta = Cuenta_Bancaria(1000)
print(cuenta.saldo)       # 1000
cuenta.saldo = 500        # cambia
cuenta.saldo = -100       # bloqueado

# Probar @staticmethod
print(Cuenta_Bancaria.calcular_interes(1000, 0.05))   # 50.0

# Probar @classmethod
nueva = Cuenta_Bancaria.cuenta_nueva("Carlos")
print(nueva.saldo)        # 0
   
