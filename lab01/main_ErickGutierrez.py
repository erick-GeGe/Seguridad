#Erick Gutierrez Enriquez 

import string

#Operacion #1
def sustituciones(texto):
    text_aux=list(texto)
    for i in range(len(texto)):
        if texto[i]=='j':
            text_aux[i]='i'
        elif texto[i]=='h':
            text_aux[i]='i'
        elif texto[i]=='ñ':
            text_aux[i]='n'
        elif texto[i]=='k':
            text_aux[i]='l'
        elif texto[i]=='u':
            text_aux[i]='v'
        elif texto[i]=='w':
            text_aux[i]='v'
        elif texto[i]=='y':
            text_aux[i]='z'
    return ''.join(text_aux)

#Operacion #2
def eliminacion_tildes(texto):
    text_aux=list(texto)
    for i in range(len(texto)):
        if texto[i]=='á':
            text_aux[i]='a'
        elif texto[i]=='é':
            text_aux[i]='e'
        elif texto[i]=='í':
            text_aux[i]='i'
        elif texto[i]=='ó':
            text_aux[i]='o'
        elif texto[i]=='ú':
            text_aux[i]='u'

    return ''.join(text_aux)

#Operacion 3
def convertir_mayusculas(texto):
    return texto.upper()

#Operacion 4
def espacios_puntuacion(texto):
    text_aux=list(texto)
    for i in range(-1,len(texto)):
        if texto[i] in string.punctuation or texto[i]==' ' or texto[i]=='\n' or texto[i]=='¡' or texto[i]=='¿':
            text_aux[i]=''

    return ''.join(text_aux)

#Operacion #5
def obtener_frecuencias(texto):
    dic={}
    for i in range(len(texto)):
        dic.setdefault(texto[i],0)
    for i in range(len(texto)):
        dic[texto[i]]+=1
    return dic

#Operacion 5.1
def mayor_frecuencia(tabla):
    for i in range(5):
        mayor=''
        for j in tabla:
            mayor = j
            break
        for j in tabla:
            if tabla[mayor] < tabla[j]:
                mayor = j
        print('\t',mayor, tabla[mayor])
        tabla.pop(mayor)

#Operacion #6
def obtener_trigramas(texto):
    dic={}
    for i in range(0,len(texto)-2):
        dic.setdefault(texto[i:i+3],[0,[]])
    for i in range(0,len(texto)-2):
        dic[texto[i:i+3]][0]+=1
        dic[texto[i:i+3]][1].append(i)
    # print(dic)
    trigramas={}
    for i in range(5):
        mayor=''
        for j in dic:
            mayor = j
            break
        for j in dic:
            if dic[mayor][0] < dic[j][0]:
                mayor = j
        # print('\t',mayor, dic[mayor])
        trigramas.setdefault(mayor,dic[mayor])
        dic.pop(mayor)
    return trigramas



def main():
    texto=open('plain-text.txt', encoding='utf-8')
    #1. Realizar las siguientes sustituciones: j x i, h x i, ñ x n, k x l, u x v, w x v, y x z
    texto=sustituciones(texto.read())
    print('********************Operacion #1************************')
    print(texto)
    #2. Elimine las tildes
    texto=eliminacion_tildes(texto)
    print('********************Operacion #2************************')
    print(texto)
    #3. Convierta todas las letras a mayúsculas
    texto=convertir_mayusculas(texto)
    print('********************Operacion #3************************')
    print(texto)
    #4. Elimine los espacios en blanco y los signos de puntuación
    texto=espacios_puntuacion(texto)
    print('********************Operacion #4************************')
    print(texto)
    #Guarde el resultado en el archivo “HERALDOSNEGROS_pre.txt”
    archivo=open('HERALDOSNEGROS_pre.txt', 'w')
    archivo.write(texto)
    archivo.close()
    #5. Abra el archivo generado e implementar una función que calcule una tabla de frecuencias para cada letra de la ’A’ a ’Z’. La función deberá definirse como frecuencias(archivo) deberá devolver un diccionario cuyos índices son las letras analizadas y cuyos valores son las frecuencias de las mismas en el texto (número de veces que aparecen). Reconozca en el resultado obtenido los cinco caracteres de mayor frecuencia
    texto=open('HERALDOSNEGROS_pre.txt')
    tabla=obtener_frecuencias(texto.read())
    print('********************Operacion #5************************')
    print(tabla)
    print('Cinco caracteres con mayor frecuencia:')
    mayor_frecuencia(tabla)
    #6. Aplicar el método Kasiski, que recorre el texto preprocesado y halla los trigramas en el mismo (sucesión de tres letras seguidas que se repiten) y las distancias (número de caracteres entre ellos) entre los trigramas
    texto=open('HERALDOSNEGROS_pre.txt')
    trigramas=obtener_trigramas(texto.read());
    print('********************Operacion #6************************')
    for i in trigramas:
        distancias=[]
        for j in range(1, len(trigramas[i][1])):
            distancias.append(trigramas[i][1][j] - trigramas[i][1][j-1])
        print(i, '\tfrecuencia:'+str(trigramas[i][0])+'\tdistancias:'+str(distancias))





if __name__ == "__main__":
    main()
