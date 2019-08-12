
#Find those 2 number in an unsorted array that their sum is like x
#Step 1- sort array
#Step 2- find numbers


class Utilities:
    def __init__(self, arr):

        self.Sort(arr, 0, len(Arr)-1)


    def Sort(self, arr, min,max):

        if min<max:

            Pivot= self.Partition(arr, min, max)

            #Sort Right
            self.Sort(arr,Pivot+1, max)
            #Sort.Left
            self.Sort(arr, min, Pivot-1)


    def Partition(self, arr, min, max):

        IndexMinValue = min-1
        Pivot = arr[max]

        for Element in range( min, max):

            if arr[Element] < Pivot:
                IndexMinValue = IndexMinValue+1
                arr[Element], arr[IndexMinValue] = arr[IndexMinValue], arr[Element]

        PivotPosition= IndexMinValue+1
        arr[PivotPosition] , arr[max] = arr[max], arr[PivotPosition]
        return PivotPosition


#Check if extists 2 numbers that they sum is x
def FindSum(x, arr, LeftIndex, RightIndex):
    ResultArr=[]
    while LeftIndex < RightIndex:
        ElementLeft=arr[LeftIndex]
        ElementRight= arr[RightIndex]

        Sum= ElementLeft+ElementRight

        if Sum == x:
            ResultArr.append(ElementRight)
            ResultArr.append(ElementLeft)
            LeftIndex= LeftIndex+1
            RightIndex= RightIndex+1
        elif Sum <x:
            LeftIndex= LeftIndex+1
        else :
            RightIndex= RightIndex-1
    return  ResultArr



if __name__=='__main__':
    Arr=[45,10,6,5,1,-5,-10]
    Utilities_ = Utilities(Arr)
    LeftIndex=0
    RightIndex= len(Arr)-1
    x=11
    print(FindSum(x, Arr, LeftIndex, RightIndex))









