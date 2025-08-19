from model.restaurante import Restaurante

restaurante_praca = Restaurante("Praça Gourmet", "Gourmet")
restaurante_mexicano = Restaurante("Mexicano", "Mexicana")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao("João", 5)
restaurante_praca.receber_avaliacao("Maria", 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()