


def sort_slots(staff_shedule: list[list[int]]):
    restmp = []
    list_for_calc_sum = []
    for i in range(0, len(staff_shedule[0])):
        Not0Elem = 0
        sumElem = 0
        for j in range(0, len(staff_shedule)):
            sumElem += staff_shedule[j][i]
            if staff_shedule[j][i] == 0:
                Not0Elem += 1
        restmp.append([Not0Elem, i, sumElem])

    restmp = sorted(restmp, key=lambda x: x[0])
    restmp.reverse()
    result = []
    #print(restmp)
    for i in range(0,len(restmp)-1):
        sortElem = []
        j = 0
        while i+j < len(restmp) and restmp[i][0] == restmp[i+j][0]:
            sortElem.append(restmp[i+j])
            j+=1

        sortElem = sorted(sortElem,key=lambda x: x[2])
        j = 0
        while i + j < len(restmp) and restmp[i][0] == restmp[i + j][0]:
            restmp[i+j] = sortElem[j]
            j += 1

        #print(restmp)

        result.append(sortElem[0][1])
    result.append(restmp[-1][1])
    return result
