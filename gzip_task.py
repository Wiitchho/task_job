import gzip
import argparse

parser = argparse.ArgumentParser(description='Zkomprimování souborů .log')
parser.add_argument('path', type=str, help='Cesta k programu')
args = parser.parse_args()


def find_f(path):
    '''
    Vyhledá soubory, které nejsou ve formátu .gzip
    :return
    list souborů, které chceme převést
    '''

    rdy_gzip = []
    for soubor in path:
        if ".gz" not in soubor:
            rdy_gzip.append(soubor)
    return rdy_gzip


def main(path):
    '''
    Vezme soubor. Pokud má soubor příponu ".log"
    upraví ho na na .gz a vymaže původní soubor.log.
    V případě, že soubor nemá formát ".log", pokračuje.
    :return: soubory.gz
    '''
    for soubor in find_f(path):
        if soubor.endswith('.log'):
            with open(soubor, 'rb') as f_in:
                with gzip.open(soubor + '.gz', 'wb') as f_out:
                    f_out.writelines(f_in)
                    path.remove(soubor)
        else:
            continue


if __name__ == '__main__':
    main(args.path)
