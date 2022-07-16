__author__ = 'Gabriel Moreno '

from random import *

#--------------funciones generales------------------
def ordenamiento_directo(v):
    #menor a mayor
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    return v
def exclusion_cero(vec):
    #suponiendo que sea de menor a mayor
    vector_ordenado = ordenamiento_directo(vec)
    men_pre = vec[0]
    for i in range(len(vector_ordenado)):
        if men_pre != 0:
            return men_pre
        else:
            men_pre = vec[i+1]
def ValidarGenerico(Minimo,Maximo,mensaje):
 n = -1
 while n < Minimo or n > Maximo:
     n = int(input(mensaje))
     if n < 0 or n > 20:
       print("Error... Vuelva a intentarlo")
 return n
def ValidarMenor(menor,mensaje):
    n = -1
    while n <= menor:
        n = int(input(mensaje))
        if n <= menor:
            print("Error... Vuelva a intentarlo")
    return n
def menu():
 print("""
--Menu de opciones para la gestion del sitio--
1.Resultados
2.Disponibilidad
3.Mejor precio y sugerencias
4.Solo comparables
5.Tabla de precios
6.Ofertas especiales
7.Presupuesto limitado
8.Mejor precio
0.Salir
    """)
 opcion = ValidarGenerico(0,8,"Ingrese la opcion deseada:")
 return opcion

def LectorAutomaticoHotel(Cantidad):
    hoteles = ["Antártida","Atlantico","Bahia","Biarritz","Calypso","Caribe","Colonial","Del Valle","Imperial","Internacional","Maison","Majestic","Mansion","Metropol","Mónaco","Moderno","Montecarlo","Nacional","Saint Tropez","Traful"]
    #n = len(hoteles)
    #dato = randint(0,n-1)
    ArrayHotelname = [] * Cantidad
    for i in range(Cantidad):
        n = len(hoteles)
        dato = randint(0,n-1)
        ArrayHotelname.append(hoteles[dato])
        del hoteles[dato]
    return ArrayHotelname
def MenuOpcionesAutomaticHotel():
    numero_Hoteles = ValidarGenerico(0,20,"Ingrese la cantidad de Hoteles que desea obtener:")
    print()
    print("1.Generar hoteles de forma AUTOMATICO")
    print("2.Generar hoteteles de forma MANUAL")
    print()
    opcion = ValidarGenerico(0,2,"Ingrese la opcion: ")

    if opcion == 1:
        arregloHoteles = LectorAutomaticoHotel(numero_Hoteles)
        precio_Hotel_Despegar = precio_Aleatorio(numero_Hoteles)
        precio_Hotel_Booking = precio_Aleatorio(numero_Hoteles)
        precio_Hotel_Expedia = precio_Aleatorio(numero_Hoteles)
    else:
        arregloHoteles = LectorManualHotel(numero_Hoteles)
        precio_Hotel_Despegar ,precio_Hotel_Booking, precio_Hotel_Expedia = Carga_precios(arregloHoteles)
    return  arregloHoteles, numero_Hoteles, precio_Hotel_Despegar, precio_Hotel_Booking, precio_Hotel_Expedia
def precio_Aleatorio(Cantidad):
    v = []
    for i in range(Cantidad):
        precio = randrange(0,10000,200)
        v.append(precio)
    return v
def LectorManualHotel(Cantidad):
    v = []
    for i in range(Cantidad):
        insertarNombre = input("ingrese el nombre del hotel "+ str(i + 1)+":")
        v.append(insertarNombre)
    return v
def Carga_precios(v):
    x = []
    y = []
    z = []
    largo = len(v)
    for i in range(largo):
        print("Para el hotel ", v[i])
        desp = int(input("Ingrese el precio de despegar: "))
        book = int(input("Ingrese el precio de booking: "))
        exp = int(input("Ingrese el preacio de expedia: "))
        x.append(desp)
        y.append(book)
        z.append(exp)
#   for i in range(largo):
#        print("Hotel:", v[i], "- Precio despegar: ", x[i], "- Precio booking: ", y[i], "- Precio expedia: ", z[i])
    return x,y,z
