import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

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

    def test_tilavuus_virheellinen(self):
        self.varasto = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_saldo_virheellinen(self):
        self.varasto = Varasto(-2, alku_saldo=-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_on_isompi_kuin_tilavuus(self):
        self.varasto = Varasto(0, alku_saldo=2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_maara_on_vanhemman_kuin_nolla_ja_maara_on_isonmpi_kuin_paljonko_mahtuu(self):
        self.varasto = Varasto(0)
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.varasto.lisaa_varastoon(4)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_jos_maara_on_enemman_kuin_saldo(self):
        self.varasto = Varasto(0)
        self.varasto.ota_varastosta(200)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ota_negatiivinen_maara(self):
        self.varasto = Varasto(0)
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_str(self):
        self.assertAlmostEqual(str(self.varasto), 'saldo = 0, vielä tilaa 10')


    