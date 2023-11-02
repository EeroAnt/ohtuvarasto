import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_kehno = Varasto(0,-1)
        self.varasto_liikaa_saldoa = Varasto(3,6)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varasto_kehno_tilavuus(self):
        self.assertEqual(self.varasto_kehno.tilavuus,0)
    
    def test_varasto_kehno_alkusaldo(self):
        self.assertEqual(self.varasto_kehno.saldo,0)

    def test_varastolla_liikaa_alkusaldoa(self):
        self.assertEqual(self.varasto_liikaa_saldoa.saldo,3)
    
    def test_lisataan_epanegatiivinen(self):
        self.varasto.lisaa_varastoon(-2)
        self.assertEqual(self.varasto.paljonko_mahtuu(),10)
    
    def test_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(10000)
        self.assertEqual(self.varasto.paljonko_mahtuu(),0)
    
    def test_ota_epanegatiivinen(self):
        self.assertEqual(self.varasto.ota_varastosta(-1),0)
    
    def test_ota_liikaa_saldo(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(1000)
        self.assertEqual(self.varasto.paljonko_mahtuu(),10)
    
    def test_ota_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.ota_varastosta(10),10)
        
    def test_print(self):
        self.assertEqual(self.varasto.__str__(),"saldo = 0, vielä tilaa 10")