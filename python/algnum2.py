def function1(x):
    F1=(x*x*x)+(2*x)-2022
    return round(F1,4)
def derivative1(x):
    P=3*(x*x)+2
    return round(P,54)
def function2(x):
    if (2022-(2*x)) < 0:
        TMP=(2022-(2*x))*(-1)
        F2=TMP**(1/float(3))
        F2=-1*F2
    else:
        F2=(2022-(2*x))**(1/float(3))
    return round(F2,4)
def iteration(x,F1,F2):
    K=x-(F1/F2)
    return round(K,4)
def is_float(variable) -> bool:
    try:
        float(variable)
        return True
    except ValueError:
        return False

variable=True
while(variable):
    E=input("Podaj dokladnosc z przedzialu od 0 do 1 (liczbe zmiennoprzecikowa wpisz uzywajac separatora '.' ):")
    if(is_float(E)):
        if(float(E)<1 and float(E)>0):
            variable=False
            E=float(E)
        else:
            print("Podana liczba jest poza dozwolonym przedzialem! Podaj ja jeszcze raz!")
    else:
        print("Podane wyrazenie nie jest liczba! Podaj je jeszcze raz!")

variable=True
while(variable):
    X_0=input("Podaj punkt poczatkowy x_0(liczbe zmiennoprzecikowa wpisz uzywajac separatora '.' ):")
    if(is_float(X_0)):
        variable=False
        X_0=float(X_0)
    else:
        print("Podane wyrazenie nie jest liczba! Podaj je jeszcze raz!")

variable=True
steps_tangent=0
X_TMP=X_0
F_TMP=function1(X_TMP)
if(F_TMP<E and F_TMP>(-E)):
    variable=False

while(variable):
    steps_tangent+=1
    FP=derivative1(X_TMP)
    X_K=iteration(X_TMP,F_TMP,FP)
    F_TMP=function1(X_K)
    X_TMP=X_K

    if(F_TMP<E and F_TMP>(-E)):
        variable=False
    elif(steps_tangent>500):
        variable=False

variable=True
steps_iteration=0
X_TMP=X_0
F_TMP=function1(X_TMP)
if(F_TMP<E and F_TMP>(-E)):
    variable=False

while(variable):
    steps_iteration+=1
    X_K=function2(X_TMP)
    F_TMP=function1(X_K)
    X_TMP=X_K
    if(F_TMP<E and F_TMP>(-E)):
        variable=False
    elif(steps_iteration>500):
        variable=False

if(steps_tangent>500):
    print("Dla metody stycznych X_0 bylo niefortunnym przypadkiem i obliczenia trwaly zbyt dlugo, więc program przerwal prace.")
else:
    print("Ilosc krokow dla metody stycznych: ",steps_tangent)

if(steps_iteration>500):
    print("Dla metody iteracji prostych X_0 bylo niefortunnym przypadkiem i obliczenia trwaly zbyt dlugo, więc program przerwal prace.")
else:
    print("Ilosc krokow dla metody iteracji prostych: ",steps_iteration)