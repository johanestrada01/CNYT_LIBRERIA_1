from math import sqrt, cos, sin, atan, radians, degrees
def suma(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna la suma de dos numeros complejos
    """
    return (num1[0]+num2[0],num1[1]+num2[1])
def producto(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna el producto de dos numeros complejos
    """
    return (num1[0]*num2[0]-num1[1]*num2[1],num1[0]*num2[1]+num1[1]*num2[0])
def resta(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna la suma de dos numeros complejos
    """
    return (num1[0] - num2[0], num1[1] - num2[1])
def division(num1,num2):
    """Tupla,Tupla->Tupla
    Retorna la division de dos numeros complejos
    """
    num3=(num2[0],-num2[1])
    num4=producto(num2,num3)
    new_number=producto(num1,num3)
    return (new_number[0]/num4[0]+num4[1],new_number[1]/num4[0]+num4[1])
def modulo(num1):
    """
    Tupla->real
    retorna el modulo de un numero complejo
    """
    return sqrt(num1[0]**2+num1[1]**2)
def conjugado(num1):
    """
    Tupla->Real
    returna el conjugado del numero complejo
    """
    return (num1[0],-num1[1])
def pol_cart(coordenadas,tipo):
    """
    Tupla,str->Tupla
    Debe ingresar el sistema de coordenadas en las que se encuentra en minusculas
    Realiza el cambio de coordenadas de cartesianas a polares, o polares a cartesianas
    """
    if tipo=="polares":
        coordenadas=(coordenadas[0],radians(coordenadas[1]))
        x = coordenadas[0] * cos(coordenadas[1])
        y = coordenadas[1] * sin(coordenadas[1])
        return (x, y)
    else:
        polares = (sqrt(coordenadas[1] ** 2 + coordenadas[0] ** 2), degrees(atan(coordenadas[1] / coordenadas[0])))
        return polares

def fase(coordenadas, tipo):
    """
    Tupla,str->Tupla
    Debe ingresar el sistema de coordenadas en las que se encuentra en minusculas
    Regresa la fase del vector comlejo
    """
    if tipo == "cartesianas":
        coordenadas = pol_cart(coordenadas, tipo)
        return radians(coordenadas[1])
    else:
        return coordenadas[1]
def ad_vec_complex(vec1,vec2):
    new_vec=[0 for i in range(len(vec1))]
    for i in range(len(new_vec)):
        new_vec[i]=suma(vec1[i],vec2[i])
    return new_vec
def inverse_add(vec):
    inverse=[]
    for i in range(len(vec)):
        inverse.append((-vec[i][0],-vec[i][1]))
    return inverse
def esc_complex(esc,vec):
    for i in range(len(vec)):
        vec[i]=producto(vec[i],esc)
    return vec
def add_mat_complex(mat1,mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j]=suma(mat1[i][j],mat2[i][j])
    return mat1
def inverse_mat(mat):
    for i in range(len(mat)):
        mat[i]=inverse_add(mat[i])
    return mat
def esc_mat(esc,mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]=producto(esc,mat[i][j])
    return mat
def traspuesta(mat):
    elements=[]
    if type(mat[0])==int:
        new_mat = [[] for i in range(len(mat))]
        for i in range(len(mat)):
            new_mat[i].append(mat[i])
    else:
        new_mat = [[] for i in range(len(mat[0]))]
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                new_mat[i].append(mat[j][i])
    return new_mat
def conjugada(mat):
    if type(mat[0])==tuple:
        for i in range(len(mat)):
            mat[i]=(mat[i][0],-mat[i][1])
    else:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=(mat[i][j][0],-mat[i][j][1])
    return mat
def adjunta(mat):
    return(conjugada(traspuesta(mat)))
def prod_mat(mat1,mat2):
    resultado=[[] for i in range(len(mat1))]
    for i in range(len(mat1)):
        suma=0
        for j in range(len(mat1[0])):
            print(i,j)
            suma+=mat1[i][j]*mat2[j][i]
        resultado[i].append(suma)
    return resultado
print(prod_mat([[1,2],[3,4],[5,6]],[[1,2,3],[1,2,3]]))

##Pruebas:
#print("Pruebas suma:")
#print("1:")
#print(suma((1,4),(8,-9)))
#print("2:")
#print(suma((7,-1),(8,-2)))
#print("Pruebas resta:")
#print("1:")
#print(resta((1,4),(-8,-9)))
#print("2:")
#print(resta((7,-1),(8,-2)))
#print("Pruebas producto:")
#print("1:")
#print(producto((1,5),(8,0)))
#print("2:")
#print(producto((7,-1),(4,-2)))
#print("Pruebas division:")
#print("1:")
#print(division((1,4),(-8,-9)))
#print("2:")
#print(division((7,-1),(8,-2)))
#print("Pruebas modulo")
#print("1:")
#print(modulo((1,4)))
#print("2:")
#print(modulo((7,-1)))
#print("Pruebas conjugado")
#print("1:")
#print(conjugado((1,4)))
#print("2:")
#print(conjugado((8,-2)))
#print("Pruebas cambio de coordenadas")
#print("1:")
#print(pol_cart((1,5),"cartesianas"))
#print("2:")
#print(pol_cart((2,45),"polares"))
#print("Pruebas fase")
#print("1:")
#print(fase((1,4),"cartesianas"))
#print("2:")
#print(fase((7,-1),"polares"))
