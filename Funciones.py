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
    return ( round(num1[0]*num2[0]-num1[1]*num2[1],2),round(num1[0]*num2[1]+num1[1]*num2[0],2))
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
def conjugado_v(num1):
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
    """
    Vec_complex,Vec_complex->Vec_complex
    Retorna la suma de dos vectores complejos
    """
    new_vec=[0 for i in range(len(vec1))]
    for i in range(len(new_vec)):
        new_vec[i]=suma(vec1[i],vec2[i])
    return new_vec
def inverse_add(vec):
    """
    Vec_complex->Vec_complex
    Retorna el inverso aditivo de un vector
    """
    inverse=[]
    for i in range(len(vec)):
        inverse.append((-vec[i][0],-vec[i][1]))
    return inverse
def esc_complex(esc,vec):
    """
    complex,matriz->matriz
    Retorna el producto de un complejo por cada elemento de una matriz
    """
    for i in range(len(vec)):
        vec[i]=producto(vec[i],esc)
    return vec
def add_mat_complex(mat1,mat2):
    """
    matriz,matriz->matriz
    retorna la suma de dos matrices complejas
    """
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j]=suma(mat1[i][j],mat2[i][j])
    return mat1
def inverse_mat(mat):
    """
    matriz->matriz
    retorna el inverso aditivo de una matriz
    """
    for i in range(len(mat)):
        mat[i]=inverse_add(mat[i])
    return mat
