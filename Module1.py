def Summa(arv1:int,arv2:int,arv3:int)->int:
    """Funktsioon tagastab klme arvu summa 
    Summa(arv1,arv2,arv3)
    :param int arv1 Arvl sisestab kasuraja
    :param int arv2 Arvl sisestab kasuraja
    :param int arv3 Arvl sisestab kasuraja
    :rtype: int
    """
    S=arv1+arv2+arv3    
    return S


def arithmetic(num1:float,num2:float):
    op=str(input("Sisesta: +,-,*,/ "))
    p=0
 
    if op=="+":
        p=num1+num2
        
    elif op=="-":
        p=num1-num2
         
    elif op=="*":
        p=num1*num2
         
    elif op=="/":
        p=num1/num2
         
    else:
        print("Tundmatu operatsioon.")
    return(p)
    

