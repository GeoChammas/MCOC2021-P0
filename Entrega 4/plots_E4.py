import matplotlib.pylab as plt
import ast
import statistics


Ns_A = []
dts_A1_float = []
dts_A2_float = []
dts_A3_float = []
dts_A4_float = []
dts_A5_float = []
dts_A6_float = []
dts_A7_float = []

dts_A1_double = []
dts_A2_double = []
dts_A3_double = []
dts_A4_double = []
dts_A5_double = []
dts_A6_double = []
dts_A7_double = []


Ns_B = []
dts_B1_float = []
dts_B2_float = []
dts_B3_float = []
dts_B4_float = []
dts_B5_float = []
dts_B6_float = []
dts_B7_float = []
dts_B8_float = []
dts_B9_float = []

dts_B1_double = []
dts_B2_double = []
dts_B3_double = []
dts_B4_double = []
dts_B5_double = []
dts_B6_double = []
dts_B7_double = []
dts_B8_double = []
dts_B9_double = []



diccionario = {}

diccionario["A_float"] = open("A_float.txt", "r")
diccionario["A_double"] = open("A_double.txt", "r")
diccionario["B_float"] = open("B_float.txt", "r")
diccionario["B_double"] = open("B_double.txt", "r")

for caso in diccionario:
    if caso == "A_float":
        Af = diccionario[caso].read().split("\n")
        

        l = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []

        
        for linea in Af:
            
            if len(linea) > 0:
                sl = ast.literal_eval(linea)

                if len(l) < 10:
                    Ns_A.append(sl[0])
                    l.append(sl[1])
                
                    if len(l) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l)):
                                aux.append(l[j][i])
                            dts_A1_float.append(statistics.mean(aux))
                      
                    
    
                elif len(l1) < 10:

                    l1.append(sl[1])

                    if len(l1) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l1)):
                                aux.append(l1[j][i])
                            dts_A2_float.append(statistics.mean(aux))

                            
                            
                elif len(l2) < 10:

                    l2.append(sl[1])
            
                    if len(l2) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l2)):
                                aux.append(l2[j][i])
                            dts_A3_float.append(statistics.mean(aux))

                            
                        
                elif len(l3) < 10:
                    
                    l3.append(sl[1])
            
                    if len(l3) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l3)):
                                aux.append(l3[j][i])
                            dts_A4_float.append(statistics.mean(aux))

                    
                      
                elif len(l4) < 10:

                    l4.append(sl[1])
            
                    if len(l4) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l4)):
                                aux.append(l4[j][i])
                            dts_A5_float.append(statistics.mean(aux))


                                                
                elif len(l5) < 10:

                    l5.append(sl[1])
            
                    if len(l5) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l5)):
                                aux.append(l5[j][i])
                            dts_A6_float.append(statistics.mean(aux))


                                               
                elif len(l6) < 10:

                    l6.append(sl[1])
            
                    if len(l6) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l6)):
                                aux.append(l6[j][i])
                            dts_A7_float.append(statistics.mean(aux))

    elif caso == "A_double":
        Ad = diccionario[caso].read().split("\n")
        

        l = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []

        
        for linea in Ad:
            
            if len(linea) > 0:
                sl = ast.literal_eval(linea)

                if len(l) < 10:

                    l.append(sl[1])
                
                    if len(l) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l)):
                                aux.append(l[j][i])
                            dts_A1_double.append(statistics.mean(aux))
                      
                    
    
                elif len(l1) < 10:

                    l1.append(sl[1])

                    if len(l1) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l1)):
                                aux.append(l1[j][i])
                            dts_A2_double.append(statistics.mean(aux))

                            
                            
                elif len(l2) < 10:

                    l2.append(sl[1])
            
                    if len(l2) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l2)):
                                aux.append(l2[j][i])
                            dts_A3_double.append(statistics.mean(aux))

                            
                        
                elif len(l3) < 10:
                    
                    l3.append(sl[1])
            
                    if len(l3) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l3)):
                                aux.append(l3[j][i])
                            dts_A4_double.append(statistics.mean(aux))

                    
                      
                elif len(l4) < 10:

                    l4.append(sl[1])
            
                    if len(l4) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l4)):
                                aux.append(l4[j][i])
                            dts_A5_double.append(statistics.mean(aux))


                                                
                elif len(l5) < 10:

                    l5.append(sl[1])
            
                    if len(l5) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l5)):
                                aux.append(l5[j][i])
                            dts_A6_double.append(statistics.mean(aux))


                                               
                elif len(l6) < 10:

                    l6.append(sl[1])
            
                    if len(l6) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l6)):
                                aux.append(l6[j][i])
                            dts_A7_double.append(statistics.mean(aux))

                                            
                            



    elif caso == "B_float":
        Bf = diccionario[caso].read().split("\n")
        

        l = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        l7 = []
        l8 = []
        
        for linea in Bf:
            
            if len(linea) > 0:
                sl = ast.literal_eval(linea)
                
                if len(l) < 10:
                    Ns_B.append(sl[0])

                    l.append(sl[1])
                
                    if len(l) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l)):
                                aux.append(l[j][i])
                            dts_B1_float.append(statistics.mean(aux))
                      
                    
    
                elif len(l1) < 10:

                    l1.append(sl[1])

                    if len(l1) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l1)):
                                aux.append(l1[j][i])
                            dts_B2_float.append(statistics.mean(aux))

                            
                            
                elif len(l2) < 10:

                    l2.append(sl[1])
            
                    if len(l2) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l2)):
                                aux.append(l2[j][i])
                            dts_B3_float.append(statistics.mean(aux))

                            
                        
                elif len(l3) < 10:
                    
                    l3.append(sl[1])
            
                    if len(l3) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l3)):
                                aux.append(l3[j][i])
                            dts_B4_float.append(statistics.mean(aux))

                    
                      
                elif len(l4) < 10:

                    l4.append(sl[1])
            
                    if len(l4) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l4)):
                                aux.append(l4[j][i])
                            dts_B5_float.append(statistics.mean(aux))


                                                
                elif len(l5) < 10:

                    l5.append(sl[1])
            
                    if len(l5) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l5)):
                                aux.append(l5[j][i])
                            dts_B6_float.append(statistics.mean(aux))


                                               
                elif len(l6) < 10:

                    l6.append(sl[1])
            
                    if len(l6) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l6)):
                                aux.append(l6[j][i])
                            dts_B7_float.append(statistics.mean(aux))

                                            
                            
                elif len(l7) < 10:

                    l7.append(sl[1])
            
                    if len(l7) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l7)):
                                aux.append(l7[j][i])
                            dts_B8_float.append(statistics.mean(aux))


                        
                elif len(l8) < 10:

                    l8.append(sl[1])
        
                    if len(l8) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l8)):
                                aux.append(l8[j][i])
                            dts_B9_float.append(statistics.mean(aux))


    elif caso == "B_double":
        Bd = diccionario[caso].read().split("\n")
        

        l = []
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        l7 = []
        l8 = []
        
        for linea in Bd:
            
            if len(linea) > 0:
                sl = ast.literal_eval(linea)

                if len(l) < 10:

                    l.append(sl[1])
                
                    if len(l) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l)):
                                aux.append(l[j][i])
                            dts_B1_double.append(statistics.mean(aux))
                      
                    
    
                elif len(l1) < 10:

                    l1.append(sl[1])

                    if len(l1) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l1)):
                                aux.append(l1[j][i])
                            dts_B2_double.append(statistics.mean(aux))

                            
                            
                elif len(l2) < 10:

                    l2.append(sl[1])
            
                    if len(l2) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l2)):
                                aux.append(l2[j][i])
                            dts_B3_double.append(statistics.mean(aux))

                            
                        
                elif len(l3) < 10:
                    
                    l3.append(sl[1])
            
                    if len(l3) == 10:

                        for i in range(20):
                            aux=[]
                            for j in range(len(l3)):
                                aux.append(l3[j][i])
                            dts_B4_double.append(statistics.mean(aux))

                    
                      
                elif len(l4) < 10:

                    l4.append(sl[1])
            
                    if len(l4) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l4)):
                                aux.append(l4[j][i])
                            dts_B5_double.append(statistics.mean(aux))


                                                
                elif len(l5) < 10:

                    l5.append(sl[1])
            
                    if len(l5) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l5)):
                                aux.append(l5[j][i])
                            dts_B6_double.append(statistics.mean(aux))


                                               
                elif len(l6) < 10:

                    l6.append(sl[1])
            
                    if len(l6) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l6)):
                                aux.append(l6[j][i])
                            dts_B7_double.append(statistics.mean(aux))

                                            
                            
                elif len(l7) < 10:

                    l7.append(sl[1])
            
                    if len(l7) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l7)):
                                aux.append(l7[j][i])
                            dts_B8_double.append(statistics.mean(aux))


                        
                elif len(l8) < 10:

                    l8.append(sl[1])
        
                    if len(l8) == 10:
    
                        for i in range(20):
                            aux=[]
                            for j in range(len(l8)):
                                aux.append(l8[j][i])
                            dts_B9_double.append(statistics.mean(aux))



