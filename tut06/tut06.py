


from datetime import datetime
start_time = datetime.now()

def attendance_report():
    pqr1 = pandas.read_csv(r"C:\Users\dell\Dropbox\My PC (DESKTOP-F8CP1UF)\Documents\GitHub\2001CB24_2022\tut06\input_attendance.csv")
    pqr2 = pandas.read_csv(r"C:\Users\dell\Dropbox\My PC (DESKTOP-F8CP1UF)\Documents\GitHub\2001CB24_2022\tut06\input_registered_students.csv")
    # dates of classes taken
    data1 = ["28-07-2022","01-08-2022","04-08-2022","08-08-2022","11-08-2022","15-08-2022","18-08-2022",
             "22-08-2022","25-08-2022","29-08-2022","01-09-2022","05-09-2022","08-09-2022","12-09-2022",
             "15-09-2022","19-09-2022","22-09-2022","26-09-2022","29-09-2022"]
    # dates of holidays
    data2 = ["15-08-2022","18-08-2022"]
    # no class because of exams
    data3 = ["15-09-2022","19-09-2022","22-09-2022"]

    for i in range(0,len(pqr2["Roll No"])):
        cnt,cnt1,cnt2,cnt3,cnt5=0,0,0,0,0
        for y in range(0,len(pqr1["Attendance"])):
            if(pqr2.loc[i,"Roll No"] in pqr1.loc[y,"Attendance"]):
                cnt=cnt+1
        pqr = pandas.DataFrame()
        pqr.loc[0,"Date"] = " "
        pqr.loc[0,"Roll No"]=pqr2.loc[i,"Roll No"]
        pqr.loc[0,"Name"] = pqr2.loc[i,"Name"]
        pqr.loc[0,"Total Attendance Count"] = cnt
        ls=[]
        for y in range(0,len(pqr1["Timestamp"])):
            if(pqr2.loc[i,"Roll No"] in pqr1.loc[y,"Attendance"]):
               for  z,l in zip(data1,range(1,len(data1)+1)):
                    if(z in pqr1.loc[y,"Timestamp"] ):
                        if(z in ls):
                            cnt3=cnt3+1
                        else:
                         if(z not in data2 and z not in data3 and "14" in pqr1.loc[y,"Timestamp"] or "15.00" in pqr1.loc[y,"Timestamp"]):
                            cnt1=cnt1+1
                         elif(z not in data2 and z not in data3 and "14" not in pqr1.loc[y,"Timestamp"] and "15.00" not in pqr1.loc[y,"Timestamp"]):
                            cnt2=cnt2+1
                            cnt5=cnt5+1
                        ls.append(z)
                    elif(pqr1.loc[y,"Timestamp"][:10] not in data1):
                        cnt2=cnt2+1
                        break
        pqr.loc[0,"Real Attendance"] = cnt1
        pqr.loc[0,"Duplicate Attendance"] = cnt3
        pqr.loc[0,"Invalid"] = cnt2
        lst = []
        for y in range(0,len(pqr1["Timestamp"])):
            if(pqr2.loc[i,"Roll No"] in pqr1.loc[y,"Attendance"]):
               for  z,l in zip(data1,range(1,len(data1)+1)):
                    pqr.loc[l,"Date"]=z
                    if(z in pqr1.loc[y,"Timestamp"]):
                        if(z in lst):
                            pqr.loc[l,"Duplicate Attendance"]=1
                        else:
                         if(z not in data2 and z not in data3 and "14" in pqr1.loc[y,"Timestamp"] or "15.00" in pqr1.loc[y,"Timestamp"]):
                            pqr.loc[l,"Real Attendance"] = 1
                         elif(z not in data2 and z not in data3 and "14" not in pqr1.loc[y,"Timestamp"] and "15.00" not in pqr1.loc[y,"Timestamp"]):
                            pqr.loc[l,"Invalid"] = 1
                        lst.append(z)
        for y in range(0,len(pqr1["Timestamp"])):
            if(pqr2.loc[i,"Roll No"] in pqr1.loc[y,"Attendance"]):
               for  z,l in zip(data1,range(1,len(data1)+1)):
                  if(pqr1.loc[y,"Timestamp"][:10] not in data1):
                      pqr.loc[len(data1)+2,"Date"]=pqr1.loc[y,"Timestamp"][:10]
                      pqr.loc[len(data1)+2,"Invalid"]=1
                      break
        cnt4=0
        for y,z in zip(range(1,len(pqr["Date"])),data1):
            if(pqr.iloc[y,4]!=1 and z not in data2 and z not in data3):
                pqr.loc[y,"Absent"]=1
                cnt4=cnt4+1
        pqr.loc[0,"Absent"]=cnt4
        pqr.to_excel(r"C:\Users\dell\Dropbox\My PC (DESKTOP-F8CP1UF)\Documents\GitHub\2001CB24_2022\tut06\output\{}.xlsx".format(pqr2.loc[i,"Roll No"]), index=False)
    pqr3= pandas.DataFrame()
    for i in range(0,len(pqr2["Roll No"])):
        pqr3.loc[i,"Roll"]=pqr2.loc[i,"Roll No"]
        ct=0
        for  z in (data1):
           flag=0
           for y in range(0,len(pqr1["Timestamp"])):
            if(pqr2.loc[i,"Roll No"] in pqr1.loc[y,"Attendance"]):
                if(z in pqr1.loc[y,"Timestamp"] and z not in data2 and z not in data3 and "14" in pqr1.loc[y,"Timestamp"] or "15.00" in pqr1.loc[y,"Timestamp"] ):
                    pqr3.loc[i,z]="P"
                    ct=ct+1
                    flag=1
           if(flag==0 and z not in data2 and z not in data3):
                    pqr3.loc[i,z]="A"
        pqr3.loc[i,"Actual Lecture Taken"]=14
        pqr3.loc[i,"Total Real Attendance"]=ct
        pqr3.loc[i,"% Attendance"]=ct/14*100
    pqr3.to_excel(r"C:\Users\dell\Dropbox\My PC (DESKTOP-F8CP1UF)\Documents\GitHub\2001CB24_2022\tut06\output\attendance_report_consolidated.xlsx",index=False)
import pandas
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()




#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))