#--------------funciones para opcion 1: compleo.------------------
def mostrarArreglo(v,precio1,precio2,precio3):
    n = len(v)
    for i in range(n):
        r = ""
        r += "Nombre del Hotel " + v[i] + " | "
        r += "Importe a cobrar por Despegar: $" + str(precio1[i]) + " | "
        r += "Importe a cobrar por Booking: $" + str(precio2[i]) + " | "
        r += "Importe a cobrar por Expedia: $" + str(precio3[i]) + " | "
        print(r)
        #formato sacado de la ficha de Registros
#--------------funciones para opcion 2: Completo..------------------
def disponibilidad(hotel,precio):
    total = len(hotel)
    avaible = 0
    for i in range(len(hotel)):
        if precio[i] != 0:
            avaible += 1
    porcentaje = avaible / total * 100
    return avaible , round(porcentaje,2)
#--------------funciones para opcion 3: completo..------------------
def bus_pre_hotel(v, x, y, z):
    n = len(v)
    nombre = input("Por favor ingrese el nombre del hotel que desea buscar: ")
    for i in range(n):
        if str.upper(v[i]) == str.upper(nombre):
            nom = v[i]
            desp = x[i]
            book = y[i]
            exp = z[i]
            vector = [desp, book, exp]
            pre = exclusion_cero(vector)
            return nom, pre
    return None, None
def compar_hotel(v, x, y, z):

    hotel_PrecioSale = []
    n = len(v)
    nom, pre = bus_pre_hotel(v, x, y, z)
    if not nom or not pre:
        print("No se encontro el hotel buscado")
    else:
        print("El hotel",nom," tiene su mejor precio cotizado en ",pre,"$")
        for i in range(n):
            if pre == x[i]:
                hotel_PrecioSale.append(v[i])
        for i in range(n):
            if pre == y[i]:
                for j in range(len(hotel_PrecioSale)):
                    if v[i] != hotel_PrecioSale[j]:
                        hotel_PrecioSale.append(v[i])
        for i in range(n):
            if pre == z[i]:
                for j in range(len(hotel_PrecioSale)):
                    if v[i] != hotel_PrecioSale[j]:
                        hotel_PrecioSale.append(v[i])
    if len(hotel_PrecioSale) > 0:
        print("Se han encontrado los siguientes hoteles con el mismo precio: ")
        for i in range(len(hotel_PrecioSale)):
            print(hotel_PrecioSale[i])
    else:
        print("No se han encontrado hoteles con precios similares")
#--------------funciones para opcion 4: Falta Display..------------------
def analasis3precios(v,precio1,precio2,precio3):
    nuevo =[]
    n = len(v)
    for i in range(n):
        if precio1[i] and precio2[i] and precio3[i] != 0:
           nuevo.append(v[i])
    return nuevo
def orden_alfabetico(v, x, y, z):
    nombreOrd_hotel = v[:]
    despegarOrd_precio = x[:]
    bookinOrd_precio = y [:]
    expediaOrd_precio = z[:]
    for i in range(len(nombreOrd_hotel) - 1):
        for j in range(i+1, len(nombreOrd_hotel)):
            if nombreOrd_hotel[i] > nombreOrd_hotel[j]:
                nombreOrd_hotel[i], nombreOrd_hotel[j] = nombreOrd_hotel[j], nombreOrd_hotel[i]
                #precios de despegar..
                despegarOrd_precio[i], despegarOrd_precio[j] = despegarOrd_precio[j], despegarOrd_precio[i]
                #precios de booking..
                bookinOrd_precio[i], bookinOrd_precio[j] = bookinOrd_precio[j], bookinOrd_precio[i]
                #precios de expedia..
                expediaOrd_precio[i], expediaOrd_precio[j] = expediaOrd_precio[j], expediaOrd_precio[i]

    return nombreOrd_hotel,despegarOrd_precio,bookinOrd_precio,expediaOrd_precio
#--------------funciones para opcion 5..------------------
def conteo_b(a):
    #recorremos cada arreglo de precios de forma individual
    b = [0] * 5
    n = len(a)
    for i in range(n):
        if 1 < a[i] < 999:
            b[0] += 1
        elif 1000 < a[i] < 1999:
            b[1] += 1
        elif 2000 < a[i] < 2999:
            b[2] += 1
        elif 3000 < a[i] < 3999:
            b[3] += 1
        elif  a[i] > 4000 :
            b[4] += 1
    return b
