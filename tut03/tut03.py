

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
    
 import pandas as pd
 import math
 pqr = pd.read_excel("input_octant_longest_subsequence.xlsx")  # reading the input file
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
        if m== 29745 : #we have break loop at m=29745 
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

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
