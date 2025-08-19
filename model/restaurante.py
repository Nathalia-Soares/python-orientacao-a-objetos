from model.avaliacao import Avaliacao

class Restaurante: 

    restaurantes = []

    #Construtor da classe
    def __init__(self, nome, categoria):
        #Utiliza-se _ para atributos privados
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} - {self._categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print("Nome do Restaurante".ljust(25), "Categoria".ljust(27), "Avaliação".ljust(15), "Status")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} - {restaurante._categoria.ljust(25)} - {str(restaurante.media_avaliacoes).ljust(13)} - {restaurante.ativo}")

    @property
    def ativo(self):
        return "verdadeiro" if self._ativo else "falso"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        media_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        return round(media_notas / len(self._avaliacoes), 1)