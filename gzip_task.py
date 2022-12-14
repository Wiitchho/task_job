import gzip
import argparse
import os

parser = argparse.ArgumentParser(description='Zkomprimování souborů .log')
parser.add_argument('file_path', type=str, help='Cesta k programu')
parser.add_argument('-k', '--keep', action='store_true', help='nesmaže komprimované soubory')
args = parser.parse_args()


def find_f(path):
    '''
    Vyhledá soubory, které nejsou ve formátu .gzip
    :return
    list souborů, které chceme převést
    '''
    path_s = os.listdir(path)
    rdy_gzip = []
    for soubor in path_s:
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
            with open(path + '/' + soubor, 'rb') as f_in:
                with gzip.open(path + '/' + soubor + '.gz', 'wb') as f_out:
                    f_out.writelines(f_in)
                    if args.keep is not True:
                        os.remove(path + '/' + soubor)


if __name__ == '__main__':
    main(args.file_path)
