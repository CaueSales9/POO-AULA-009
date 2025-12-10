from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo

if __name__ == "__main__":
    #carro inteligente
    carro_inteligente = CarroInteligente(10)
    print('Carro inteligente:')
    carro_inteligente.exibir_velocidade()
    carro_inteligente.estacionar()
    print()
    
    #Carro esportivo
    carro_sportivo = CarroEsportivo(50)
    print('carro sportivo')
    carro_sportivo.turbo()
    carro_sportivo.exibir_velocidade()
    print()