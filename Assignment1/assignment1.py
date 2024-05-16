import argparse as ap
import multiprocessing as mp

""" 
Iterate through fastqfile. NB: chunk is assumed to be multiple of 4!
"""

def iterate_fastqfile():
    with open(fastqfile, 'r') as fastq:
        #fastforward
        i = 0
        while i < start:
            fastq.readline()
            i += 1

        results = []
        counter = 0
        while counter < chunk:
            header = fastq.readline()
            nucleotides = fastq.readline()
            strand = fastq.readline()
            qual = fastq.readline()
            counter += 4

            if not(qual):
                # we reached the end of the file
                break
            for j, c in enumerate(qual):

                try:
                    results[j] += ord(c) - 33
                except IndexError:
                    results.append(ord(c) - 33)

        return [(phredscore / (counter / 4)) for phredscore in results]



argparser = ap.ArgumentParser(description="Script voor Opdracht 1 van Big Data Computing")
argparser.add_argument("-n", action="store",
                       dest="n", required=True, type=int,
                       help="Aantal cores om te gebruiken.")
argparser.add_argument("-o", action="store", dest="csvfile", type=ap.FileType('w', encoding='UTF-8'),
                       required=False, help="CSV file om de output in op te slaan. Default is output naar terminal STDOUT")
argparser.add_argument("fastq_files", action="store", type=ap.FileType('r'), nargs='+', help="Minstens 1 Illumina Fastq Format file om te verwerken")
args = argparser.parse_args()