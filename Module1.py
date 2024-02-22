def Summa(arv1:int,arv2:int,arv3:int)->int:
    """Funktsioon tagastab kolme arvu summa 
    Summa(arv1,arv2,arv3)
    :param int arv1 Arvl sisestab kasuraja
    :param int arv2 Arvl sisestab kasuraja
    :param int arv3 Arvl sisestab kasuraja
    :rtype: int
    """
    S=arv1+arv2+arv3    
    return S

#1
def arithmetic(num1:float,num2:float):
    """Funktsioon tagastab kahe antud arvude aritmeetilise toimingu (liitmine, lahutamine, korrutamine, jagamine) tulemuse.
  arithmetic(num1,num2)
  :param float num1 Arvl sisestab kasuraja
  :param float num2 Arvl sisestab kasuraja
  :param str op Arvl väärtus valitakse järgmiste valikute hulgast: +,-,*,/
 """
    op=str(input("Sisesta +,-,*,/: "))
    p=0
 
    if op=="+":
        p=num1+num2
        
    elif op=="-":
        p=num1-num2
         
    elif op=="*":
        p=num1*num2
         
    elif op=="/":
        if num2==0:
            print("Viga, te ei saa nulliga jagada")
            return(p)
        else:
            p=num1/num2
        
    else:
        print("Tundmatu operatsioon.")
    return(p)



#2


#3
from math import sqrt
def square(side:float):
    P=side*4
    S=side**2
    d=side*sqrt(2)
    return(print("Ümbermõõt:",P, " Ruut:",S, " Diagonaal:",d))
    




