#DISCLOSURE: Unless otherwise stated, I did not cheat.
#SOURCE: https://www.geeksforgeeks.org/sum-of-the-elements-from-index-l-to-r-in-an-array-when-arri-i-1i/

#Q
    #Given two integers L and R and an array arr[]
    # every element of which at index i is calculated
    # as arr[i] = i * (-1)^i. The task is to find the sum
    #of these elements of the array within the index range [L, R].

    #Examples:
    #For input L=1, R=5
    #arr = [-1,2,-3,4,-5]
    #sumAltElements = -3

    #For input L=5, R=100000000
    #sumAltElements = 49999998

#A
    #Off the bat, the most obvious solution is an iterative solution running in  O(n)
    def slowSumAltElements(L,R):
        sumAlt=0
        for number in range(L,R+1):
            if (number)%2==1:
                sumAlt+=number*-1
            else:
                sumAlt+=number
        return sumAlt

    #A point of interest though:
    # starting from the beginning of our array, pairs of elements will add to positive or negative one, depending on
    # whether the first element is negative or positive respectively. In an equation:

                # arr[i] + arr[i+1] = -1^(arr[i+1])

    # So let's count the number of pairs (round down (L-R/2)) and multiply it by -1^(arr[1])
    # If there are an even  number of elements, that's our answer
    # If there are an odd number of elements, we need to add or subtract the last element from our sum
    # Our equation would look like this:

                # floor((R-(L-1))/2) + R*(R-(L-1))%2*(-1)^(R)

                # (remember that L and R are both included,
                # so we need to subtract 1 from L-R to take that into account)

    # And there you have it! Our (L-R-1)%2 will be 0 if there are an even number of elements, and our -1^array[0] will
    # ensure that we perform our addition/subtraction appropriately.
    def fastSumAltElements(L,R):
        sumPairs = ((R - (L - 1)) // 2) * ((-1) ** (L + 1))
        lastNumIfOdd = R * ((R - (L - 1)) % 2) * ((-1) ** (R))
        return sumPairs + lastNumIfOdd
    #and this runs in constant time.