diccionario["A_float"].close()
diccionario["A_double"].close()
diccionario["B_float"].close()
diccionario["B_double"].close()



N0 = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
dt_label = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
dt0 = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]


plt.title("Caso A Float")
plt.loglog(Ns_A[0],dts_A1_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A2_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A3_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A4_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A5_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A6_float, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A7_float, marker="o", markersize=5)
plt.autoscale(True,True,True)
plt.ylabel("Tiempo Transcurrido [s]")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xlabel("Tamaño Matriz N")
plt.xticks(N0, N0, rotation=45)
plt.legend(["x = Am1*b", "Solve por defecto", "assume_a='pos'", "assume_a='sym'", "overwrite_a=True", "overwrite_b=True", "overwrite_a=True y overwrite_b=True"])
plt.savefig("Caso A Float", bbox_inches = 'tight')
plt.show()



plt.title("Caso A Double")
plt.loglog(Ns_A[0],dts_A1_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A2_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A3_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A4_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A5_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A6_double, marker="o", markersize=5)
plt.loglog(Ns_A[0],dts_A7_double, marker="o", markersize=5)
plt.autoscale(True,True,True)
plt.ylabel("Tiempo Transcurrido [s]")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xlabel("Tamaño Matriz N")
plt.xticks(N0, N0, rotation=45)
plt.legend(["x = Am1*b", "Solve por defecto", "assume_a='pos'", "assume_a='sym'", "overwrite_a=True", "overwrite_b=True", "overwrite_a=True y overwrite_b=True"])
plt.savefig("Caso A Double", bbox_inches = 'tight')
plt.show()



