import re

def main():
    inf = open('StockQuote.txt', 'rt')
    outf = open('StockQuote.csv', 'wt')
    for line in inf:
        print(line.replace("\t",","), file=outf)
        #outfile.writelines(line)
        print('.', end='', flush=True)
    outf.close()
    print('\ndone.')

if __name__ == '__main__': main()