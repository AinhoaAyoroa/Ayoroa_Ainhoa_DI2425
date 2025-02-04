import pytest


import segundo_trimestre.unidad7.actividad1_resuelta.operaciones as operaciones


def test_suma_cero():
  assert operaciones.suma_enteros(0,0) == 0


def test_suma_positivos():
  assert operaciones.suma_enteros(5,5) == 10


def test_suma_positivos_negativos():
  assert operaciones.suma_enteros(-5,5) == 0


def test_suma_nagativo():
  assert operaciones.suma_enteros(-5,-5) == -10


def test_suma_excepcion_sumando1():
   with pytest.raises(TypeError):
       operaciones.suma_enteros(5.0,5) == 0


def test_suma_excepcion_sumando2():
   with pytest.raises(TypeError):
       operaciones.suma_enteros(5.0,'a') == 0


def test_suma_excepcion_sumandos():
   with pytest.raises(TypeError):
       operaciones.suma_enteros(True,'a') == 0