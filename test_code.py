import unittest
import numpy as np

import code

class Test(unittest.TestCase):

    seq = 'ATCTGACGCGCGCCGC'
    valid_bases = ['A', 'C', 'T', 'G']

    def test_maxcount(self):
        '''Tests that the total count of bases equals the length of the
        input sequence.
        '''
        seq_len = len(self.seq)
        # get the count of each base in self.seq as dictionary
        count_dict = code.count_basie(self.seq)
        # sum the values in the dictionary
        total_count = np.sum([count for count in count_dict.values()])
        # the count and length must be equal to pass this test
        self.assertEqual(total_count, seq_len)

if __name__ == '__main__':
    unittest.main()

