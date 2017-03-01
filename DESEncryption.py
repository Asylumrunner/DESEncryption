__author__ = 'Michael Burdick'

import sys

initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]

inverse_initial_permutations = [40, 8, 48, 16, 56, 24, 64, 32,
                                39, 7, 47, 15, 55, 23, 63, 31,
                                38, 6, 46, 14, 54, 22, 62, 30,
                                37, 5, 45, 13, 53, 21, 61, 29,
                                36, 4, 44, 12, 52, 20, 60, 28,
                                35, 3, 43, 11, 51, 19, 59, 27,
                                34, 2, 42, 10, 50, 18, 58, 26,
                                33, 1, 41, 9, 49, 17, 57, 25 ]

E_bit_selection_table = [32, 1, 2, 3, 4, 5,
                         4, 5, 6, 7, 8, 9,
                         8, 9, 10, 11, 12, 13,
                         12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21,
                         20, 21, 22, 23, 24, 25,
                         24, 25, 26, 27, 28, 29,
                         28, 29, 30, 31, 32, 1 ]

thirty_two_bit_permutation = [16, 7, 20, 21,
                              29, 12, 28, 17,
                              1, 15, 23, 26,
                              5, 18, 31, 10,
                              2, 8, 24, 14,
                              32, 27, 3, 9,
                              19, 13, 30, 6,
                              22, 11, 4, 25]

key_permutations_1_C = [57, 49, 41, 33, 25, 17, 9,
                        1, 58, 50, 42, 34, 26, 18,
                        10, 2, 59, 51, 43, 35, 27,
                        19, 11, 3, 60, 52, 44, 36]

key_permutations_1_D = [63, 55, 47, 39, 31, 23, 15,
                        7, 62, 54, 46, 38, 30, 22,
                        14, 6, 61, 53, 45, 37, 29,
                        21, 13, 5, 28, 20, 12, 4]

permuted_choice_2 = [14, 17, 11, 24, 1, 5,
                     3, 28, 15, 6, 21, 10,
                     23, 19, 12, 4, 26, 8,
                     16, 7, 27, 20, 13, 2,
                     41, 52, 31, 37, 47, 55,
                     30, 40, 51, 45, 33, 48,
                     44, 49, 39, 56, 34, 53,
                     46, 42, 50, 36, 29, 32]

S1_row_one = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
S1_row_two = [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ]
S1_row_three = [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0 ]
S1_row_four = [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]
S1 = [S1_row_one, S1_row_two, S1_row_three, S1_row_four]

S2_row_one = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10 ]
S2_row_two = [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5 ]
S2_row_three = [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15]
S2_row_four = [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]
S2 = [S2_row_one, S2_row_two, S2_row_three, S2_row_four]

S3_row_one = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8]
S3_row_two = [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1]
S3_row_three = [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7]
S3_row_four = [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
S3 = [S3_row_one, S3_row_two, S3_row_three, S3_row_four]

S4_row_one = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15]
S4_row_two = [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9]
S4_row_three = [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4]
S4_row_four = [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
S4 = [S4_row_one, S4_row_two, S4_row_three, S4_row_four]

S5_row_one = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9]
S5_row_two = [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6]
S5_row_three = [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14]
S5_row_four = [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
S5 = [S5_row_one, S5_row_two, S5_row_three, S5_row_four]

S6_row_one = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11]
S6_row_two = [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8]
S6_row_three = [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6]
S6_row_four = [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
S6 = [S6_row_one, S6_row_two, S6_row_three, S6_row_four]

S7_row_one = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1]
S7_row_two = [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6]
S7_row_three = [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2]
S7_row_four = [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
S7 = [S7_row_one, S7_row_two, S7_row_three, S7_row_four]

S8_row_one = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7]
S8_row_two = [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2]
S8_row_three = [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8]
S8_row_four = [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
S8 = [S8_row_one, S8_row_two, S8_row_three, S8_row_four]


def permute(list_to_permute, permutation_matrix): #permute takes a list and permutes it according to a matrix
    permuted_list = [] #create an empty list
    for x in range(len(permutation_matrix)): #for every value in the matrix
        permuted_list.append(list_to_permute[permutation_matrix[x]-1]) #use the permutation matrix to see what value should be placed here
    return permuted_list #of note is the fact that permute can make shorter lists longer, which we use for our f function


def permute_key(key, permutation_matrix_C, permuation_matrix_D): #permute_key takes in an initial key, and two halves of the key permutation matrix, and outputs all keys for encryption/decryption
    key_permutations = []#create an empty list to hold all the keys
    key_in_list_form = list(str(key))#turn the key into a list
    key_C = permute(key_in_list_form, permutation_matrix_C)#permute the left half
    key_D = permute(key_in_list_form, permuation_matrix_D)#permute the right half
    two_left_shifts = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]#mark the iterations where we have to left shift twice
    for x in range(16):#then, for sixteen iterations
        if two_left_shifts.count(x) == 1:
            temp_C = key_C.pop(0)
            temp_D = key_D.pop(0)
            key_C.append(temp_C)
            key_D.append(temp_D)

        temp_C = key_C.pop(0)#perform left shifts as needed
        temp_D = key_D.pop(0)
        key_C.append(temp_C)
        key_D.append(temp_D)
        key_permutations.append(permute(key_C+key_D, permuted_choice_2))#then use PC2 on that shifted keystring to generate this round's subkey

    return key_permutations #then return the list of subkeys