def opcion_5(x, y, z):
    #aca extraemos los nuevos arreglos de conteo
    columna_despegar = conteo_b(x)
    columna_book = conteo_b(y)
    columna_exp = conteo_b(z)
    conteo = [[0] * 5 for i in range(3)]
    #metemos en la matriz estos arreglos ya hechos
    for i in range(len(conteo[0])):
        conteo[0][i] = columna_despegar[i]
        conteo[1][i] = columna_book[i]
        conteo[2][i] = columna_exp[i]
    return conteo
def display_opcion5(matriz):
    #recorro por columnas la matriz, mostrando para cada intervalo de precios su respectivo conteo por cada sitio
    for c in range(len((matriz[0]))):
            if c == 0:
                print("Para el intervalo de 1$ a 999$ se encontraron..")
                print("---"*40)
                print("En Despegar:",matriz[0][c], "En Booking:",matriz[1][c],"En Expedia:",matriz[2][c],)
                print("---"*40)
            elif c == 1:
                print("Para el intervalo de 1000$ a 1999$ se encontraron..")
                print("---"*40)
                print("En Despegar:",matriz[0][c], "En Booking:",matriz[1][c],"En Expedia:",matriz[2][c],)
                print("---"*40)
            elif c == 2:
                print("Para el intervalo de 2000$ a 2999$ se encontraron..")
                print("---"*40)
                print("En Despegar:",matriz[0][c], "En Booking:",matriz[1][c],"En Expedia:",matriz[2][c],)
                print("---"*40)
            elif c == 3:
                print("Para el intervalo de 3000$ a 3999$ se encontraron..")
                print("---"*40)
                print("En Despegar:",matriz[0][c], "En Booking:",matriz[1][c],"En Expedia:",matriz[2][c],)
                print("---"*40)
            elif c == 4:
                print("Para el intervalo de 4000$ y superior, se encontraron..")
                print("---"*40)
                print("En Despegar:",matriz[0][c], "En Booking:",matriz[1][c],"En Expedia:",matriz[2][c],)
                print("---"*40)
#--------------funciones para opcion 6: ..------------------
def seleccion_sitio(hotel,precioDespegar,precioBooking,precioExpedia):
    print("Ingrese el sitio que desea seleccionar..")
    print()
    print("1.Despegar")
    print("2.Booking")
    print("3.Expedia")
    sitio = ValidarGenerico(0,4,"Ingrese su opcion: ")
    print()
    if sitio == 1:
        precioOferta = precioDespegar[:]
        nombre = "Despegar"
    elif sitio == 2:
        precioOferta = precioBooking[:]
        nombre = "Booking"
    elif sitio == 3:
        precioOferta = precioExpedia[:]
        nombre = "Expedia"
    print("Para el sitio ",nombre, "se encontralos los siguientes resultados..")
    print("--"*30)
    n = len(precioOferta)
    for i in range(n):
        print("--"*30)
        precio = precioOferta[i]
        if precioOferta[i] < 1000:
            precioOferta[i] = precio - precio * 0.2
            print("Hotel",hotel[i], " | Precio $",precioOferta[i],"(con un descuento del 20%)")
        else :
            precioOferta[i] = precio - precio * 0.1
            print("Hotel",hotel[i], " | Precio $",precioOferta[i],"(con un descuento del 10%)")
#--------------funciones para opcion 7: ..------------------
def h_d_analizador(vectorPrecio,vectorHoteles,minimo,maximo):
    in_intervalo = []
    n = len(vectorPrecio)
    for i in range(n):
        id = i
        if minimo < vectorPrecio[i] < maximo:
            in_intervalo.append(vectorHoteles[id])
    if len(in_intervalo) != 0 :
        return in_intervalo
    else :
        return None
def Display_opcion_7(vectorHoteles, minimo, maximo,sitio):

    if vectorHoteles is not None :
        n = len(vectorHoteles)
        print("con un presupuesto minimo de $",minimo, " y un maximo de $",maximo, "se han encontrado los sientes hoteles en el sitio " ,sitio)
        for i in range(n):
            print(chr(27)+"[0;94m"+vectorHoteles[i]+chr(27)+"[0m")
            print("·."*7)
    else:
        print("No se encontraron hoteles disponibles en el rango de precio asignado para el sitio ",sitio)

