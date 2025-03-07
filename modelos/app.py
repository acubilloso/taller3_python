from boa_constrictor import Boa_constricor
from huron import Huron
from modelos.guarderia import Guarderia

boa = Boa_constricor('Boa 1', 34, 2, 'Kenia', 2000, 0)
print(boa.calcular_flete())
boa.comer_ratones()
print(boa.get_ratones_comidos())
boa.comer_ratones()
print(boa.get_ratones_comidos())
print(boa.hacer_sonido())
boa.comer(30)
print(boa.get_kilos_comidos())

huron = Huron('Huron 1', 15, 2, 'Ecuador', 200)
print(huron.calcular_flete())
huron.comer(230)
print(huron.get_kilos_comidos())
print(huron.hacer_sonido())


guarderia = Guarderia()
guarderia.alimentar_boa(guarderia.crear_boas()[0])