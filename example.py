    def potencias(a,n):
        if n==0:
            return 1
        elif n/2==0:
            return pot(a,n/2)*pot(a,n/2)
        else: #n impar
            return a*pot(a,(n-1)/2)



