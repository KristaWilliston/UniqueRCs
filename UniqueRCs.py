# Using just the concepts introduced so far, find as many (different!) ways as
# possible to code DNA reverse complement (at least 3!)
#   You may use any built-in function or string or list method.
#   You may use only basic data-types and lists and dictionaries.
#   Compare and critique each technique for robustness, speed, and correctness.

seq = "ATCGTACG"
# reverse = "GCATGCTA"
# rev comp = "CGTACGAT"


# 1
# using dictionary
dna_comps = {"A": "T", "T": "A", "C": "G", "G": "C"}

def reverse_complement(dna_string):
    reverse_comp = "" 
    for base in dna_string[::-1]: # reverses string
        reverse_comp += dna_comps[base]  # adds reverses back together
    return reverse_comp

reverse_comp = reverse_complement(seq)
print('Method 1 reverse complement:',reverse_comp)



# 2
# using ''.join and reversed() for seq
def reverse(dna_string):
    return ''.join(reversed(dna_string)) # reversed built in function

def complement(dna_string):
    return ''.join(dna_comps[i] for i in seq)

print('Method 2 reverse complement:',reverse(complement(seq)))



# 3
# using if statements 
def reverses(dna_string):
    if len(dna_string) == 0:
        return dna_string
    else:
        return reverses(dna_string[1:]) + dna_string[0] # iterating and rebuilding seq

def complements(dna_string): 
    dna_string = dna_string.upper()
    newstrand = ""
    for i in range(0,len(dna_string)):
        if dna_string[i] == "T":
            newstrand += "A"

        if dna_string[i] == "A":
            newstrand += "T"

        if dna_string[i] == "G":
            newstrand += "C"

        if dna_string[i] == "C":
            newstrand += "G"

    return newstrand

print('Method 3 reverse complement',complements(reverses(seq)))
