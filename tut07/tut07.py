
from datetime import datetime
start_time = datetime.now()

#Help

##Read all the excel files in a batch format from the input/ folder. Only xlsx to be allowed
##Save all the excel files in a the output/ folder. Only xlsx to be allowed
## output filename = input_filename[_octant_analysis_mod_5000].xlsx , ie, append _octant_analysis_mod_5000 to the original filename. 

def octant_analysis(mod=5000):
    pqr1 = pandas.read_excel(r"input\1.0.xlsx")
    pqr2 = pandas.read_excel(r"input\2.0.xlsx")
    pqr3 = pandas.read_excel(r"input\2.5.xlsx")
    pqr4 = pandas.read_excel(r"input\3.0.xlsx")
    pqr5 = pandas.read_excel(r"input\3.4.xlsx")
    pqr6 = pandas.read_excel(r"input\3.7.xlsx")
    pqr7 = pandas.read_excel(r"input\4.0.xlsx")
    pqr8 = pandas.read_excel(r"input\4.2.xlsx")
    pqr9 = pandas.read_excel(r"input\4.4.xlsx")
    pqr10 = pandas.read_excel(r"input\4.6.xlsx")
    pqr11 = pandas.read_excel(r"input\4.7.xlsx")
    pqr12 = pandas.read_excel(r"input\4.8.xlsx")
    pqr13 = pandas.read_excel(r"input\4.9.xlsx")
    pqr14 = pandas.read_excel(r"input\5.0.xlsx")
    pqr15 = pandas.read_excel(r"input\5.1.xlsx")
    pqr16 = pandas.read_excel(r"input\5.2.xlsx")
    pqr17 = pandas.read_excel(r"input\5.3.xlsx")
    pqr18 = pandas.read_excel(r"input\surface.xlsx")


    
    inputfiles = [pqr1,pqr2,pqr3,pqr4,pqr5,pqr6,pqr7,pqr8,pqr9,pqr10,pqr11,pqr12,pqr13,pqr14,pqr15,pqr16,pqr17,pqr18]
    outputfiles= [r"output\1.0_octant_analysis_mod_5000.xlsx",r"output\2.0_octant_analysis_mod_5000.xlsx",
                  r"output\2.5_octant_analysis_mod_5000.xlsx",r"output\3.0_octant_analysis_mod_5000.xlsx",
                  r"output\3.4_octant_analysis_mod_5000.xlsx",r"output\3.7_octant_analysis_mod_5000.xlsx",
                  r"output\4.0_octant_analysis_mod_5000.xlsx",r"output\4.2_octant_analysis_mod_5000.xlsx",
                  r"output\4.4_octant_analysis_mod_5000.xlsx",r"output\4.6_octant_analysis_mod_5000.xlsx",
                  r"output\4.7_octant_analysis_mod_5000.xlsx",r"output\4.8_octant_analysis_mod_5000.xlsx",
                  r"output\4.9_octant_analysis_mod_5000.xlsx",r"output\5.0_octant_analysis_mod_5000.xlsx",
                  r"output\5.1_octant_analysis_mod_5000.xlsx",r"output\5.2_octant_analysis_mod_5000.xlsx",
                  r"output\5.3_octant_analysis_mod_5000.xlsx",r"input\surface_octant_analysis_mod_5000.xlsx"]

    for pqr,out in zip(inputfiles,outputfiles):
        pqr.loc[0, "U Avg"] = pqr["U"].mean()
        pqr.loc[0, "V Avg"] = (pqr["V"].mean())
        pqr.loc[0, "W Avg"] = (pqr["W"].mean())
        pqr["U'=U - U avg"] = (pqr["U"]-pqr.loc[0, "U Avg"])
        pqr["V'=V - V avg"] = (pqr["V"]-pqr.loc[0, "V Avg"])
        pqr["W'=W - W avg"] = (pqr["W"]-pqr.loc[0, "W Avg"])

        for i in range(len(pqr)):
            octant(pqr,pqr.loc[i, "U'=U - U avg"], pqr.loc[i, "V'=V - V avg"],pqr.loc[i, "W'=W - W avg"],i)

        pqr.loc[1, "User Input"] = "Mod 5000"
        
        pqr.loc[0, "Octant ID"] = "Overall Count"
        q_list = [1,-1,2,-2,3,-3,4,-4]
        for i in q_list:
            pqr.loc[0, i] = get_count(pqr,i)

        mod_max_value = 20000
        range_value = int(2 + (mod_max_value/mod))
        print(range_value)
        x = 0
        y = mod
        for j in range(2,range_value):
            print("The x is {} and Y is {}".format(x,y))
            pqr.loc[j, "Octant ID"] = str(x)+"-"+str(y-1)
            for i in q_list:
                pqr.loc[j, i] = get_count(pqr.iloc[x:y],i)
            x = y
            y = x + mod
        pqr.loc[5, "Octant ID"] = str(x-mod-1)+"-"+"Last Index"
        
        #ranking the values
        octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
        for j in range(0,range_value):
            get_rank(pqr,j,q_list)
        
        for i,j in zip(q_list,range(0,8)):
            pqr.loc[range_value+2,1] = "Octant ID"
            pqr.loc[range_value+2,-1] = "Octant Name"
            pqr.loc[range_value+2,2] = "Count of Rank 1 Mod Values"
            pqr.loc[range_value+3+j,1] = i
            pqr.loc[range_value+3+j,-1] = octant_name_id_mapping[str(i)]
            count = 0
            for x in range(2,range_value):
                if(pqr.loc[x,"Rank1 Octant ID"]==i):
                    count+=1
            pqr.loc[range_value+3+j,2] = count
        

        # Overall Transition Count 
        columns = ["A","B","C","D","E","F","G","H"]
        pqr.loc[2," "] = "From"
        pqr.loc[1,"Overall Transition Count"] = "Count"
        pqr.loc[0,"A"] = "To"
        for j,i in zip(range(0,8),q_list):
                pqr.loc[j+2,"Overall Transition Count"] = i     
        for j,i in zip(columns,q_list):
            pqr.loc[1, j] = i

        pqr['C']=pqr['Octant'].shift(-1)
        group=pqr.groupby(['Octant','C'])
        counts = {i[0]:len(i[1]) for i in group}
        print(counts)
        # prints overall transition count of each octant in the output file
        matrix=pandas.DataFrame()
        for i in q_list:
            matrix[str(i)]=pandas.Series([counts.get((i,j),0) for j in q_list], index = q_list)
        print(matrix)
        print("     ")

        pqr1 = matrix
        for x in range(0,8):
                for i,y in zip(columns,range(0,8)):
                    pqr.loc[x+2,i] = pqr1.iloc[x,y]

        # prints overall transition count of each octant for mod ranges in the output file
        n=mod_max_value//mod
        for i in range(0,n):
            print("The x is {} and Y is {}".format(i*mod,(i+1)*mod))
            pqr.loc[12+(i*12), "Overall Transition Count"] = str(i*mod)+"-"+str((i+1)*mod)
            pqr.loc[11+(i*12),"Overall Transition Count"] = "Mod Transition Count"
            pqr.loc[14+(i*12), " "] = "From"
            pqr.loc[12+(i*12), "A"] = "To"
            pqr.loc[13+(i*12),"Overall Transition Count"] = "Count"
            for j,k in zip(range(12,20),q_list):
                pqr.loc[2+j+(i*12),"Overall Transition Count"] = k     
            for j,k in zip(columns,q_list):
                pqr.loc[13+(i*12), j] = k

            pqr['C']=pqr['Octant'][i*mod:(i+1)*mod].shift(-1)
            groups=pqr.groupby(['Octant','C'])
            counts = {i[0]:len(i[1]) for i in groups}

            matrix=pandas.DataFrame()
            for t in q_list:
                matrix[str(t)]=pandas.Series([counts.get((t,r),0) for r in q_list], index = q_list)
            print(matrix)
            print("     ")

            pqr2 = matrix
            for x in range(0,8):
                for k,y in zip(columns,range(0,8)):
                    pqr.loc[x+14+(i*12),k] = pqr2.iloc[x,y]
        #remove the extra column made 
        pqr.drop(['C'],axis=1,inplace = True)


        #longest subsequent lengths and their ranges
        counts = 1
        for i in range(0,len(pqr["Octant"])-1):
            if(pqr.loc[i,"Octant"] == pqr.loc[i+1,"Octant"]):
                pqr.loc[i,"update"] = counts
                counts=counts+1
            else:
                pqr.loc[i,"update"] = counts
                counts = 1
        pqr.loc[len(pqr["Octant"])-1,"update"] = counts


        for x,y in zip(range(0,8),q_list):
            pqr.loc[x,"Octant_num"] = y
        
        for x,y in zip(range(0,8),q_list):
            pqr.loc[x,"Longest Subsequence Length"] = get_max_count(pqr,y)
        
        for x,y in zip(range(0,8),q_list):
            pqr.loc[x,"Count"] = count_of_max_count(pqr,y)
        
        pqr["-"] = " "
        for x,y in zip(range(0,8),q_list):
            get_time_range(x,pqr,pqr.loc[x,"Longest Subsequence Length"],y,pqr.loc[x,"Count"])
        
        pqr.drop(['update'],axis=1,inplace=True)

        # pqr.insert(11," "," ")
        # pqr.insert(32," "," ")
        # pqr.insert(42," "," ")
        #save to output files
        pqr.to_excel(out,index=False)

