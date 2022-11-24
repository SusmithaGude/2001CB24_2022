

from datetime import datetime
start_time =datetime.now()

def octant_longest_subsequence_count():
  import pandas
  import math
  pqr = pandas.read_excel("input_octant_longest_subsequence.xlsx")  
  pqr.head()
  pqr["U_Average"] = pqr["U"].mean()     #Creating average for coloumns U,V,W 
  pqr["V_Average"] = pqr["V"].mean()
  pqr["W_Average"] = pqr["W"].mean()
  pqr["U1"] = pqr["U"]-pqr["U_Average"]  # Creating new columns for U1,V2,W3 
  pqr["V2"] = pqr["V"]-pqr["V_Average"] 
  pqr["W3"] = pqr["W"]-pqr["W_Average"] 

  pqr.loc[((pqr.U1 > 0) & (pqr.V2 > 0) & (pqr.W3 >0)), "octant"] = "+1"   #creating octant_ID column,   assigning integers for each octant_ID
  pqr.loc[((pqr.U1 > 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-1"
  pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 >0)), "octant" ] = "+2"
  pqr.loc[((pqr.U1 < 0) &(pqr.V2 > 0) & (pqr.W3 <0)), "octant" ] = "-2"    
  pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+3"
  pqr.loc[((pqr.U1 < 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-3"
  pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 >0)), "octant" ] = "+4"
  pqr.loc[((pqr.U1 > 0) &(pqr.V2 < 0) & (pqr.W3 <0)), "octant" ] = "-4"    
 
  octant = ["+1","-1","+2","-2","+3","-3","+4","-4"]
  x = len(pqr["octant"])
  counts =1
  for j in range(0,x-1):
       if(pqr.loc[j,"octant"] == pqr.loc[j+1,"octant"]):
          pqr.loc[j,"XYZ"]=counts
          counts = counts+1
       else:
          pqr.loc[j,"XYZ"]=counts
          counts = 1
  pqr.loc[x-1,"XYZ"]=counts
  for j,i in zip(octant,range(0,8)):
    m = 0
    for z in range(0,x-1):
      if(pqr.loc[z,'octant']==j):
         c = pqr.loc[z,'XYZ']
         m = max(m,c)
    count=0
    for p in range(0,x-1):
      if((pqr.loc[p,'octant']==j)and(m==pqr.loc[p,'XYZ'])):
        count = count+1
    pqr.loc[i,'COUNT']=j
    pqr.loc[i,"Longest_Subsequence_Length"] = m 
    pqr.loc[i,'count']= count

  pqr.drop(['XYZ'],axis=1)
  pqr.to_excel("output_octant_longest_subsequence.xlsx")
    
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