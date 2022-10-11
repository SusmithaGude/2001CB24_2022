import pandas as pd
import math
pqr = pd.read_excel("input_octant_transition_identify.xlsx")  # reading the input file
pqr.head()
pqr["U_Average"] = pqr["U"].mean()    
pqr["V_Average"] = pqr["V"].mean()
pqr["W_Average"] = pqr["W"].mean()  # making average for U,V,W columns
pqr["U1"] = pqr["U"]-pqr["U_Average"]  
pqr["V2"] = pqr["V"]-pqr["V_Average"] 
pqr["W3"] = pqr["W"]-pqr["W_Average"]  # making new columns for U1,V2,W3

pqr.loc[((pqr.U1 > 0) & (pqr.V2 > 0) & (pqr.W3 >0)), "octant"] = "+1" 
pqr.loc[((pqr.U1 > 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-1"
pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 >0)), "octant" ] = "+2"
pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-2"   
pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+3"
pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-3"
pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+4"
pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-4"  # making octant column, assigning integers for each octant 
pqr.loc[1,""]="given input"

A =pqr['octant'].value_counts() # total count of number of values for each octant
pqr.loc[0,"overall id"]="overall count"  # making overall id column and assigning overall count under that
pqr.loc[0,"+1"]=A["+1"]                   
pqr.loc[0,"-1"]=A["-1"]
pqr.loc[0,"+2"]=A["+2"] 
pqr.loc[0,"-2"]=A["-2"]
pqr.loc[0,"+3"]=A["+3"]
pqr.loc[0,"-3"]=A["-3"]
pqr.loc[0,"+4"]=A["+4"]
pqr.loc[0,"-4"]=A["-4"]      # giving overall count under all octants(+1,+2,+3,+4,-1,-2,-3,-4)
mod=5000
B=str(mod)
pqr.loc[1,"overall id"]="mod"+" "+B # assigning input label based on the user 
d=math.ceil(29745/mod) # greatest integer function for identifing 
k=0000
l=mod-1
p=str(k)
q=str(l)
for j in range(d) :
  pqr.loc[j+2,"overall id"]= p+"-"+q
  k=l+1
  l=l+mod
  p=str(k)
  q=str(l)

l=0 
m=0
n=2
for j in range(d) : # no of coloumns in the output for each octant 
    for x in range(mod) : #running at each 5000 iterations (0-5000,5001-10000,......25000-30000)
        if pqr["octant"][m]=="+4" : # counting number of +4 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 : #we have break loop at m=29745 because after 
          break
    pqr.loc[n,"+4"]=l #assigning count of +4 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="-4" :# counting number of -4 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"-4"]=l #assigning count of -4 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="+3" :# counting number of +3 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"+3"]=l #assigning count of +3 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="-3" :# counting number of -3 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"-3"]=l #assigning count of -3 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="+2" :# counting number of +2 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"+2"]=l #assigning count of +2 in each coloumn by iterating n
    n=n+1
    l=0
    j=7 
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="-2" :# counting number of -2 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"-2"]=l #assigning count of -2 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="+1" :# counting number of +1 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"+1"]=l#assigning count of +1 in each coloumn by iterating n
    n=n+1
    l=0
    j=7    
l=0
m=0
n=2
for j in range(d) :# no of coloumns in the output for each octant
    for x in range(mod) :
        if pqr["octant"][m]=="-1" :# counting number of -1 octant in range of 0-30000
           l =l+1
        m=m+1
        if m== 29745 :
          break
    pqr.loc[n,"-1"]=l #assigning count of -1 in each coloumn by iterating n
    n=n+1
    l=0
    j=7
pqr.loc[11,"overall id"]="Overall Transition Count" #making overall transition count under overall id column
pqr.loc[12,"+1"]="To" # making to column in 12th row from start   
pqr.loc[13,"overall id"]="Count"
pqr.loc[13,"+1"]="+1"
pqr.loc[13,"-1"]="-1"
pqr.loc[13,"+2"]="+2"   #assigning (+4 to -4) both rows and columns
pqr.loc[13,"-2"]="-2"
pqr.loc[13,"+3"]="+3"
pqr.loc[13,"-3"]="-3"
pqr.loc[13,"+4"]="+4"
pqr.loc[13,"-4"]="-4"
pqr.loc[14,""]="From"
cat=27
for x in range(d):   
    pqr.loc[cat-2,"overall id"]="Mod Transition Count"
    pqr.loc[cat-1,"+1"]="To"
    pqr.loc[cat,"overall id"]="Count"
    pqr.loc[cat,"+1"]="+1"
    pqr.loc[cat,"-1"]="-1"
    pqr.loc[cat,"+2"]="+2"     
    pqr.loc[cat,"-2"]="-2"
    pqr.loc[cat,"+3"]="+3"
    pqr.loc[cat,"-3"]="-3"
    pqr.loc[cat,"+4"]="+4"
    pqr.loc[cat,"-4"]="-4"
    pqr.loc[cat+1,""]="From"
    cat=cat+13
