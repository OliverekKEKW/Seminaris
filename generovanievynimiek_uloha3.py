#nacitanie vstupnych hodnot: rozmery podlahy, vydatnost plechovky
sirka = input('Šírka podlahy (v metroch): ')
dlzka = input('Dĺžka podlahy (v metroch): ')
vydatnost_farby = input('Výdatnosť plechovky farby (v m štvorcových): ')


def plechovky_ks(sirka, dlzka, vydatnost):
    try:
        sirka = float(sirka)
        dlzka = float(dlzka)
        vydatnost_farby = float(vydatnost_farby)
    except ValueError:
        raise ValueError('Nečíselná hodnota.')
    if sirka < 0 or dlzka < 0:
        raise ValueError('Záporná hodnota pre dĺžku strany obdĺžnika.')
    plocha_podlahy = sirka * dlzka
    pocet_plechoviek = plocha_podlahy // vydatnost
    if plocha_podlahy % vydatnost != 0:
        pocet_plechoviek = pocet_plechoviek + 1
    return pocet_plechoviek






#vypisanie poctu plechoviek
print(f'Na premaľovanie podlahy potrebujeme {pocet_plechoviek(sirka, dlzka, vydatnost_farby)} ks plechoviek.')
