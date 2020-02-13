class FindSmallset:

    def findmethod(self, arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index
    
    


s = FindSmallset()
arr_test = [89, 4, 12, 6, 34, 0, 8, 22, 5, 21, 99, 2, 1, 11]
index = s.findmethod(arr_test)
print(arr_test[index])
