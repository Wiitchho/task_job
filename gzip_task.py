import gzip
import os


cur_dir = os.getcwd()
seznam_dir = os.listdir(cur_dir)


def find_f ():
    '''
    Vyhledá soubory, které nejsou ve formátu .gzip
    :return
    list souborů, které chceme převést
    '''

    rdy_gzip = []
    for soubor in seznam_dir:
        if ".gz" not in soubor:
            rdy_gzip.append(soubor)
    return rdy_gzip


def main():
    '''
    Vezme soubor. Pokud má soubor příponu ".log"
    upraví ho na na .gz a vymaže původní soubor.log.
    V případě, že soubor nemá formát ".log", pokračuje.
    :return: soubory.gz
    '''
    for soubor in find_f():
        if '.log' in soubor:
            with open(soubor,'rb') as f_in:
                with gzip.open (soubor + '.gz','wb') as f_out:
                    f_out.writelines(f_in)
                    os.remove(soubor)
        else:
            continue


if __name__ == '__main__':
    main()