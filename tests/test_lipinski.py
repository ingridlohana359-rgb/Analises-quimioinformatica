import unittest

def validar_lipinski(peso, logp, h_donors, h_acceptors):
    """Função de validação baseada na Regra de Lipinski para testes."""
    if peso <= 500 and logp <= 5 and h_donors <= 5 and h_acceptors <= 10:
        return "Aprovado"
    return "Rejeitado"

class TestLipinskiFilter(unittest.TestCase):
    
    def test_aspirina_aprovada(self):
        # Valores aproximados da Aspirina (deve passar)
        resultado = validar_lipinski(peso=180.16, logp=1.2, h_donors=1, h_acceptors=4)
        self.assertEqual(resultado, "Aprovado")

    def test_molecula_grande_rejeitada(self):
        # Molécula com peso e lipofilicidade acima do limite (deve ser rejeitada)
        resultado = validar_lipinski(peso=650.0, logp=6.5, h_donors=6, h_acceptors=12)
        self.assertEqual(resultado, "Rejeitado")

if __name__ == '__main__':
    unittest.main()