cat=28
for x in range(d): 
    pqr.loc[cat,"overall id"]="+1"
    pqr.loc[cat+1,"overall id"]="-1"
    pqr.loc[cat+2,"overall id"]="+2"    
    pqr.loc[cat+3,"overall id"]="-2"
    pqr.loc[cat+4,"overall id"]="+3"
    pqr.loc[cat+5,"overall id"]="-3"
    pqr.loc[cat+6,"overall id"]="+4"
    pqr.loc[cat+7,"overall id"]="-4"
    cat=cat+13
pqr.loc[14,"overall id"]="+1"
pqr.loc[15,"overall id"]="-1"
pqr.loc[16,"overall id"]="+2"
pqr.loc[17,"overall id"]="-2"
pqr.loc[18,"overall id"]="+3"
pqr.loc[19,"overall id"]="-3"
pqr.loc[20,"overall id"]="+4"
pqr.loc[21,"overall id"]="-4"
for x in range(8) :
    pqr["+1"][x+14]=0
    pqr["-1"][x+14]=0
    pqr["+2"][x+14]=0
    pqr["-2"][x+14]=0
    pqr["+3"][x+14]=0    # filling the all columns (-4 to 4) with 0
    pqr["-3"][x+14]=0
    pqr["+4"][x+14]=0
    pqr["-4"][x+14]=0
k=0000
l=mod-1
p=str(k)
q=str(l)
bal=26
for j in range(d) :
  pqr.loc[bal,"overall id"]= p+"-"+q  #assigning range  from total count(0-4999 ......25000-29999 ) if mode is 5000
  k=l+1
  l=l+mod
  p=str(k)
  q=str(l)
  bal=bal+13

rows, columns = (9, 9) # assigning rows and column variables 
arr = [[0 for x in range(columns)] for j in range(rows)] # making array with all zeros with 9 rows 9 columns
for ban in range(29744) : 
    arr[int(pqr["octant"][ban])+4][int(pqr["octant"][ban+1])+4]=arr[int(pqr["octant"][ban])+4][int(pqr["octant"][ban+1])+4]+1 #count of all ranges is stored in array ,we add +4 to avoid negative index in array
C=5    
for x in range(8) :
    if(x%2==0) :
      pqr["+1"][x+14]=arr[C][5]               # count of +1 - +1 is stored in arr[4+1][4+1]   [adding 4 to each index +1,-1,+2,-2,+3,-3,+4,-4]
    if(x%2!=0) :                             # count of +1 - -1 is stored in arr[4+1][4-1]
       C=8-C                                 # count of +1 - +2 is stored in arr[4+1][2+4]
       pqr["+1"][x+14]=arr[C][5]              # count of +1 - -2 is stored in arr[1+4][-2+4]
       C=8-C                                 # count of +1 - +3 is stored in arr[4+1][3+4]
       C=C+1                                 # count of +1 - -3 is stored in arr[4+1][-3+4]
C=5                                          # count of +1 - +4 is stored in arr[4+1][4+4]
for x in range(8) :                          # count of +1 - -4 is stored in arr[4+1][-4+4]
    if(x%2==0) :
      pqr["-1"][x+14]=arr[C][3]
    if(x%2!=0) :                             # count of +2 - +1 is stored in arr[4+2][1+4]
       C=8-C                                 # count of +2 - -1 is stored in arr[4+2][-1+4]
       pqr["-1"][x+14]=arr[C][3]              # count of +2 - +2 is stored in arr[4+2][2+4]
       C=8-C                                 # count of +2 - -2 is stored in arr[4+2][-2+4]
       C=C+1                                 # count of +2 - +3 is stored in arr[4+2][3+4]
C=5                                          # count of +2 - -3 is stored in arr[4+2][-3+4]
for x in range(8) :                          # count of +2 - +4 is stored in arr[4+2][4+4]
    if(x%2==0) :                             # count of +2 - -4 is stored in arr[4+2][-4+4]
      pqr["+2"][x+14]=arr[C][6]
    if(x%2!=0) :
       C=8-C
       pqr["+2"][x+14]=arr[C][6]              # count of +3 - +1 is stored in arr[4+3][1+4]
       C=8-C                                 # count of +3 - -1 is stored in arr[4+3][-1+4]
       C=C+1                                 # count of +3 - +2  is stored in arr[4+3][2+4]
C=5                                          # count of +3 - -2  is stored in arr[4+3][-2+4]
for x in range(8) :                          # count of +3 - +3  is stored in arr[4+3][3+4]
    if(x%2==0) :                             # count of +3 - -3  is stored in arr[4+3][-3+4]
      pqr["-2"][x+14]=arr[C][2]               # count of +3 - +4  is stored in arr[4+3][4+4]
    if(x%2!=0) :                             # count of +3 - -4  is stored in arr[4+3][-4+4]
       C=8-C
       pqr["-2"][x+14]=arr[C][2]
       C=8-C
       C=C+1