#functions
# def highlight_cells(val):
#     color = 'yellow' if val == 1 else ''
#     return 'background-color: {}'.format(color)
# pqr.style.applymap(highlight_cells)

def get_rank(pqr,column_no,q_list):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    octant_count = []
    for i in q_list:
        octant_count.append(pqr.loc[column_no,i]) 
    octant_count.sort(reverse=True)

    for i in q_list:
        for x in range(0,8):
            if(octant_count[x]==pqr.loc[column_no,i]):
                pqr.loc[column_no,"Rank Octant "+str(i)] = x+1
    
    for i in q_list:
        if(pqr.loc[column_no,"Rank Octant "+str(i)]==1):
            pqr.loc[column_no,"Rank1 Octant ID"] = i
            pqr.loc[column_no,"Rank1 Octant Name"]=octant_name_id_mapping[str(i)]
    
    for i in q_list:
        val = pqr.loc[column_no,"Rank Octant "+str(i)]
        #pqr.style.apply(lambda val:['background:yellow' if val == 1 else " "],axis =0)
        # color = 'yellow' if val == 1 else ''
        # return 'background-color: {}'.format(color)
        pqr.style.applymap(lambda:['background-color:yellow' if val == 1 else ''],axis=0)


def get_count(pqr,value):
    return len(pqr[pqr['Octant'] == value]) 

