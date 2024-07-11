import os,time,csv
from funciones import*
while True:
    os.system("cls")
    print("bienvenidos al programa para calcular sueldos")
    print("\ningrese una de las siguientes opciones:")
    print("\t opcion 1° generar sueldo aleatorio.")
    print("\t opcion 2° clasificar sueldos.")
    print("\t opcion 3° Ver estadísticas.")
    print("\t opcion 4° Reporte de sueldos.")
    print("\t opcion 5° salir.")
    opc=int(input("\t ingrese una de las opciones escritas anteriormente: "))
    if opc==1:
        generar_sueldo()
    elif opc==2:
        clasificar_sueldo()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_sueldos()
    elif opc==5:
        salir()
    else:
        print("\n ¡¡ERROR!! no existe la opcion ingresada porfavor ingrese alguna de las opciones señaladas anterior mente")
        time.sleep(3)