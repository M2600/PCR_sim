import sys
import difflib


def get_dna_complement(dna):
    dna = dna.upper()
    pares = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    complement = ""
    for c in dna:
        if c not in pares:
            print("DNA string allowed characters: A, T, C, G")
            sys.exit(1)
        complement += pares[c]
    return complement


def check(needle, haystack, threshold=0.8):
    match_indexes = []
    d = difflib.Differ()
    for i,c in enumerate(haystack):
        if i + len(needle) > len(haystack):
            break
        h = haystack[i:i+len(needle)]
        #print("needle:", needle)
        #print("h:", h)
        diffs = d.compare(needle, h)
        plus = 0
        minus = 0
        for diff in diffs:
            #print (diff)
            if diff.startswith("+"):
                plus += 1
            elif diff.startswith("-"):
                minus += 1
        accuracy = (len(needle) - minus) / len(needle)
        if accuracy >= threshold:
            match_indexes.append(i)
            print ("Found match at index", i)
            print ("primer:", needle)
            print ("Accuracy: ", accuracy*100, "%")
            print("---------------")
    return match_indexes

def main():
    if len(sys.argv) < 4:
        print("Error: Forward_primer or reverse_primer or haystack not provided")
        print("Usage: python check_match.py <haystack> <forward_primer> <reverse_primer> [threshold]")
        sys.exit(1)
    forward_primer = sys.argv[2].upper()
    reverse_primer = sys.argv[3].upper()
    haystack = sys.argv[1].upper()
    if len(sys.argv) > 4:
        threshold = float(sys.argv[4])
    else:
        threshold = 0.8

    forward_primer = get_dna_complement(forward_primer)
    reverse_primer = get_dna_complement(reverse_primer)



    print("Forward primer: ", forward_primer)
    print("Reverse primer: ", reverse_primer)
    print("Haystack: ", haystack)
    print("Threshold: ", threshold)
    print()
    
    print("[Checking forward primer...]")
    forward_match_indexes = check(forward_primer, haystack, threshold=threshold)
    print("=============================")
    print("[Checking reverse primer...]")
    reverse_match_indexes = check(reverse_primer[::-1], haystack, threshold=threshold)

    print("=============================")
    print("[Printing matches...]")

    for f_index in forward_match_indexes:
        for r_index in reverse_match_indexes:
            if f_index < r_index:
                print("Match found at indexes", f_index, "and", r_index)
                print("Forward primer:", haystack[f_index:f_index+len(forward_primer)])
                print("Reverse primer:", haystack[r_index:r_index+len(reverse_primer)])
                print("DNA sequence:", haystack[f_index:r_index+len(reverse_primer)])
                print("DNA length:", len(haystack[f_index:r_index+len(reverse_primer)]))
                print("---------------")



if __name__ == '__main__':
    main()





