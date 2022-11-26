from datetime import datetime
from subprocess import list2cmdline
start_time = datetime.now()

#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):
    pqr = pandas.read_excel("octant_input.xlsx")  
    pqr.head()
    pqr["U_Average"] = pqr["U"].mean()     
    pqr["V_Average"] = pqr["V"].mean()
    pqr["W_Average"] = pqr["W"].mean()    #Creating average for coloumns U,V,W 
    pqr["U1"] = pqr["U"]-pqr["U_Average"]   
    pqr["V2"] = pqr["V"]-pqr["V_Average"] 
    pqr["W3"] = pqr["W"]-pqr["W_Average"]   #Creating new columns for U1,V2,W3

    pqr.loc[((pqr.U1 > 0) & (pqr.V2 > 0) & (pqr.W3 >0)), "octant"] = "+1"    #creating octant_ID column,   assigning integers for each octant_ID 
    pqr.loc[((pqr.U1 > 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-1"
    pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 >0)), "octant" ] = "+2"
    pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-2"    
    pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+3"
    pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-3"
    pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+4"
    pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-4"
    pqr.loc[1,""]="input used"

    h =pqr['octant'].value_counts() # total count of number of values for each octant_ID
    pqr.loc[0,"octant_ID"]="total count"  # creating octant_ID column and assigning total count under that.
    pqr.loc[0,"+1"]=h["+1"]      # assigning octant_ID count under all octant_IDs(+1,-1,+2,-2,+3,-3,+4,-4)             
    pqr.loc[0,"-1"]=h["-1"]
    pqr.loc[0,"+2"]=h["+2"] 
    pqr.loc[0,"-2"]=h["-2"]
    pqr.loc[0,"+3"]=h["+3"]
    pqr.loc[0,"-3"]=h["-3"]
    pqr.loc[0,"+4"]=h["+4"]
    pqr.loc[0,"-4"]=h["-4"]
    y=str(mod)
    pqr.loc[1,"octant_ID"]="mod"+" "+y # assigning input label based on the user 
    g=math.ceil(26745/mod) # greatest integer function for identifying 
    e=0000
    l=mod-1
    p=str(e)
    q=str(l)
    for a in range(g) :
      pqr.loc[a+2,"octant_ID"]= p+"-"+q
      e=l+1
      l=l+mod
      p=str(e)
      q=str(l)

    m=0 
    n=0
    o=2
    for a in range(g) : # no of coloumns in the output for each octant_ID 
        for y in range(mod) : #running at each 5000 iterations (0-5000,5001-10000,......25000-30000)
            if pqr["octant"][n]=="+4" : # counting number of +4 octant_ID in range of 0-30000
                m =m+1
            n=n+1
            if n== 26745 : #we have break loop at t=26745 because after 
             break
        pqr.loc[o,"+4"]=m #assigning count of +4 in each coloumn  iterating o
        o=o+1
        m=0
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="-4" :# counting number of -4 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
             break
        pqr.loc[o,"-4"]=m #assygning count of -4 in each coloumn iterating o
        o=o+1
        m=0
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="+3" :# counting number of +3 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"+3"]=m #assigning count of +3 in each coloumn iterating o
        o=o+1
        m=0
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="-3" :# counting number of -3 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"-3"]=m #assigning count of -3 in each coloumn iterating o
        o=o+1
        m=0
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="+2" :# counting number of +2 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"+2"]=m #assigning count of +2 in each coloumn iterating o
        o=o+1
        m=0 
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="-2" :# counting number of -2 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"-2"]=m #assigning count of -2 in each coloumn iterating o
        o=o+1
        m=0
    m=0
    n=0
    o=2
    for a in range(g) :# no of columns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="+1" :# counting number of +1 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"+1"]=m#assigning count of +1 in each coloumn iterating o
        o=o+1
        m=0   
    m=0
    n=0
    o=2
    for a in range(g) :# no of coloumns in the output for each octant_ID
        for y in range(mod) :
            if pqr["octant"][n]=="-1" :# counting number of -1 octant_ID in range of 0-30000
               m =m+1
            n=n+1
            if n== 26745 :
              break
        pqr.loc[o,"-1"]=m #assigning count of -1 in each coloumn iterating o
        o=o+1
        m=0

    list2 = ["+1","-1","+2","-2","+3","-3","+4","-4"]     
    for k in range(0,8):
       list1 = []
       list1.append(pqr.loc[k,"+1"])
       list1.append(pqr.loc[k,"-1"])
       list1.append(pqr.loc[k,"+2"])
       list1.append(pqr.loc[k,"-2"])
       list1.append(pqr.loc[k,"+3"])
       list1.append(pqr.loc [k,"-3"])
       list1.append(pqr.loc[k,"+4"])
       list1.append(pqr.loc[k,"-4"])
       list1.sort(reverse=True)
       #print(list1)
       for j in list2:
          for i in range(0,8):
              if(pqr.loc[k,j]==list1[i]):
                 pqr.loc[k,"rank"+j] = i+1
    
    for k in range(0,8):
       for j in list2:
          if(pqr.loc[k,"rank"+j]==1):
             pqr.loc[k,"Rank1 octant ID"]=j
    
    octant_name_id_mapping = {"+1":"Internal outward interaction", "-1":"External outward interaction", "+2":"External Ejection", "-2":"Internal Ejection", "+3":"External inward interaction", "-3":"Internal inward interaction", "+4":"Internal sweep", "-4":"External sweep"}
    for k in range(0,8):
       for j in list2:
          if(pqr.loc[k,"Rank1 octant ID"]==j):
             pqr.loc[k,"Rank1 octant Name"]=octant_name_id_mapping[j]
  
    for j,k in zip(list2,range(0,8)):
       pqr.loc[11,"+1"]="octant ID"
       pqr.loc[12+k,"+1"]=j
       pqr.loc[11,"-1"]="octant Name"
       pqr.loc[12+k,"-1"]=octant_name_id_mapping[j]
       pqr.loc[11,"+2"]="Count of Rank 1 Mod Values"
    
    for j,k in zip(list2,range(0,8)):
        cnt=0
        for i in range(2,8):
          if(pqr.loc[i,"Rank1 octant ID"]==j):
            cnt=cnt+1
        pqr.loc[12+k,"+2"]=cnt

    pqr.to_excel("octant_output_ranking_excel.xlsx")

    
    

import pandas
import math
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
octant_range_names(mod)



    #This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))