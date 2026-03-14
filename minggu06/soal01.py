def perkalian(a, b):
    hasil = 0
    string = ""
    for i in range(a):
        hasil += b
        if i < a -1:
            string += str(b) + " + "  
        else:
            string += str(b)
    print(str(a) + " x " + str(b) + " = " + string + " = " + str(hasil) + ".")
    return hasil

perkalian(6,5)
perkalian(7,10) 


