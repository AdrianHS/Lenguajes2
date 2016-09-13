def separar(num,pagina,count,lista1):
    a=count%num
    list=[]
    lista=[]
    if(a==0):
        for x in range(count):
            if (x % num == 0 ):
                list.append(lista)
                lista=[]
            lista.append(lista1[x])
        list.append(lista)
        return list[pagina]
    else:
        for x in range(count - (a - 1)):
            if (x % num == 0):
                list.append(lista)
                lista = []
            lista.append(lista1[x])
        list.append(lista1[count - a:])
        return list[pagina]

y=[7]
print(separar(5,0,1,y))