def s_function(block, s_chart):#the s function is simple
    column = (block[1]*8) + (block[2]*4) + (block[3]*2) + block[4]#it picks the column equal to the four-digit binary number demonstrated by the middle four numbers of the block
    row = (block[0]*2) + block[5]#and the column designated by the two digit binary nummber demonstrated by the first and last digits
    return bin(s_chart[row][column])[2:].zfill(4)#then it returns the result as a four-bit binary number


def f_function(text, key): #the f-function is the meat of the encryption/decryption process
    extended_text = permute(text, E_bit_selection_table)#first, use permute to extend the plaintext to 48 bits
    text_xored_with_data = []
    for x in range(48):#then, xor the text with the key
        text_xored_with_data.append(int(extended_text[x]) ^ int(key[x]))
    block_S1 = text_xored_with_data[0:6]#split this result into 6-bit blocks
    block_S2 = text_xored_with_data[6:12]
    block_S3 = text_xored_with_data[12:18]
    block_S4 = text_xored_with_data[18:24]
    block_S5 = text_xored_with_data[24:30]
    block_S6 = text_xored_with_data[30:36]
    block_S7 = text_xored_with_data[36:42]
    block_S8 = text_xored_with_data[42:]

    s1_resolved = str(s_function(block_S1, S1))#then, apply the s-function to each of these 6-bit blocks
    s2_resolved = str(s_function(block_S2, S2))
    s3_resolved = str(s_function(block_S3, S3))
    s4_resolved = str(s_function(block_S4, S4))
    s5_resolved = str(s_function(block_S5, S5))
    s6_resolved = str(s_function(block_S6, S6))
    s7_resolved = str(s_function(block_S7, S7))
    s8_resolved = str(s_function(block_S8, S8))

    pre_p_permutation = s1_resolved + s2_resolved + s3_resolved + s4_resolved + s5_resolved + s6_resolved + s7_resolved + s8_resolved#append all of these blocks together
    pre_p_permuation_list = list(pre_p_permutation)#then convert them to a list
    return permute(pre_p_permuation_list, thirty_two_bit_permutation)#lastly, return the result of permuting that list by the 32-bit permutation


#------------START OF MAIN---------------------
plaintext_filename = sys.argv[1]
if sys.argv[2] == "encrypt": #a sysarg determines if you're encrypting or decrypting
    encrypt = True
else:
    encrypt = False
plaintext_file = open(plaintext_filename, "r")
plaintext = []

for line in plaintext_file:
    plaintext.append(line)

plaintext_file.close()#open the file, read in the data to be processed, then close it
key = 1001011010010110100101101001011010010110100101101001011010010110 #I'm hardcoding in the key rn

plaintext_bin = list(plaintext[0])

if encrypt:#if we're encrypting
    permuted_plaintext = permute(plaintext_bin, initial_permutation)#perform the initial permutation upon the plaintext

    L = permuted_plaintext[0:32]#split the plaintext into two blocks, L and R
    R = permuted_plaintext[32:]

    key_permutations = permute_key(key, key_permutations_1_C, key_permutations_1_D) #generate all key permutations we need

    for x in range(16): #for sixteen rounds
        new_L = R #L = R
        f_r_k = f_function(R, key_permutations[x])
        new_R = []
        for y in range(32):
            new_R.append(int(L[y]) ^ int(f_r_k[y])) #R = L XOR f(R, K)
        L = new_L
        R = new_R

    preoutput = L + R

    output = permute(preoutput, inverse_initial_permutations)#then, perform the inverse initial permutation

    outfile = open("outfile.txt", "w")#write it to a file
    for element in output:
        outfile.write(str(element))
    outfile.write('\n')
    outfile.close()

else:
    permuted_plaintext = permute(plaintext_bin, initial_permutation)

    L = permuted_plaintext[0:32]
    R = permuted_plaintext[32:]

    key_permutations = permute_key(key, key_permutations_1_C, key_permutations_1_D)

    for x in range(16):
        new_R = L
        f_r_k = f_function(L, key_permutations[15-x])
        new_L = []
        for y in range(32):
            new_L.append(int(R[y]) ^ int(f_r_k[y]))
        L = new_L
        R = new_R

    preoutput = L + R

    output = permute(preoutput, inverse_initial_permutations)

    outfile = open("decryptedOutfile.txt", "w")
    for element in output:
        outfile.write(str(element))
    outfile.write('\n')
    outfile.close()