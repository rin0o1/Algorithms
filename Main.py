

def MergeSort(Arr):

    if (len(Arr)>1):
        Mid= len(Arr) // 2
        LeftSize= Arr[:Mid]
        RightSize= Arr[Mid:]

        MergeSort(LeftSize)
        MergeSort(RightSize)

        IndexLeft=0
        IndexRight=0
        IndexArr=0

        while IndexLeft< len(LeftSize) and IndexRight <len(RightSize):
            if LeftSize[IndexLeft]< RightSize[IndexRight]:
                Arr[IndexArr]= LeftSize[IndexLeft]
                IndexLeft+=1
            else:
                Arr[IndexArr]= RightSize[IndexRight]
                IndexRight+=1
            IndexArr+=1

        while IndexLeft< len(LeftSize):
            Arr[IndexArr]= LeftSize[IndexLeft]
            IndexArr+=1
            IndexLeft+=1
        while IndexRight< len(RightSize):
            Arr[IndexArr]= RightSize[IndexRight]
            IndexArr+=1
            IndexRight+=1


    pass


if __name__=='__main__':
    TestCases= int(input())
    for _  in range(TestCases):
        Lenght = int(input())
        arr = list(map(int, input().split()))
        MergeSort(arr)
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
