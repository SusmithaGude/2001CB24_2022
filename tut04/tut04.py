
from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():

    
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

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count_with_range()








#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
