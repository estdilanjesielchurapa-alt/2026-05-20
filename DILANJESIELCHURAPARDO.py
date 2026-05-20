import math

opcion = ""

while opcion != "0":
    print("\n--- MENU ---")
    print("1 Angulo recto")
    print("2 Temperatura")
    print("3 Positivo o negativo")
    print("4 Condicion x y z")
    print("5 Distancia")
    print("6 Comparar numeros")
    print("7 Numero central")
    print("8 Raiz cuadrada")
    print("9 Par o impar")
    print("10 Fecha siguiente")
    print("11 Pesos")
    print("12 Divisor")
    print("13 Tipo de angulo")
    print("14 Nota a letra")
    print("15 Operaciones")
    print("16 Calculadora codigo")
    print("17 Validar fecha")
    print("18 Ascensor")
    print("19 Media hasta negativo")
    print("20 Dias del mes")
    print("21 Suma 1-100")
    print("22 Media hasta 0")
    print("23 Primos 2-1000")
    print("24 Aprobados")
    print("25 Notables")
    print("26 Media positivos y negativos")
    print("27 Articulos")
    print("28 Temperaturas")
    print("29 E(x)")
    print("30 Fibonacci")
    print("31 Mayores 65")
    print("32 Duplicar capital")
    print("33 Salarios")
    print("34 Tabla multiplicar")
    print("35 Primo o no")
    print("0 Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        ang = float(input("Angulo: "))
        if ang == 90:
            print("Recto")
        else:
            print("No es recto")

    elif opcion == "2":
        t = float(input("Temp: "))
        if t > 100:
            print("Mayor a 100")
        else:
            print("Menor o igual")

    elif opcion == "3":
        n = float(input("Numero: ")) 
        if n > 0:
            print("Positivo")
        elif n < 0:
            print("Negativo")
        else:
            print("Cero")

    elif opcion == "4":
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
        if x > y and z < 20:
            p = float(input("p: "))
            print(p)

    elif opcion == "5":
        d = float(input("Distancia: "))
        if d > 20 and d < 35:
            t = float(input("Tiempo: "))
            print(t)

    elif opcion == "6":
        a = float(input("a: "))
        b = float(input("b: "))
        if a > b:
            print("Mayor")
        elif a < b:
            print("Menor")
        else:
            print("Iguales")

    elif opcion == "7":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        if (a > b and a < c) or (a < b and a > c):
            print(a)
        elif (b > a and b < c) or (b < a and b > c):
            print(b)
        else:
            print(c)

    elif opcion == "8":
        n = float(input("Numero: "))
        if n >= 0:
            print(math.sqrt(n))
        else:
            print("No se puede")

    elif opcion == "9":
        n = int(input("Numero: "))
        if n % 2 == 0:
            print("Par")
        else:
            print("Impar")

    elif opcion == "10":
        d = int(input("Dia: "))
        m = int(input("Mes: "))
        a = int(input("Año: "))

        if m == 2:
            if a % 4 == 0:
                dm = 29
            else:
                dm = 28
        elif m in [4,6,9,11]:
            dm = 30
        else:
            dm = 31

        if d < dm:
            d += 1
        else:
            d = 1
            if m < 12:
                m += 1
            else:
                m = 1
                a += 1

        print(d, "/", m, "/", a)

    elif opcion == "11":
        n = int(input("Cantidad: "))
        a=b=c=d=0
        for i in range(n):
            p = float(input("Peso: "))
            if p < 40:
                a+=1
            elif p < 50:
                b+=1
            elif p < 60:
                c+=1
            else:
                d+=1
        print(a,b,c,d)

    elif opcion == "12":
        a = int(input("a: "))
        b = int(input("b: "))
        if b % a == 0:
            print("a divide b")
        elif a % b == 0:
            print("b divide a")
        else:
            print("No")

    elif opcion == "13":
        ang = float(input("Angulo: "))
        if ang < 90:
            print("Agudo")
        elif ang == 90:
            print("Recto")
        else:
            print("Obtuso")

    elif opcion == "14":
        n = float(input("Nota: "))
        if n >= 90:
            print("A")
        elif n >= 80:
            print("B")
        elif n >= 70:
            print("C")
        elif n >= 60:
            print("D")
        else:
            print("F")

    elif opcion == "15":
        a = float(input("a: "))
        b = float(input("b: "))
        op = input("Op: ")
        if op == "+":
            print(a+b)
        elif op == "-":
            print(a-b)
        elif op == "*":
            print(a*b)
        elif op == "/":
            if b != 0:
                print(a/b)

    elif opcion == "16":
        a = float(input("a: "))
        b = float(input("b: "))
        c = int(input("1 suma 2 mult 3 div: "))
        if c == 1:
            print(a+b)
        elif c == 2:
            print(a*b)
        elif c == 3:
            if b != 0:
                print(a/b)

    elif opcion == "17":
        m = int(input("Mes: "))
        d = int(input("Dia: "))
        if m < 1 or m > 12:
            print("Mal")
        else:
            if m == 2:
                maxd = 28
            elif m in [4,6,9,11]:
                maxd = 30
            else:
                maxd = 31

            if d >=1 and d <= maxd:
                print("Bien")
            else:
                print("Mal")

    elif opcion == "18":
        piso = 1
        while True:
            print("Piso", piso)
            mov = input("s subir b bajar: ")
            if mov == "s":
                piso += 1
            elif mov == "b":
                piso -= 1

            seguir = input("seguir s/n: ")
            if seguir != "s":
                break

    elif opcion == "19":
        suma = 0
        cont = 0
        while True:
            n = float(input("Numero: "))
            if n < 0:
                break
            suma += n
            cont += 1
        if cont > 0:
            print(suma/cont)

    elif opcion == "20":
        mes = input("Mes: ")
        if mes == "febrero":
            print("28 o 29")
        elif mes in ["abril","junio","septiembre","noviembre"]:
            print("30")
        else:
            print("31")

    elif opcion == "21":
        suma = 0
        for i in range(1,101):
            suma += i
        print(suma)

    elif opcion == "22":
        suma=0
        c=0
        while True:
            n=float(input("Num: "))
            if n<=0:
                break
            suma+=n
            c+=1
        if c>0:
            print(suma/c)

    elif opcion == "23":
        for n in range(2,1001):
            primo=True
            for i in range(2,n):
                if n%i==0:
                    primo=False
            if primo:
                print(n)

    elif opcion == "24":
        n=int(input("Cantidad: "))
        a=0
        for i in range(n):
            nota=float(input("Nota: "))
            if nota>=5:
                a+=1
        print(a)

    elif opcion == "25":
        n=int(input("Cantidad: "))
        c=0
        for i in range(n):
            nota=float(input("Nota: "))
            if nota>=7 and nota<9:
                c+=1
        print(c)

    elif opcion == "26":
        sp=sn=cp=cn=0
        for i in range(10):
            n=float(input("Num: "))
            if n>0:
                sp+=n; cp+=1
            elif n<0:
                sn+=n; cn+=1
        if cp>0:
            print(sp/cp)
        if cn>0:
            print(sn/cn)

    elif opcion == "27":
        while True:
            cod=input("A B X: ")
            if cod=="X":
                break
            precio=float(input("Precio: "))
            cant=int(input("Cant: "))

    elif opcion == "28":
        d=0
        while True:
            a=float(input("Max: "))
            b=float(input("Min: "))
            if a==0 and b==0:
                break
            d+=1
        print("Dias:",d)

    elif opcion == "29":
        x=float(input("x: "))
        n=int(input("n: "))
        s=1
        f=1
        p=1
        for i in range(1,n+1):
            p*=x
            f*=i
            s+=p/f
        print(s)

    elif opcion == "30":
        n=int(input("n: "))
        a,b=1,2
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        print(b)

    elif opcion == "31":
        c=0
        while True:
            e=int(input("Edad: "))
            if e==-1:
                break
            if e>65:
                c+=1
        print(c)

    elif opcion == "32":
        c=float(input("Capital: "))
        r=float(input("Interes: "))
        años=0
        while c<2*c:
            c+=c*r
            años+=1
        print(años)

    elif opcion == "33":
        for i in range(5):
            s=float(input("Salario: "))

    elif opcion == "34":
        for i in range(1,6):
            for j in range(1,6):
                print(i*j,end=" ")
            print()

    elif opcion == "35":
        n=int(input("Num: "))
        primo=True
        for i in range(2,n):
            if n%i==0:
                primo=False
        if primo:
            print("Primo")
        else:
            print("No")

    elif opcion == "0":
        print("Fin")

    else:
        print("Error")