C=5                                          # count of +4 - +1  is stored in arr[4+4][1+4]
for x in range(8) :                          # count of +4 - -1  is stored in arr[4+4][-1+4]
    if(x%2==0) :                             # count of +4 - +2  is stored in arr[4+4][2+4]
      pqr["+3"][x+14]=arr[C][7]               # count of +4 - -2  is stored in arr[4+4][-2+4]
    if(x%2!=0) :                             # count of +4 - +3  is stored in arr[4+4][3+4]
       C=8-C                                 # count of +4 - -3  is stored in arr[4+4][-3+4]
       pqr["+3"][x+14]=arr[C][7]              # count of +4 - +4  is stored in arr[4+4][4+4]
       C=8-C                                 # count of +4 - -4  is stored in arr[4+4][-4+4]
       C=C+1

C=5
for x in range(8) :
    if(x%2==0) :
      pqr["-3"][x+14]=arr[C][1]
    if(x%2!=0) :
       C=8-C
       pqr["-3"][x+14]=arr[C][1]
       C=8-C
       C=C+1
C=5
for x in range(8) :
    if(x%2==0) :
      pqr["+4"][x+14]=arr[C][8]
    if(x%2!=0) :
       C=8-C
       pqr["+4"][x+14]=arr[C][8]
       C=8-C
       C=C+1
C=5
for x in range(8) :
    if(x%2==0) :
      pqr["-4"][x+14]=arr[C][0]
    if(x%2!=0) :
       C=8-C
       pqr["-4"][x+14]=arr[C][0]
       C=8-C
       C=C+1

bank=0
f=28
for xk in range(d) :
    rows, columns = (9, 9)
    arr = [[0 for x in range(columns)] for j in range(rows)]
    for j in range(mod) :
        arr[int(pqr["octant"][bank])+4][int(pqr["octant"][bank+1])+4]=arr[int(pqr["octant"][bank])+4][int(pqr["octant"][bank+1])+4]+1
        bank=bank+1
        if bank>=29744 :
            break
        C=5    
    for xb1 in range(8) :
            if(xb1%2==0) :
               pqr["+1"][xb1+k]=arr[C][5]
            if(xb1%2!=0) :                   # counting +1 with all other values(-4 to 4) in all modes of transition count 
               C=8-C
               pqr["+1"][xb1+k]=arr[C][5]
               C=8-C
               C=C+1
    C=5    
    for xb2 in range(8) :
            if(xb2%2==0) :
               pqr["-1"][xb2+k]=arr[C][3]
            if(xb2%2!=0) :                      # counting -1 with all other values(-4 to 4) in all modes of transition count
               C=8-C
               pqr["-1"][xb2+k]=arr[C][3]
               C=8-C
               C=C+1
    C=5    
    for xb3 in range(8) :
            if(xb3%2==0) :
               pqr["+2"][xb3+k]=arr[C][6]
            if(xb3%2!=0) :                      # counting +2 with all other values(-4 to 4) in all modes of transition count 
               C=8-C
               pqr["+2"][xb3+k]=arr[C][6]
               C=8-C
               C=C+1
    C=5    
    for xb4 in range(8) :
            if(xb4%2==0) :
               pqr["-2"][xb4+k]=arr[C][2]
            if(xb4%2!=0) :                           # counting -2 with all other values(-4 to 4) in all modes of transition count
               C=8-C
               pqr["-2"][xb4+k]=arr[C][2]
               C=8-C
               C=C+1
    C=5    
    for xb5 in range(8) :
            if(xb5%2==0) :
               pqr["+3"][xb5+k]=arr[C][7]              # counting +3 with all other values(-4 to 4) in all modes of transition count
            if(xb5%2!=0) :
               C=8-C
               pqr["+3"][xb5+k]=arr[C][7]
               C=8-C
               C=C+1
    C=5    
    for xb6 in range(8) :
            if(xb6%2==0) :
               pqr["-3"][xb6+k]=arr[C][1]
            if(xb6%2!=0) :                              # counting -3 with all other values(-4 to 4) in all modes of transition count
               C=8-C
               pqr["-3"][xb6+k]=arr[C][1]
               C=8-C
               C=C+1
    C=5    
    for xb7 in range(8) :
            if(xb7%2==0) :
               pqr["+4"][xb7+k]=arr[C][8]                  # counting +4 with all other values(-4 to 4) in all modes of transition count
            if(xb7%2!=0) :
               C=8-C
               pqr["+4"][xb7+k]=arr[C][8]
               C=8-C
               C=C+1
    C=5    
    for xb8 in range(8) :
            if(xb8%2==0) : 
               pqr["-4"][xb8+k]=arr[C][0]
            if(xb8%2!=0) :                                  # counting -4 with all other values(-4 to 4) in all modes of transition count
               C=8-C
               pqr["-4"][xb8+k]=arr[C][0]
               C=8-C
               C=C+1       
         
    f=f+13
print(pqr)
pqr.to_excel("output_octant_transition_identify.xlsx")