plt.title("Caso B Float")
plt.loglog(Ns_B[0],dts_B1_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B2_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B3_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B4_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B5_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B6_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B7_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B8_float, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B9_float, marker="o", markersize=5)
plt.autoscale(True,True,True)
plt.ylabel("Tiempo Transcurrido [s]")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xlabel("Tamaño Matriz N")
plt.xticks(N0, N0, rotation=45)
plt.legend(["Eigh por defecto", "driver='ev', overwrite_a=False", "driver='ev', overwrite_a=True", "driver='evd', overwrite_a=False", "driver='evd', overwrite_a=True", "driver='evr', overwrite_a=False", "driver='evr', overwrite_a=True", "driver='evx', overwrite_a=False", "driver='evx', overwrite_a=True"])
plt.savefig("Caso B Float", bbox_inches = 'tight')
plt.show()



plt.title("Caso B Double")
plt.loglog(Ns_B[0],dts_B1_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B2_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B3_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B4_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B5_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B6_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B7_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B8_double, marker="o", markersize=5)
plt.loglog(Ns_B[0],dts_B9_double, marker="o", markersize=5)
plt.autoscale(True,True,True)
plt.ylabel("Tiempo Transcurrido [s]")
plt.yticks(dt0, dt_label)
plt.grid(True)
plt.xlabel("Tamaño Matriz N")
plt.xticks(N0, N0, rotation=45)
plt.legend(["Eigh por defecto", "driver='ev', overwrite_a=False", "driver='ev', overwrite_a=True", "driver='evd', overwrite_a=False", "driver='evd', overwrite_a=True", "driver='evr', overwrite_a=False", "driver='evr', overwrite_a=True", "driver='evx', overwrite_a=False", "driver='evx', overwrite_a=True"])
plt.savefig("Caso B Double")
plt.show()
