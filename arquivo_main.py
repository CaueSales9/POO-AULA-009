from carro_inteligente import CarroInteligente
from carro_esportivo import CarroEsportivo
from carro_corrida import CarroCorrida


def test_drive(carro):
    print(f'\nTestando {carro.__class__.__name__}')
    carro.acelerar()
    carro.exibir_velocidade()
    
if __name__ == "__main__":
    carro_inteligente = CarroInteligente(10)
    carro_inteligente.estacionar()
    test_drive(carro_inteligente)
    
    
    carro_sportivo = CarroEsportivo(10)
    carro_sportivo.turbo()
    test_drive(carro_sportivo)
    
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)