
import random
import gmpy2
import argparse

def getprimeover(bits):
    """Returns a prime number with specific number of bits """

    randfunc = random.SystemRandom()
    r = gmpy2.mpz(randfunc.getrandbits(bits))
    r = gmpy2.bit_set(r, bits - 1)
    return gmpy2.next_prime(r)
parser = argparse.ArgumentParser()
parser.add_argument('--n_len', type=int, required=True)
args = parser.parse_args()
sk = getprimeover(args.n_len)
print(sk)