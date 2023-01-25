def burbuja(lista):
    for i in range(0, lista.__len__()):
        flag = True
        for j in range(0, lista.__len__()-i-1):
            if (lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                flag = False
        if flag: break
        print(lista)
    return lista


print(burbuja([5, 2, 3, 4, 1]), " Final")
print(burbuja([5, 4, 3, 2, 1]), " Final")
print(burbuja([1, 2, 3, 4, 5]), " Final")
print(burbuja([2, 1, 3, 4, 5]), " Final")
