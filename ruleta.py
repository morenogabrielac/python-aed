
import random

#-------------------------------------------------------------------------------------------------
def TextoMenu():
    print("__"*35)
    print (chr(27)+"[5;30m"+"Menu de opciones de la ruleta:" + chr(27)+"[0m")
    print("__"*35)
    print("1.Apostar Rojo/Negro")
    print("__"*35)
    print("2.Apostar Par/Impar")
    print("__"*35)
    print("3.Apostar Pasa/Falta")
    print("__"*35)
    print("4.Apostar Columna")
    print("__"*35)
    print("5.Apostar Docena")
    print("__"*35)
    print("6.Apostar Pleno")
    print("__"*35)
    print (chr(27)+"[0;32m"+"7.No va más!" + chr(27)+"[0m")
    print("__"*35)
    print (chr(27)+"[0;31m"+"8.Retirarse" + chr(27)+"[0m")
    print("__"*35)
#opciones para la interfaz de usuario-------------------------------------------------------------
def opcionColor(Color):
    if Color == 1:
        Color = "Rojo"
        return Color
    elif Color == 2:
        Color = "Negro"
        return Color
#-------------------------------------------------------------------------------------------------
def opcionParidad(Paridad):
    if Paridad == 1:
        Paridad = "Par   "
        return Paridad
    else:
        Paridad = "Impar"
        return Paridad
#-----------------------------------------------------------------------
def opcionPasaFalta(PasaFalta):
    if PasaFalta == 1:
        PasaFalta = "Pasa"
        return PasaFalta
    else:
        PasaFalta = "Falta"
        return PasaFalta
#-------------------------------------------------------------------------------------------------
def opcionColumna(Columna):

    if Columna == 1:
        Columna = "Columna Nº1"
        return  Columna
    elif Columna == 2:
        Columna = "Columna Nº2"
        return  Columna
    else:
        Columna = "Columna Nº3"
        return  Columna
#-------------------------------------------------------------------------------------------------
def opcionDocena(Docena):

    if Docena == 1:
        Docena = "Docena Nº1"
        return Docena
    elif Docena == 2:
        Docena = "Docena Nº2"
        return Docena
    else:
        Docena = "Docena Nº3"
        return Docena
#-------------------------------------------------------------------------------------------------
def opcionNumero(NumeroFijo):
    return NumeroFijo
