#cuenta dig int->int
#cuenta la cantidadd de digito
#del entero n
#
#
def cuentaDig(n):
    if -9<=n<=9:
        return 1
#caso recursivo
    else:
        return  1+cuentaDig(n//10)