#--------------funciones para opcion 8: Completo..------------------
def mejor_Precio( x, y, z):
    elprecio = []
    n = len(x)
    for i in range(n):
       dato = min(x[i],y[i],z[i])
       if dato == 0:
           elprecio.append("No existe Precio para este hotel.")
       else:
           elprecio.append(dato)
    return elprecio
def display_Mejor_precio(hotel, precio):
    n = len(hotel)
    print("Listado de hoteles con su mejor precio:")
    for i in range (n):
        print("Hotel ",hotel[i],"--- $",precio[i] )

def Hotel_Triv4go():
    nombre_Hoteles, numero_Hoteles,precio_Hotel_Despegar, precio_Hotel_Booking, precio_Hotel_Expedia= MenuOpcionesAutomaticHotel()
    opcion = -1
    while opcion !=0:
         opcion = menu()

         if opcion == 1:
             opcion1 = mostrarArreglo(nombre_Hoteles,precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             ok = input("pulse enter para continuar")
         elif opcion == 2:
             disponibilidad_Despegar = disponibilidad(nombre_Hoteles,precio_Hotel_Despegar)
             disponibilidad_Booking = disponibilidad(nombre_Hoteles,precio_Hotel_Booking)
             disponibilidad_Expedia = disponibilidad(nombre_Hoteles,precio_Hotel_Expedia)
             print(

            "Cantidad de Hotel Disponibles en Despegar: " + str(disponibilidad_Despegar[0]) + " | con un porcertaje total: "+ str(disponibilidad_Despegar[1]) + "%" "\n"
            "Cantidad de Hotel Disponibles en Booking: " + str(disponibilidad_Booking[0]) + " | con un porcertaje total: "+ str(disponibilidad_Booking[1]) + "%" "\n"
            "Cantidad de Hotel Disponibles en Expedia: " + str(disponibilidad_Expedia[0]) + " | con un porcertaje total: "+ str(disponibilidad_Expedia[1]) + "%""\n"
             )
             ok = input("pulse enter para continuar")
         elif opcion == 3:
             compar_hotel(nombre_Hoteles,precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             ok = input("pulse enter para continuar")
         elif opcion == 4:
             HotelesD3 = analasis3precios(nombre_Hoteles,precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             hoteles,despegar,booking,expedia = orden_alfabetico(HotelesD3,precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             print()
             print("Por orden Alfabetico")
             mostrarArreglo(hoteles,despegar,booking,expedia)
             ok = input("pulse enter para continuar")
         elif opcion == 5:
             bidimencional = opcion_5(precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             print(bidimencional)
             display_opcion5(bidimencional)
             print()
             ok = input("pulse enter para continuar")
         elif opcion == 6:
             seleccion_sitio(nombre_Hoteles,precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             print()
             ok = input("pulse enter para continuar")
         elif opcion == 7:
            minimo = ValidarMenor(0,"ingrese la cantidad minima de su presupuesto:")
            maximo = ValidarMenor(minimo, "ingrese la cantidad maxima de su presupuesto:")
            h_d_despegar = h_d_analizador(precio_Hotel_Despegar,nombre_Hoteles,minimo,maximo)
            h_d_booking = h_d_analizador(precio_Hotel_Booking,nombre_Hoteles,minimo,maximo)
            h_d_expedia = h_d_analizador(precio_Hotel_Expedia,nombre_Hoteles,minimo,maximo)
            Display_opcion_7(h_d_despegar,minimo,maximo,"Despegar")
            print("--"*40)
            Display_opcion_7(h_d_booking,minimo,maximo,"Booking")
            print("--"*40)
            Display_opcion_7(h_d_expedia,minimo,maximo,"Expedia")
            print("--"*40)
            ok = input("pulse enter para continuar")
         elif opcion == 8:
             precio = mejor_Precio(precio_Hotel_Despegar,precio_Hotel_Booking,precio_Hotel_Expedia)
             display_Mejor_precio(nombre_Hoteles,precio)
             ok = input("pulse enter para continuar")

if __name__ == '__main__':
    Hotel_Triv4go()
