#Binary search

from QuickSort import QuickSort


def SearchElementInArray(arr, element, min,max):
    #Base case of recursion
    if max >= min:
        #Find the index of half array
        MidElement= min+(max-min)//2

        #If the element to find catch with "MidElement" return it
        if arr[MidElement]==element:
            return  MidElement
        #if the element to find is less than element in "MidElement" index search just on the left way
        elif arr[MidElement]>element:
            return  SearchElementInArray(arr, element,min, MidElement-1)
        #else search just on the right way
        else:
            return SearchElementInArray(arr, element, MidElement+1, max)
    else:
        return  -1



if __name__=='__main__':
    Arr=[14,17,16,18, 6]
    x=17
    Sort= QuickSort(Arr)
    res= SearchElementInArray(Arr, x, 0, len(Arr)-1)
    print(res)

