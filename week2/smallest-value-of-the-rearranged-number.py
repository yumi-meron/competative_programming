class Solution:
    def smallestNumber(self, num: int) -> int:
        #define a helper function that sorts the number the way we want
        def sorter(num):
            if num > 0:
                x = list(str(num))
                x.sort()
                if x[0] == '0':
                    #since a number can't have leading zeros, we swap the zero with the next small number
                    for i in range(len(x)):
                        if x[i] != '0':
                            x[0], x[i] = x[i], x[0]
                            break
            else:
                #if its a negative number ,just reverse sort the number and return it with '-' sign
                x = list(str(num)[1:])
                x.sort(reverse = True)
                x = ['-'] + x

            return int(''.join(x))


        
            
        return 0 if num== 0 else sorter(num)
        
        