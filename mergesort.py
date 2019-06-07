def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        leftcounter=0 #for lefthalf
        rightcounter=0 #for righthalf
        commoncounter=0 #just counter
        while leftcounter<len(lefthalf) and rightcounter<len(righthalf):
            if lefthalf[leftcounter]<righthalf[rightcounter]:
                alist[commoncounter]=lefthalf[leftcounter]
                leftcounter+=1
            else:
                alist[commoncounter]=righthalf[rightcounter]
                rightcounter+=1
            commoncounter+=+1

        while leftcounter<len(lefthalf):
            alist[commoncounter]=lefthalf[leftcounter]
            leftcounter+=1
            commoncounter+=1

        while rightcounter<len(righthalf):
            alist[commoncounter]=righthalf[rightcounter]
            rightcounter+=1
            commoncounter+=1
    print("Merging ",alist)

alist = [18,35,57,24,
         68,8,47,25]
mergeSort(alist)
print(alist)
