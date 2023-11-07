from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(f'''Luonnin jälkeen:"
Mehuvarasto: {mehua}" 
Olutvarasto: {olutta}
Olut getterit:
saldo = {olutta.saldo}"
tilavuus = {olutta.tilavuus}"
paljonko_mahtuu = {olutta.paljonko_mahtuu()}
Mehu setterit: Lisätään 50.7''')
    huonoa(mehua, olutta)

def huonoa(mehua, olutta):
    huono = Varasto(-100.0)
    mehua.lisaa_varastoon(50.7)
    print(f'''Mehuvarasto: {mehua}
Otetaan 3.14''')
    mehua.ota_varastosta(3.14)
    print(f'''Mehuvarasto: {mehua}
Virhetilanteita:
Varasto(-100.0);
{huono}
Varasto(100.0, -50.7)''')
    huono = Varasto(100.0, -50.7)
    print(f'''{huono}
Olutvarasto: {olutta}"
olutta.lisaa_varastoon(1000.0)''')
    olutta.lisaa_varastoon(1000.0)
    print(f'''Olutvarasto: {olutta}"
Mehuvarasto: {mehua}")
mehua.lisaa_varastoon(-666.0)''')
    mehua.lisaa_varastoon(-666.0)
    mehuaa(mehua, olutta)

def mehuaa(mehua, olutta):
    saatiin = olutta.ota_varastosta(1000.0)
    print(f'''Mehuvarasto: {mehua}"
Olutvarasto: {olutta}")
olutta.ota_varastosta(1000.0)
saatiin {saatiin}
Olutvarasto: {olutta}''')
    saatiin = mehua.ota_varastosta(-32.9)
    print(f'''Mehuvarasto: {mehua}
mehua.otaVarastosta(-32.9)
saatiin {saatiin}
Mehuvarasto: {mehua}''')       


if __name__ == "__main__":
    main()
