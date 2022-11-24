
from datetime import datetime

start_time = datetime.now()
#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
    pqr1 = pandas.read_excel("input_octant_longest_subsequence_with_range.xlsx")
      
    pqr1.head()
    pqr1["U_Average"] = pqr1["U"].mean()    
    pqr1["V_Average"] = pqr1["V"].mean()
    pqr1["W_Average"] = pqr1["W"].mean()
    pqr1["U1"] = pqr1["U"]-pqr1["U_Average"]  
    pqr1["V2"] = pqr1["V"]-pqr1["V_Average"] 
    pqr1["W3"] = pqr1["W"]-pqr1["W_Average"] 

    pqr1.loc[((pqr1.U1 > 0) & (pqr1.V2 > 0) & (pqr1.W3 >0)), "octant"] = "+1" 
    pqr1.loc[((pqr1.U1 > 0) &(pqr1.V2 > 0) & (pqr1.W3 <0)), "octant" ] = "-1"
    pqr1.loc[((pqr1.U1 < 0) &(pqr1.V2 > 0) & (pqr1.W3 >0)), "octant" ] = "+2"
    pqr1.loc[((pqr1.U1 < 0) &(pqr1.V2 > 0) & (pqr1.W3 <0)), "octant" ] = "-2"    
    pqr1.loc[((pqr1.U1 < 0) &(pqr1.V2 < 0) & (pqr1.W3 >0)), "octant" ] = "+3"
    pqr1.loc[((pqr1.U1 < 0) &(pqr1.V2 < 0) & (pqr1.W3 <0)), "octant" ] = "-3"
    pqr1.loc[((pqr1.U1 > 0) &(pqr1.V2 < 0) & (pqr1.W3 >0)), "octant" ] = "+4"
    pqr1.loc[((pqr1.U1 > 0) &(pqr1.V2 < 0) & (pqr1.W3 <0)), "octant" ] = "-4"
    pqr1.loc[1,""]="input used"

    pqr1[" "] = " "
    pqr1["octant "] = " "  
    arr = ["+1", "-1", "+2", "-2", "+3", "-3", "+4", "-4"]
    for h in range(8):
        pqr1.loc[h, "octant "] = arr[h]  

    pqr1["Longest Subsequence Length"] = " "
    pqr1["Count"] = " "

    k = len(pqr1)  
    b= 0
    minimum_num = [0]*8  
    maximum_num = [0]*8  
    d1 = {"+1": 0, "-1": 1, "+2": 2, "-2": 3,"+3": 4, "-3": 5, "+4": 6, "-4": 7}  
    range_of_time = []
    for h in range(8):
        range_of_time.append([])

    while (b < k):
        s1 = pqr1.at[b, "octant"]
        count = 0
        z = b
        while (1):             
            if (z >= k or pqr1.at[z, "octant"] != s1):
                break
            count += 1
            z += 1

        b += count
        var = minimum_num[d1[s1]]      
        minimum_num[d1[s1]] = max(minimum_num[d1[s1]], count)

        if (count > var):
            maximum_num[d1[s1]] = 1
            if(len(range_of_time[d1[s1]])==0):
                range_of_time[d1[s1]].append(z-1)
            else:
                range_of_time[d1[s1]].clear()
                range_of_time[d1[s1]].append(z-1)
                   
        if (count == var):
            maximum_num[d1[s1]] += 1
            range_of_time[d1[s1]].append(z-1)

    for h in range(8):
        pqr1.loc[h, "Longest Subsequence Length"] = minimum_num[h]

    for z in range(8):
        pqr1.loc[z, "Count"] = maximum_num[z]

    pqr1["  "] = " "
    pqr1[" octant "] = " "
    pqr1[" Longest Subsequence Length"] = " "
    pqr1[" Count"] = " "
    print(range_of_time)

    t=0
    for h in range(8):
        pqr1.loc[t," octant "]=arr[h]
        pqr1.loc[t," Longest Subsequence Length"]=minimum_num[h]
        pqr1.loc[t," Count"]=maximum_num[h]
        t+=1
        pqr1.loc[t," octant "]="Time"
        pqr1.loc[t," Longest Subsequence Length"]="From"
        pqr1.loc[t," Count"]="To"
        t+=1
        for z in range(maximum_num[h]):
            pqr1.loc[t," Longest Subsequence Length"]=0.01*(range_of_time[d1[arr[h]]][z])-0.01*(minimum_num[h]-1)
            pqr1.loc[t," Count"]=0.01*range_of_time[d1[arr[h]]][z]
            t+=1

    pqr1.to_excel('output_octant_longest_subsequence_with_range.xlsx', index=False)
    

from platform import python_version

import pandas

ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmzw")


octant_longest_subsequence_count_with_range()








#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))