def esc_mat(esc,mat):
    """
    comlex,matriz->matriz
    retorna la multiplicacion de una matriz con un numero complejo
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j]=producto(esc,mat[i][j])
    return mat
def traspuesta(mat):
    """
    mat->mat
    retorna la traspuesta de una matriz
    """
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
    """
    matriz->matriz
    retorna la conjugada de una matriz
    """
    if type(mat[0])==tuple:
        for i in range(len(mat)):
            mat[i]=(mat[i][0],-mat[i][1])
    else:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=(mat[i][j][0],-mat[i][j][1])
    return mat
def adjunta(mat):
    """
    matriz->matriz
    retorna la adjunta de una matriz
    """
    return(conjugada(traspuesta(mat)))
def prod_mat(mat1,mat2):
    """
    matriz,matriz->matriz
    retorna el producto de dos matrices
    """
    n=len(mat1)
    m=len(mat2[0])
    prod=[["" for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            valor=(0,0)
            for k in range(len(mat2)):
                val1=mat2[k][j]
                val2=mat1[i][k]
                valor=suma(valor,producto(val1,val2))
            prod[i][j]=valor
    return prod
def acc_mat_vec(mat,vec):
    """
    matriz,vector->matriz/vector
    retorna el resultado de el producto de un vector y una matriz
    """
    fil=len(mat)
    new_vec=[0 for i in range(fil)]
    for i in range(len(mat)):
        valor=(0,0)
        for j in range(len(mat[i])):
            valor=suma(valor,producto(mat[i][j],vec[j]))
        new_vec[i]=valor
    return new_vec
def prod_int(vec1,vec2):
    salida=(0,0)
    for i in range(len(vec1)):
        vec1[i]=conjugado(vec1[i])
        salida=suma(salida,producto(vec1[i],vec2[i]))
    return salida
def norma(vec):
    prod=prod_int(vec[:],vec)
    return sqrt(prod[0])
def distancia(vec1,vec2):
    new_vec=[]
    for i in range(len(vec2)):
        vec2[i]=-vec2[i][0],-vec2[i][1]
        new_vec.append(suma(vec1[i],vec2[i]))
    return norma(new_vec)
def mat_unitaria(mat):
    new_mat=[[(0,0) for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0])):
            if i==j:
                new_mat[i][j]=(1,0)
    mat2=mat[:]
    unit=prod_mat(mat,mat2)
    cond=True
    for i in range(len(unit)):
        for j in range(len(unit[i])):
            cond=(unit[i][j][0]==new_mat[i][j][0] and unit[i][j][1]==new_mat[i][j][1])
            if not cond:
                return False
    return cond
def hermit(mat):
    return adjunta(mat[:])==mat
def prod_tensor(element1,element2):
    filas=len(element1*len(element2))
    if type(element1[0])==tuple or type(element2[0])==tuple:
        columnas=1
    else:
        columnas=len(element1[0])*len(element2[0])
    new_mat=[]
    for i in range(len(element1)):
        for j in range(len(element1[0])):
            element1[i][j]=esc_mat(element1[i][j],element2)
    for i in element1:
        print(i)

##Pruebas:
print("Pruebas suma:")
print("1:")
print(suma((1,4),(8,-9)))
print("2:")
print(suma((7,-1),(8,-2)))
print("Pruebas resta:")
print("1:")
print(resta((1,4),(-8,-9)))
print("2:")
print(resta((7,-1),(8,-2)))
print("Pruebas producto:")
print("1:")
print(producto((1,5),(8,0)))
print("2:")
print(producto((7,-1),(4,-2)))
print("Pruebas division:")
print("1:")
print(division((1,4),(-8,-9)))
print("2:")
print(division((7,-1),(8,-2)))
print("Pruebas modulo")
print("1:")
print(modulo((1,4)))
print("2:")
print(modulo((7,-1)))
print("Pruebas conjugado")
print("1:")
print(conjugado_v((1,4)))
print("2:")
print(conjugado_v((8,-2)))
print("Pruebas cambio de coordenadas")
print("1:")
print(pol_cart((1,5),"cartesianas"))
print("2:")
print(pol_cart((2,45),"polares"))
print("Pruebas fase")
print("1:")
print(fase((1,4),"cartesianas"))
print("2:")
print(fase((7,-1),"polares"))
print("Pruebas Adición de vectores complejos")
print("1:")
print(ad_vec_complex([(1,0),(1,1),(-4,5)],[(1,2),(4,4),(7,1)]))
print("2:")
print(ad_vec_complex([(1,5),(1,1)],[(4,5),(2,0)]))
print("Pruebas Inverso (aditivo) de un vector complejo.")
print("1:")
print(inverse_add([(1,0),(1,1),(-4,5)]))
print("2:")
print(inverse_add([(1,5),(1,1)]))
print("Pruebas Multiplicación de un escalar por un vector complejo.")
print("1:")
print(esc_mat((4,1),[[(1,0),(2,4)],[(5,4),(1,1)]]))
print("2:")
print(esc_mat((0,1),[[(1,1),(1,0),(2,4)],[(8,8),(5,4),(1,1)]]))
print("Pruebas Adición de matrices complejas.")
print("1:")
print(add_mat_complex([[(1,2),(2,3)],[(4,5),(1,1)],[(1,0),(4,1)]],[[(1,1),(0,0)],[(1,8),(10,9)],[(1,0),(3,4)]]))
print("2:")
print(add_mat_complex([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]],[[(1,1),(10,10),(7,6)],[(2,2),(1,8),(10,9)],[(4,4),(1,0),(3,4)]]))
print("Pruebas Inversa (aditiva) de una matriz compleja.")
print("1:")
print(inverse_mat([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]]))
print("2:")
print(inverse_mat([[(1,1),(0,0)],[(1,8),(10,9)],[(1,0),(3,4)]]))
print("Pruebas Multiplicación de un escalar por una matriz compleja.")
print("1:")
print(esc_mat((0,1),[[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]]))
print("2:")
print(esc_mat((1,8),[[(1,0),(2,4)],[(5,4),(1,1)]]))
print("Pruebas Transpuesta de una matriz/vector")
print("1:")
print(traspuesta([[(1,0),(2,4)],[(5,4),(1,1)]]))
print("2")
print([(1,0),(1,1),(-4,5)])
print("Pruebas Conjugada de una matriz/vector")
print("1:")
print(conjugada([[(1,0),(2,4)],[(5,4),(1,1)]]))
print("2:")
print(conjugada([(1,1),(0,0)]))
print("Pruebas adjunta")
print("1:")
print(adjunta([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]]))
print("2:")
print(adjunta([(1,0),(2,4)]))
print("Pruebas producto matrices:")
print("1:")
print(prod_mat([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]],[[(14,-8),(30,13),(14,40)],[(0,1),(0,0),(-100,90)],[(1,-10),(4,0),(1,1)]]))
print("2:")
print(prod_mat([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]],[[(1,8),(0,3),(4,4)],[(10,10),(0,0),(21,9)],[(1,0),(14,1),(7,9)]]))
print("Pruebas accion matriz sobre vector")
print("1:")
print(acc_mat_vec([[(1,0),(2,4)],[(5,4),(1,1)]],[(1,0),(4,1),(0,9)]))
print("2:")
print(acc_mat_vec([[(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)],[(1,0),(4,1),(0,9)]],[(1,8),(0,3),(4,4)]))
print("pruebas Producto interno de dos vectores")
print("1:")
print(prod_int([(1,0),(2,4)],[(1,10),(7,8)]))
print("2:")
print(prod_int([(1,8),(0,3),(4,4)],[(0,1),(0,0),(-100,9)]))