#------------------RuletaEngine3.6----------------------------------------------------------------
def RuletaEngine(NumRuleta,NumeroFijo,Color,Paridad,PasaFalta,Columna,Docena,Vueltas):
                FichasRecuperadas = 0
                FichasGanadas = 0
                if (NumRuleta != 0 and NumeroFijo != 0) or (NumRuleta !=0 and NumeroFijo == 0):
                    if 1<= NumRuleta >=10  and 19 <= NumRuleta >=28:
                       if NumRuleta % 2 == 1:
                            ParidadR = "impar"
                            ColorR = "rojo"
                       else:
                            ParidadR = "par"
                            ColorR = "negro"
                    else:
                       if NumRuleta % 2 == 0:
                            ParidadR = "par"
                            ColorR = "negro"
                       else:
                            ParidadR = "inpar"
                            ColorR = "rojo"

                    #SUBTEMA PASA FALTA
                    if 1<= NumRuleta >= 18:
                        PasaFaltaR = "Pasa"
                    else:
                        PasaFaltaR = "Falta"

                    #SUB TEMA DOCENA

                    if 1<= NumRuleta >= 12:
                        DocenaR  = "Primer Docena"
                    elif 13<= NumRuleta >= 24:
                        DocenaR  = "Segunda Docena"
                    else:
                        DocenaR  = "Tercera Docena"
                    #Sub Tema Columna
                    Columna_seleccion = NumRuleta % 3
                    if Columna_seleccion == 0:
                        ColumnaR  = "Columna Nº3"
                    elif Columna_seleccion == 1:
                        ColumnaR  = "Columna Nº2"
                    else:
                        ColumnaR  = "Columna Nº1"
                    #Comprobador y contador


                    if Color == ColorR:
                        Color_Ac = (chr(27)+"[0;32m"+"ACIERTO!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 1
                    else:
                         Color_Ac = "        ."
                    if Paridad == ParidadR:
                        Paridad_Ac = (chr(27)+"[0;32m"+"ACIERTO!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 1
                    else:
                       Paridad_Ac = "    ."
                    if PasaFalta == PasaFaltaR:
                        PasaFalta_Ac = (chr(27)+"[0;32m"+"ACIERTO!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 1
                    else:
                       PasaFalta_Ac = "."
                    if Columna == ColumnaR:
                        Columna_Ac = (chr(27)+"[0;32m"+"ACIERTO!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 2
                    else:
                        Columna_Ac = "."
                    if Docena == DocenaR:
                        Docena_Ac = (chr(27)+"[0;32m"+"ACIERTO!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 2
                    else:
                       Docena_Ac = "    ."
                    if NumRuleta == NumeroFijo:
                        Numero_Ac = (chr(27)+"[0;32m"+"ACIERTO TOTAL!"+ chr(27)+"[0m")
                        FichasRecuperadas += 1
                        FichasGanadas += 35
                    else:
                        Numero_Ac = "        ."
                    # Lista con el contenido:
                    print("La ruleta a empezado a girar..")

                    print("=="*20)
                    print("El numero que a salido en la ruleta es: ",NumRuleta)
                    print("=="*20)
                    print("__"*35)


                    EnteryContinuar = input("pulse enter para continuar...")
                    print()
                    #RESULTADOS.................
                    print("A continuacion se mostraran los resultados finales acorde al numero de la ruleta, Vuelta Nº: ",Vueltas)
                    print("**"*20)
                    print("Color: ",Color,"\t",Color_Ac)
                    print("**"*20)
                    print("Paridad: ",Paridad,"\t",Paridad_Ac)
                    print("**"*20)
                    print("Pasa o Falta: ",PasaFalta,"\t",PasaFalta_Ac)
                    print("**"*20)
                    print("Docena:", Docena,"\t",Docena_Ac)
                    print("**"*20)
                    print("Columna: ", Columna,"\t",Columna_Ac)
                    print("**"*20)
                    print("Numero Fijo:", NumeroFijo,"\t",Numero_Ac)
                    print("**"*20)
                    print()
                    EnteryContinuar = input("pulse enter para continuar...")
                elif NumRuleta == 0 and NumeroFijo == 0:
                        # Lista con el contenido:
                    print("La ruleta a empezado a girar..")

                    print("=="*20)
                    print("El numero que a salido en la ruleta es: ",NumRuleta)
                    print("=="*20)
                    print("__"*35)


                    EnteryContinuar = input("pulse enter para continuar...")
                    print()
                    FichasRecuperadas += 1
                    FichasGanadas += 35
                    print("                           _,-'^\                                         ")
                    print("                       _,-'   ,\ )                                        ")
                    print("                  ,,-'     ,'  d'                   ~NUTRIA DANCE~        ")
                    print("    ,,,     ,,,-- J_ \    ,'                                              ")
                    print("   `\ /    /__   '  \ \ ,'         _________________________________________________ ")
                    print("   / /  _,-'  '      \ \           =_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_^_= ")
                    print("  / |,-'             /  }          =  _    _____  _     _____ _   _  _____     _   = ")
                    print(" (                 ,'  /           = |_|  |  __ \| |   |  ___| \ | |/ ___ \   | |  = ")
                    print("  '-,________         /            =  _   | |__) | |   | |___|  \| | |   | |  | |  = ")
                    print("       / ,/  \        /            = | |  |  ___/| |   |  ___| . ` | |   | |  |_|  = ")
                    print("       /,/    |       |            = | |  | |    | |__ | |___| |\  | |___| |   _   = ")
                    print("       V     /        |            = |_|  |_|    \____|\_____|_| \_|\_____/   |_|  = ")
                    print("            /          |           =______________________________________________ = ")
                    print("           /  /~\   (\__/)         _~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_~_ ")
                    print("          {  /   \,      \                                                 ")
                    print("          | |     |   a a )                   ¡¡HAS GANADO PLENO !!  ")
                    print("          / |      ~(:_Y_:)~                                               ")
                    print("          J \,                                                             ")
                    print("    _______'``_______________________________________________________________________")
                elif NumRuleta == 0 and NumeroFijo != 0:
                    FichasGanadas, FichasRecuperadas = 0
                    # Lista con el contenido:
                    print("La ruleta a empezado a girar..")

                    print("=="*20)
                    print("El numero que a salido en la ruleta es: ",NumRuleta)
                    print("=="*20)
                    print("__"*35)


                    EnteryContinuar = input("pulse enter para continuar...")
                    print()
                    #MENSAJE
                    print("        (\____/) ")
                    print("        /      \ ")
                    print("       (  / \   \ ")
                    print("        \ a a   / ")
                    print("       ~(_Y _)~/   ")
                    print("         ||   ||           -HAS PERDIDO- ")
                    print("         ||   |\ ")
                    print("        //    \ |_   ")
                    print("       / _,==.____\       SALIO EL 0 EN LA RULETA... ")
                    print("      (__:|0F|:___ ) ")
                    print("       /\ |__|   /\_-, ")
                    print("      / (       /   \ \ ")
                    print("      \  \     (    /   \_  ")
                    print("      )  '._____)  /\ _,   \_ ")
                    print("    (((___.---(((___/   \___  > ")
                    print("________________________________________________ ")
                return FichasGanadas, FichasRecuperadas
#-------------------------------------------------------------------------------------------------
def UdApos(n):
    print("Usted a apostado otra ficha a", n)
    print()
    enter = input("pulse enter para continuar")
    print()
def printFichas(fichas):
    print ((chr(27)+"[0;33m"+"Fichas en mano:" + chr(27)+"[0m"), fichas )
    print("__"*35)
def EstudioJugada(Vuelta,Fichas,TextoMayorMenor):
    print("La ",TextoMayorMenor ," cantidad de fichas se obtuvo en la vuelta ",Vuelta," con una cantidad de fichas de",Fichas)
#---------------------.Validadores.----------------------------------------------------------------
def validar_Gral(menor, mayor, mensaje):
    num = menor - 1
    while num < menor or num > mayor:
        num = int(input(mensaje))
        if num < menor or num > mayor:
            print("Error... El número no se encuentra entre las opciones disponibles")
    return  num
def validar_Menor(menor, mensaje):
    num = menor - 1
    while num < menor:
        num = int(input(mensaje))
        if num < menor:
            print("Error... El número no se encuentra entre las opciones disponibles")
    return num
def validar_Mayor(mayor, mensaje):
    num = mayor + 1
    while num > mayor:
        num = int(input(mensaje))
        if num > mayor:
            print("Error... El número no se encuentra entre las opciones disponibles")
    return  num
#--------------------------------------------------------------------------------------------------
def MontoObtenido(Player,FichasGanadas,FichasRecuperadas,fichas):
    print("・・"*20)
    print("El jugador ",Player, "ha conseguido una cantidad de fichas totales de:", FichasGanadas + FichasRecuperadas + fichas)
    print("・・"*20)
    #monton total en dinero

    print("Valor real de cada ficha: $100")
    print("・・"*20)
    Dinero = FichasGanadas + FichasRecuperadas + fichas
    DineroR = Dinero*100
    Comision = DineroR * 5/100
    DineroTotal = DineroR - Comision
    print("monton total a cobrar:$",DineroR ,"(5% de comision): $",DineroTotal)
def ApostFich():
    print()
    fichas = int(input("Ingrese la cantidad de fichas que desea apostar al rubro:"))
    print()
    return fichas
def OpcionRetirada():
    print("・・"*20)
    print("Se ha retirado de la mesa")
    print("・・"*20)
#-------------------------------def general--------------------------------------------------------
def Ruleta():
    menuOpciones = 0
    Acumulador_Fichas = 0
    vueltas = 0
    PrimerVuelta = True
    Apostado = False
    FlagColor = False
    FlagParidad = False
    FlagPasaFalta = False
    FlagColumna = False
    FlagDocena = False
    FlagNumero = False
    MayorF = MayorV = MenorF = MenorV = False
    AcumuladorFichasGanadas = AcumuladorRecuperadas = FichasGanadas = FichasRecuperadas =   0

    Color = Paridad = Numero = PasaFalta = Columna = Docena = (chr(27)+"[0;101m"+"No seleccionado"+ chr(27)+"[0m")


    print("Bievenido al juego de la ruleta UTN TP 2.")
    print("En la presente version , solo habra un jugador contra la ruleta y el jugador contara con la libertdad de apostar a todo lo que desee siempre y cuando cuente con las fichas necesarias\n")
    Player  = input("Ingrese su nombre para continuar: ")
    Fichas = validar_Menor(0,"ingrese la cantidad de fichas con las que desea jugar: ")

    #procedimiento de la ruleta
    while menuOpciones != 8:

#opcion de NO VA MAS!
        if (menuOpciones == 7 or Fichas == 0) and Apostado == True :#realizae giro ruleta
#-----------------------------------------------------------------------------------------------------------------------
            if Fichas > 0:
                        print("Ha seleccionado girar la ruleta con:")
                        printFichas(Fichas)
                        enter = input("pulse enter para continuar..")
            elif Fichas == 0:
                        printFichas(Fichas)
                        print("Se ha quedado con 0(cero) fichas, la ruleta empezara a girar con las apuestas hechas hasta el momento..")
                        enter = input("pulse enter para continuar..")
#-----------------------------------------------------------------------------------------------------------------------
            NumRuleta = random.randint(0,36)
            vueltas += 1
            FichasGanadas , FichasRecuperadas = RuletaEngine(NumRuleta,Numero,Color,Paridad,PasaFalta,Columna,Docena,vueltas)
            FichasGanadas *= Acumulador_Fichas
            FichasRecuperadas *= Acumulador_Fichas
            PrimerVuelta = False
            #Reset Interfaz de comparador de apuestas
            Color = Paridad = Numero = PasaFalta = Columna = Docena = (chr(27)+"[0;101m"+"No seleccionado"+ chr(27)+"[0m")
            Apostado = False
            FlagColor = False
            FlagParidad = False
            FlagPasaFalta = False
            FlagColumna = False
            FlagDocena = False
            FlagNumero = False
            Apostado = False
            Acumulador_Fichas = 0
#------------------ Fichas SubProblema--------/---------------------------------------------------------------------------
            FichasTotal = FichasGanadas + FichasRecuperadas + Fichas
            FichasTotalAnterior = FichasTotal
            FichasGanadasAnterior = FichasGanadas
            if Fichas < 0:
                    printFichas(Fichas)
                    print("Se ha quedado sin fichas se retirara automaticamente de la mesa..")
                    enter = input("enter para continuar..")
                    menuOpciones = 8
            elif Fichas >= 0:
                    printFichas(FichasTotal)
                    print ((chr(27)+"[0;33m"+"Fichas Ganadas:" + chr(27)+"[0m"), FichasGanadas )
                    print("__"*35)
                    print ((chr(27)+"[0;33m"+"Fichas Recuperdas:" + chr(27)+"[0m"), FichasRecuperadas )
                    print("__"*35)
                    print("Posee fichas suficientes para seguir jugando.")
                    enter = input("pulse enter para continuar")
                    print("==" * 40)
                    AcumuladorFichasGanadas += FichasGanadas
                    AcumuladorRecuperadas += FichasRecuperadas
                #ACA VAMOS A PONER EL MECANISMO DE LA MEJOR Y PEOR JUGADA Y SU VUELTA
#---------------------Rastreo de fichas para OP 8 ---------------------------------------MayorF = MayorV = Menor F = MenorV = False
            if PrimerVuelta:
                MayorF = FichasGanadasAnterior
                MayorV = vueltas
            elif FichasGanadasAnterior < FichasGanadas:
                MayorF = FichasGanadas
                MayorV = vueltas
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
            if PrimerVuelta:
                MenorF = FichasGanadasAnterior
                MenorV = vueltas
            elif FichasGanadasAnterior > FichasGanadas:
                MenorF = FichasGanadas
                MenorV = vueltas

#---------------------------------------------------------------------------------------
        elif (menuOpciones == 7 or Fichas == 0) and Apostado == False:
            print (chr(27)+"[0;95m"+"Usted no ha apostado a nada, porfavor vuelva a intentarlo y esta vez apueste!"+ chr(27)+"[0m")
            print()
            enter = input (chr(27)+"[0;95m"+"Pulse enter para continuar..."+ chr(27)+"[0m")

        if Fichas > 0:
            if menuOpciones == 1 :
                    if FlagColor == False:
                        ColorV = validar_Gral(1,2,"Apuesta a:\n1.Rojo\n2.Negro\nOpcion: ")
                        Color = opcionColor(ColorV)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF
                        FlagColor = True
                    elif FlagColor == True:
                        UdApos(Color)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF


                    Apostado = True

            elif menuOpciones == 2:
                if FlagParidad == False:#Paridad
                    ParidadV = validar_Gral(1,2,"Apuesta a..\n1.Par\n2.Inpar\nEleccion: ")
                    Paridad = opcionParidad(ParidadV)
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF
                    FlagParidad = True

                elif FlagParidad == True:
                        UdApos(Paridad)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF


                Apostado = True

            elif menuOpciones == 3:
                if FlagPasaFalta == False: #pasafalta
                    PasaFaltaV = validar_Gral(1,2,"Apuesta entre Pasa y Falta:\n1.Pasa\n2.Falta\nEleccion: ")
                    PasaFalta = opcionPasaFalta(PasaFaltaV)
                    FlagPasaFalta = True
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF
                elif FlagPasaFalta == True:
                        UdApos(PasaFalta)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF


                Apostado = True

            elif menuOpciones == 4 :
                if FlagColumna == False:  #Columndas
                    ColumnaV = validar_Gral(1,3,"Apuesta entre alguna de las 3 Columna:\n1.Columna Nº1\n2.Columna Nº2\n3.Columna Nº3\nEleccion: ")
                    Columna = opcionColumna(ColumnaV)
                    FlagColumna = True
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF
                elif FlagColumna == True:
                        UdApos(Columna)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF


                Apostado = True

            elif menuOpciones == 5:
                if FlagDocena == False: #docenas
                    DocenaV = validar_Gral(1,3,"Apuesta entre alguna de las 3 docenas:\n1.Docena Nº1\n2.Docena Nº2\n3.Docena Nº3\n""Eleccion: ")
                    Docena =  opcionDocena(DocenaV)
                    FlagDocena = True
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF
                elif FlagDocena == True:
                        UdApos(Docena)
                        ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                        Fichas -= ApuestaF


                Apostado = True

            elif menuOpciones == 6 :#numero
                if FlagNumero == False:
                    #Numero = opcionNumero(PreguntaNumeroFijo())
                    Numero = validar_Gral(0,36,"Seleccione un numero entre el 0 y el 36 para finalizar con las apuestas\nNumero:")
                    FlagNumero = True
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF
                elif FlagNumero == True:
                    UdApos(Numero)
                    ApuestaF = validar_Gral(0,Fichas,"Ingrese la cantidad de fichas que desea apostar al rubro:")
                    Fichas -= ApuestaF


                Apostado = True
        Fichas = Fichas + FichasGanadas + FichasRecuperadas

        if menuOpciones != 8:
            TextoMenu()#aca vuelve al comienzo
            printFichas(Fichas)
            MenuOpcionesV = validar_Gral(1,8,"Indique que desea realizar:")
            menuOpciones = MenuOpcionesV

            print()
    OpcionRetirada()
    MontoObtenido(Player,AcumuladorFichasGanadas,AcumuladorRecuperadas,Fichas)
    print()
    print("La mayor cantidad de fichas se obtuvo en la vuelta ",MayorV," con una cantidad de fichas de",MayorF)
    print()
    print("La menor cantidad de fichas se obtuvo en la vuelta ",MenorV," con una cantidad de fichas de",MenorF)
#----------------------------------<Programa>------------------------------------------------------



Ruleta()
