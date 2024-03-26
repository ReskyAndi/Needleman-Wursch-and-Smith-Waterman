
import pandas as pd

dna1 = input("Enter DNA 1 : ")
dna2 = input("Enter DNA 2 : ")

ar_dna1 = list(dna1)
ar_dna2 = list(dna2)
print(ar_dna1)
print(ar_dna2)

len_ar_dna1 = len(ar_dna1)
len_ar_dna2 = len(ar_dna2)
print(len_ar_dna1)
print(len_ar_dna2)

print("The Needleman–Wunsch Algorithm")
print("Value Comparison")
val_dna =[]
d = 7
for i in range(0,len_ar_dna1):
    
    in_val_dna = []
    for j in range(0,len_ar_dna2):
        if i ==0 and j ==0:
            in_val_dna.append(0)
        elif ar_dna2[i] != ar_dna1[j]:
            if ar_dna1[i] == '_' or ar_dna2[j] =='_':
                if (i == 0 and j > 1): 
                    in_val_dna.append(-d *j)
                elif  (i > 1 and j == 0):
                    in_val_dna.append(-d*i)
                else : 
                    in_val_dna.append(-d)
            else:
                in_val_dna.append(-3)
        elif ar_dna2[i] == ar_dna1[j]: 
            in_val_dna.append(5)
    val_dna.append(in_val_dna)
    has_val_dna = val_dna.copy()

datfram_hasval = pd.DataFrame(has_val_dna)
datfram_hasval.index = ar_dna2
datfram_hasval.columns = ar_dna1
print(datfram_hasval)
print()
print("Final Value")
re_val_dna =[]
for m in range(0, len(has_val_dna)):
    new_val_dna = []
    for n  in range(len(has_val_dna)):
        if m == 0 :
            new_val_dna.append(has_val_dna[0][n])
        elif n ==0:
            new_val_dna.append(has_val_dna[m][0])
        else:
            if has_val_dna[m][n]== 5:
                nilai_dna_true = max(has_val_dna[m-1][n-1] + has_val_dna[m][n], has_val_dna[m][n - 1] - d, has_val_dna[m - 1][n] - d)
                has_val_dna[m][n] = nilai_dna_true
                new_val_dna.append(has_val_dna[m][n])
                continue
            elif has_val_dna[m][n]== -3:
                nilai_dna_false = max(has_val_dna[m-1][n-1] + has_val_dna[m][n], has_val_dna[m][n - 1] - d, has_val_dna[m - 1][n] - d)
                has_val_dna[m][n] = nilai_dna_false
                new_val_dna.append(has_val_dna[m][n])
                continue
            else:
                continue
                
    re_val_dna.append(new_val_dna)            

print()
datfram_reval = pd.DataFrame(re_val_dna)
datfram_reval.index = ar_dna2
datfram_reval.columns = ar_dna1
print(datfram_reval)       
        
print()    

print("The Smith-Waterman Algorithm")
print("Value Comparison")
val2_dna =[]
d = 3
for k in range(0,len_ar_dna1):
    
    in_val2_dna = []
    for l in range(0,len_ar_dna2):
        if k ==0 or l ==0:
            in_val2_dna.append(0)
        elif ar_dna2[k] != ar_dna1[l]:
                in_val2_dna.append(-3)
        elif ar_dna2[k] == ar_dna1[l]: 
            in_val2_dna.append(5)
    val2_dna.append(in_val2_dna)
    has_val2_dna = val2_dna.copy()

datfram_hasval2 = pd.DataFrame(has_val2_dna)
datfram_hasval2.index = ar_dna2
datfram_hasval2.columns = ar_dna1
print(datfram_hasval2)
print()
print("Final Value")
re_val2_dna =[]
for r in range(0, len(has_val2_dna)):
    new_val2_dna = []
    for s  in range(len(has_val2_dna)):
        if r == 0 :
            new_val2_dna.append(has_val2_dna[0][s])
        elif s ==0:
            new_val2_dna.append(has_val2_dna[r][0])
        else:
            if has_val2_dna[r][s]== 5:
                nilai2_dna_true = max(0,has_val2_dna[r-1][s-1] + has_val2_dna[r][s], has_val2_dna[r][s - 1] - d, has_val2_dna[r - 1][s] - d)
                has_val2_dna[r][s] = nilai2_dna_true
                new_val2_dna.append(has_val2_dna[r][s])
                continue
            elif has_val2_dna[r][s]== -3:
                nilai2_dna_false = max(0,has_val2_dna[r-1][s-1] + has_val2_dna[r][s], has_val2_dna[r][s - 1] - d, has_val2_dna[r - 1][s] - d)
                has_val2_dna[r][s] = nilai2_dna_false
                new_val2_dna.append(has_val2_dna[r][s])
                continue
            else:
                continue
                
    re_val2_dna.append(new_val2_dna)            

print()
datfram_reval2 = pd.DataFrame(re_val2_dna)
datfram_reval2.index = ar_dna2
datfram_reval2.columns = ar_dna1
print(datfram_reval2)       
        
print()    










