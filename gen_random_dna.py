import random

DNA_CHARS = "ACGT"

def random_dna(length):
    return ''.join(random.choice(DNA_CHARS) for _ in range(length))

def main():
    rand_dna = random_dna(100)
    print(rand_dna)

if __name__ == '__main__':
    main()
