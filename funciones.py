import random,os,time,csv
empresa=[]
sueldo= random.randint (300000,2500000)
sueldo1= random.randint (300000,2500000)
sueldo2= random.randint (300000,2500000)
sueldo3= random.randint (300000,2500000)
sueldo4= random.randint (300000,2500000)
sueldo5= random.randint (300000,2500000)
sueldo6= random.randint (300000,2500000)
sueldo7= random.randint (300000,2500000)
sueldo8= random.randint (300000,2500000)
sueldo9= random.randint (300000,2500000)
sueldot=sueldo-sueldo*0.19
sueldot1=sueldo1-sueldo1*0.19  
sueldot2=sueldo2-sueldo2*0.19
sueldot3=sueldo3-sueldo3*0.19
sueldot4=sueldo4-sueldo4*0.19
sueldot5=sueldo5-sueldo5*0.19
sueldot6=sueldo6-sueldo6*0.19
sueldot7=sueldo7-sueldo7*0.19
sueldot8=sueldo8-sueldo8*0.19
sueldot9=sueldo9-sueldo9*0.19
trabajadores =[("Juan Pérez",sueldo), ("María García",sueldo1), ("Carlos López",sueldo2), ("Ana Martínez",sueldo3), ("Pedro Rodríguez",sueldo4), ("Laura Hernández",sueldo5),
                ("Miguel Sánchez",sueldo6), ("Isabel Gómez",sueldo7), ("Francisco Díaz",sueldo8), ("Elena Fernández",sueldo9)]
sueldos =[(sueldo,"Juan Pérez"), (sueldo1,"María García"), (sueldo2,"Carlos López"), (sueldo3,"Ana Martínez"), (sueldo4,"Pedro Rodríguez"), (sueldo5,"Laura Hernández"),
                (sueldo6,"Miguel Sánchez"), (sueldo7,"Isabel Gómez"), (sueldo8,"Francisco Díaz"), (sueldo9,"Elena Fernández")]
reporte =[("Juan Pérez","sueldo liquido:",sueldot,"sueldo bruto:",sueldo),("María García","sueldo liquido:",sueldot1,"sueldo bruto:",sueldo1), ("Carlos López","sueldo liquido:",sueldot2,"sueldo bruto:",sueldo2), ("Ana Martínez","sueldo liquido:",sueldot3,"sueldo bruto:",sueldo3), ("Pedro Rodríguez","sueldo liquido:",sueldot4,"sueldo bruto:",sueldo4), ("Laura Hernández","sueldo liquido:",sueldot5,"sueldo bruto:",sueldo5),
              ("Miguel Sánchez","sueldo liquido:",sueldot6 ,"sueldo bruto:",sueldo6), ("Isabel Gómez","sueldo liquido:",sueldot7,"sueldo bruto:",sueldo7), ("Francisco Díaz","sueldo liquido:",sueldot8,"sueldo bruto:",sueldo8), ("Elena Fernández","sueldo liquido:",sueldot9,"sueldo bruto:",sueldo9)]
def generar_sueldo():
    print("generando un sueldo por trabajador.")
    print("espere unos segundos.")
    time.sleep(2)
    for d in trabajadores:
        print("trabajador",d)
        time.sleep(0.9)
    print("los datos fueron entregados con exito entregados")
    time.sleep(3)

def clasificar_sueldo():
    print("la clasificacion esta en proceso")
    print("espere unos segundos.")
    time.sleep(2)
    for s in sueldos: 
        if sueldos>800000:
            print("trabajadores con un sualdo inferior a $800.000:", s)
            time.sleep(0,5)
            print("los datos fueron clasificados con exito")
            time.sleep(2)
        elif (0)>800000 and s<2000000:
            print("trabajadores con un sueldo entre $800.000 y $2.000.000:",s)
            time.sleep(0,5)
            print("los datos fueron clasificados con exito")
            time.sleep(2)
        elif sueldos>2000000:
            print("trabajadores con sueldo superior a $2.000.000:",s )
            time.sleep(0,5)
            print("los datos fueron clasificados con exito")
            time.sleep(2)

def ver_estadisticas():
    print("la creaccion de etadisticas esta en proceso")
    print("espere unos segundos.")
    time.sleep(2)

def reporte_sueldos():
    print("la creaccion del reporte de sueldos esta en porceso")
    print("espere unos segundos.")
    time.sleep(2)
    for r in reporte:
        print("los reportes de sueldo son los sigientes: ",r)
        time.sleep(0.5)
        
    opcion=int(input("si decea convertir esta infrmacion en un archivo escoja la opcion 1.\n deforma contraria escoja el opcion 2."))
    if opcion==1:
        try:
            nombre_archivo=input("ingrece el nombre del arcivo"),+".csv"
            escritor=csv.writer
            csv.reader=(nombre_archivo,"x",)
                
        except:
            print("ya existe un archivo con ese nombre porfavor ingrese otro")
    elif opcion==2:
        print("entendido en seguida lo enviaremos al menu principal")
        time.sleep(3)
def salir():
    print("finalisando programa")
    time.sleep(0.5)
    os.system("cls")
    print("finalisando programa.")
    time.sleep(0.5)
    os.system("cls")
    print("finalisando programa..")
    time.sleep(0.5)
    os.system("cls")
    print("finalisando programa...")
    time.sleep(0.5)
    print("el programa fue desarrollado por Vicente Guajardo")
    time.sleep(0.2)
    print("¡¡gracias a DIOS!!")
    exit()