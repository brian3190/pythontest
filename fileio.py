def main():
    inf = open('lines.txt', 'rt')
    outf = open('lines2.txt', 'wt')
    for line in inf:
        print(line.rstrip(), file=outf)
        #outfile.writelines(line)
        print('.', end='', flush=True)
    outf.close()
    print('\ndone.')

if __name__ == '__main__': main()
