def octact_identification(mod=5000):
    pqr = pandas.read_excel("input_octant_transition_identity.xlsx")
    pqr.loc[0, "U_Avg"] = pqr["U"].mean()
    pqr.loc[0, "V_Avg"] = pqr["V"].mean()
    pqr.loc[0, "W_Avg"] = pqr["W"].mean()
    pqr["U'= U - U_Avg"] = pqr["U"]-pqr.loc[0, "U_Avg"]
    pqr["V'= V - V_Avg"] = pqr["V"]-pqr.loc[0, "V_Avg"]
    pqr["W'= W - W_Avg"] = pqr["W"]-pqr.loc[0, "W_Avg"]
    for x in range(len(pqr)):
        octant(pqr,pqr.loc[x, "U'= U - U_Avg"], pqr.loc[x, "V'= V - V_Avg"], pqr.loc[x, "W'= W - W_Avg"],x)

    pqr.loc[1, "User Input"] = "Mod 5000"
    
    pqr.loc[0, "Octant ID"] = "Overall Count"
    Digits = [1,-1,2,-2,3,-3,4,-4] 
    for x in Digits :
        pqr.loc[0, x] = get_count(pqr,x) 

    M = 30000 #M= mod_maximum_value
    range_value = int(2 + (M)) 
    #print(range_value)
    a = 0
    b = mod
    for y in range(2,range_value):
        print("The a is {} and b is {}".format(a,b))
        pqr.loc[y, "Octant ID"] = str(a)+"-"+str(b)
    for x in Digits:
        pqr.loc[y, x] = get_count(pqr.xloc[a:b],x)
        a = b 
        b = a + mod
    pqr.to_excel("output_octant_transition_identity.xlsx")

def get_count(pqr,value):
    return len(pqr[pqr['Octant'] == value])    

def octant(pqr,a,b,c,x):
    
    if(a >= 0 and b >= 0 and c >= 0) :
        pqr.loc[x, "Octant"] = 1
        
    elif(a >=0 and b >=0 and c < 0) :
        pqr.loc[x, "Octant"] = -1
            
    elif(a < 0 and b >= 0 and c >= 0) :
        pqr.loc[x, "Octant"] = 2
        
    elif(a < 0 and b >=0 and c < 0) :
        pqr.loc[x, "Octant"] = -2
                   
    elif(a < 0 and b < 0 and c >= 0) :
        pqr.loc[x, "Octant"] = 3
        
    elif(a < 0 and b < 0 and c < 0) :
        pqr.loc[x, "Octant"] = -3
            
    elif(a >= 0 and b < 0 and c >= 0) :
        pqr.loc[x, "Octant"] = 4
        
    elif(a >= 0 and b < 0 and c < 0) :
        pqr.loc[x, "Octant"] = -4
        
pqr.loc[11,"Octant ID"]="Overall Transition Count" #creating overall transition count under Octant ID column
pqr.loc[12,"+1"]="To" # creating to column in 12th row from start   
pqr.loc[13,"Octant ID"]="Count"
pqr.loc[13,"+1"]="+1"
pqr.loc[13,"-1"]="-1"
pqr.loc[13,"+2"]="+2"   #assigning (+4 to -4) both rows and columns
pqr.loc[13,"-2"]="-2"
pqr.loc[13,"+3"]="+3"
pqr.loc[13,"-3"]="-3"
pqr.loc[13,"+4"]="+4"
pqr.loc[13,"-4"]="-4"
pqr.loc[14,""]="From"
sushu=27
for i in range(d):   
    pqr.loc[sushu-2,"Octant ID"]="Mod Transition Count"
    pqr.loc[sushu-1,"+1"]="To"
    pqr.loc[sushu,"Octant ID"]="Count"
    pqr.loc[sushu,"+1"]="+1"
    pqr.loc[sushu,"-1"]="-1"
    pqr.loc[sushu,"+2"]="+2"     
    pqr.loc[sushu,"-2"]="-2"
    pqr.loc[sushu,"+3"]="+3"
    pqr.loc[sushu,"-3"]="-3"
    pqr.loc[sushu,"+4"]="+4"
    pqr.loc[sushu,"-4"]="-4"
    pqr.loc[sushu+1,""]="From"
    sushu=sushu+13
sushu=28
for i in range(d): 
    pqr.loc[sushu,"Octant ID"]="+1"
    pqr.loc[sushu+1,"Octant ID"]="-1"
    pqr.loc[sushu+2,"Octant ID"]="+2"    
    pqr.loc[sushu+3,"Octant ID"]="-2"
    pqr.loc[sushu+4,"Octant ID"]="+3"
    pqr.loc[sushu+5,"Octant ID"]="-3"
    pqr.loc[sushu+6,"Octant ID"]="+4"
    pqr.loc[sushu+7,"Octant ID"]="-4"
    sushu=sushu+13
pqr.loc[14,"Octant ID"]="+1"
pqr.loc[15,"Octant ID"]="-1"
pqr.loc[16,"Octant ID"]="+2"
pqr.loc[17,"Octant ID"]="-2"
pqr.loc[18,"Octant ID"]="+3"
pqr.loc[19,"Octant ID"]="-3"
pqr.loc[20,"Octant ID"]="+4"
pqr.loc[21,"Octant ID"]="-4"
for i in range(8) :
    pqr["+1"][i+14]=0
    pqr["-1"][i+14]=0
    pqr["+2"][i+14]=0
    pqr["-2"][i+14]=0
    pqr["+3"][i+14]=0    # filling the all columns (-4 to 4) with 0
    pqr["-3"][i+14]=0
    pqr["+4"][i+14]=0
    pqr["-4"][i+14]=0

import pandas
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)