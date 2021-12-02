from openpyxl import Workbook
import random


def alg1(stafftmp, staffdatatmp, slotstmp, sh1tmp):
    smeni = []
    for i in range(0,staff):
        smeni.append(0)
    for i in range(0, slotstmp):
        smeni1 = []
        for j in range(0, staff):
            smeni1.append(0)
        for j in range(0, stafftmp):
            if int(staffdatatmp[j][i]) == 2:
                smeni1[j] += 1 + smeni[j]
            if smeni1[j] == 0:
                smeni1[j] = 999

        smeni1_num = list (enumerate(smeni1, 0))

        r = min(smeni1_num, key=lambda g: g[1])

        del(smeni1_num[r[0]])
        if r[1]!=999:

            smeni[r[0]]+=1
        r2 = min(smeni1_num, key=lambda g: g[1])
        if r2[1] != 999 and r2[0]!=r[0]:
            smeni[r2[0]] += 1
            l = [i, r[0],r2[0]]

        else:
            l = [i,r[0],'-']
        if r[1]==999:
            l = [i,'-','-']
        sh1tmp.append(l)

    sh1tmp.append(smeni)

def alg2(stafftmp, staffdatatmp, slotstmp, sh1tmp):
    smeni = []
    for i in range(0, staff):
        smeni.append(0)
    for i in range(0, slotstmp):
        smeni1 = []
        for j in range(0, staff):
            smeni1.append(0)

        for j in range(0, stafftmp):
            if int(staffdatatmp[j][i]) == 2 or int(staffdatatmp[j][i]) == 1:
                smeni1[j] += 1 + smeni[j]
            if smeni1[j] == 0:
                smeni1[j] = 999
        smeni1_num = list (enumerate(smeni1, 0))

        r = min(smeni1_num, key=lambda g: g[1])
        del(smeni1_num[r[0]])
        if r[1]!=999:
            smeni[r[0]]+=1
        r2 = min(smeni1_num, key=lambda g: g[1])
        if r2[1] != 999 and r2[0]!=r[0]:
            smeni[r2[0]] += 1
            l = [i, r[0],r2[0]]
        else:
            l = [i, r[0],'-']
        if r[1] == 999:
            l = [i, '-', '-']
        sh1tmp.append(l)

    sh1tmp.append(smeni)


wb = Workbook()

wb["Sheet"].title = "Schedule"
wb2 = Workbook()
wb2["Sheet"].title = "Schedule2"
sh1 = wb.active
sh2 = wb2.active
print("Enter the number of staff")
staff = int(input()) #количество человек
#print("Enter the number of threads")
threads = 2 #int(input()) #количество потоков(пока не использовал)
slots = 28 #слоты
staffdata = [] #список для каджого человека
firstline = [staff, threads]
sh1.append(firstline)
sh2.append(firstline)
#for i in range(0, staff):
    #tmp = []
    #for j in range(0, slots):
        #tmp.append(random.randint(0, 2))

    #staffdata.append(tmp)
    #sh1.append(tmp)
    #sh2.append(tmp)
for i in range(0,staff):
    print("Enter ",i+1," staff")
    tmp = []
    tmp = input().split()
    if len(tmp)!=28:
        print("You should enter 28 slots for ",i+1," staff")
        break
    staffdata.append(tmp)


alg1(staff,staffdata,slots,sh1)
alg2(staff,staffdata,slots,sh2)
wb.save("Schedule.xlsx")
wb2.save("Schedule2.xlsx")