def octant(pqr,x,y,z,i):
    
    if(x >= 0 and y >= 0 and z >= 0) :
        pqr.loc[i, "Octant"] = 1
    elif (x < 0 and y >= 0 and z >= 0) :
        pqr.loc[i, "Octant"] = 2
            
    elif(x < 0 and y < 0 and z >= 0) :
        pqr.loc[i, "Octant"] = 3
            
    elif(x >= 0 and y < 0 and z >= 0) :
        pqr.loc[i, "Octant"] = 4
            
    elif(x >= 0 and y >= 0 and z < 0) :
        pqr.loc[i, "Octant"] = -1
            
    elif(x < 0 and y >= 0 and z < 0) :
        pqr.loc[i, "Octant"] = -2
            
    elif(x < 0 and y < 0 and z < 0) :
        pqr.loc[i, "Octant"] = -3
            
    elif(x >= 0 and y < 0 and z < 0) :
        pqr.loc[i, "Octant"] = -4
	
def get_max_count(pqr,value):
    max_val = 0 
    for j in range(0,len(pqr["Octant"])-1):
        if(pqr.loc[j, "Octant"]==value):
            val = pqr.loc[j, "update"] 
            max_val = max(max_val,val)
    return max_val  

def count_of_max_count(pqr,value):
    z = get_max_count(pqr,value)
    count=0
    for j in range(0,len(pqr["Octant"])-1):
        if(pqr.loc[j, "Octant"]==value):
           if(pqr.loc[j, "update"]==z):
              count = count+1
    print("The maximum value is {} and The count is {}".format(z,count))
    return count     

def get_time_range(x,pqr,max_val,value,count):
    list_of_index = []
    for j in range(0,len(pqr["Octant"])-1):
        if(pqr.loc[j, "Octant"]==value):
            if(pqr.loc[j, "update"]==max_val):
                list_of_index.append(j)
    maximum_time = []
    minimum_time = []
    for j in list_of_index:
        maximum_time.append(pqr.loc[j, "T"])
    for j in list_of_index:
        minimum_time.append(pqr.loc[j-max_val+1, "T"])

    length=0
    if(value!=1):
      for i in range(0,x):
            length = length+pqr.loc[i,"Count"]+2
    pqr.loc[length,"octant_num"] = value
    pqr.loc[length,"longest subsequence length"] = max_val
    pqr.loc[length,"count"] = count
    pqr.loc[length+1,"octant_num"] = "Time"
    pqr.loc[length+1,"longest subsequence length"] = "From"
    pqr.loc[length+1,"count"] = "To"
    for i in range(0,len(maximum_time)):
        pqr.loc[i+length+2,"longest subsequence length"],pqr.loc[i+length+2,"count"] = round(minimum_time[i],3),round(maximum_time[i],3)
                   
    print("The max_value is {} Minimim time {} and the Maximum time {}".format(max_val,minimum_time,maximum_time))
    

###Code
import pandas
from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000
octant_analysis(mod)






#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))