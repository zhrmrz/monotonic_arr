class Sol:
    def monotonic_arr(self,arr):
        return all(arr[i]<=arr[i+1] for i in range(len(arr)-1))
if __name__ == '__main__':
    p = Sol()
    print(p.monotonic_arr(arr=[1,4,5,1]))
