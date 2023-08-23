# Python program that takes a string of nucleotides
# and counts the occurrence of each type.

def count_nucleotide(seq):
    n_dict = dict()
    for n in seq:
        if n not in n_dict:
            n_dict[n] = 1
        else:
            n_dict[n] += 1
    return n_dict

def calc_freq(seq):
    print('freqs')
    n_dict = count_nucleotide(seq)
    total = float(sum([n_dict[n] for n in n_dict.keys()]))
    for n in n_dict.keys():
        print(n + ':' + str(n_dict[n]/total))

calc_freq('ATCTGACGCGCGCCGC')
