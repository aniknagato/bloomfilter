import random
from bitarray import bitarray
import math

def generate_random_dna(length):

    dna_seq = ''.join(random.choice('ACGT') for _ in range(length))
        
    return dna_seq


class BloomFilter:

    
    def __init__(self, dna_l, p):


        self.dna_l = dna_l
        self.n = len(self.dna_l)
        self.p = p
        self.m = -int(self.n*math.log(p)/math.log(2)**2)
        self.k = -int(math.log(p,2))
        self.len_dna = len(self.dna_l[0])

        self.bloom_fil = bitarray('0'*self.m)


    def gen_hash(self,dna_seq):
        dna_element = {'A':0,'C':1,'G':2,'T':3}
        hash_list = []

        dna_num = ''
        length = len(dna_seq)
        for i in range(length):
            dna_num += str(dna_element[dna_seq[i]])
            
        
        dna_num = int(dna_num)
        random.seed(dna_num)

        for x in range(self.k):
            a = random.randint(1,dna_num)
            b = random.randint(1,dna_num)
            hash_val = (a*x + b + 10) % self.m
            hash_list.append(hash_val)

        return hash_list
    
    
    def insert_BF(self,dna_seq):

        hash_list = self.gen_hash(dna_seq)

        for i in hash_list:
            self.bloom_fil[i]=True
            
        #print (self.bloom_fil)


    def check_viral(self, dna): 

        hash_val = self.gen_hash(dna)
        flag = True
        for i in hash_val:
            if self.bloom_fil[i]== 0:
                flag = False
            
        return flag



# this function is commited later.
def evaluation_func(num, leng, p):
    dna_list = []
    for i in range(num):
        dna_sample = generate_random_dna(leng)
        dna_list.append(dna_sample)

    # p = 0.02

    bf = BloomFilter(dna_list, p)
    for j in dna_list:
        bf.insert_BF(j)

    dna_test_list = []

    # dna_test was created for testing purpose
    number_of_test_dna = 100  # as mentioned in question
    count_false_positive = 0
    for i in range(number_of_test_dna):
        test_dna = generate_random_dna(leng)
        if test_dna not in dna_list and bf.check_viral(test_dna) == True:
            count_false_positive += 1
    false_positive_probability = count_false_positive / number_of_test_dna

    print ("Number of False Positive Instances in Test: ", count_false_positive)
    print ("False Positive: ", false_positive_probability)
