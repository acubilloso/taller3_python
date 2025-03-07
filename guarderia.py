from modelos.boa_constrictor import Boa_constricor

class Guarderia():
    def crear_boas(self) -> list:
        boas = []
        boa1 = Boa_constricor('Boa 1', 34, 2, 'Kenia', 2000, 9)
        boa2= Boa_constricor('Boa 2', 34, 2, 'Kenia', 2000, 6)
        boas.append(boa1)
        boas.append(boa2)
        return boas

    def alimentar_boa(self, boa : Boa_constricor | None):
        if(boa == None):
             return ValueError("Esta Boa no existe")
        
        try:
            boa.comer_ratones()
        except ValueError:
            return("La boa esta llena")

        return "Exito!"



if __name__ == "__main__":
    guarderia = Guarderia()  
    boa1 = None
    listBoas = guarderia.crear_boas()
    print(guarderia.alimentar_boa(boa1))
        



