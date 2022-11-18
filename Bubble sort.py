tal = [3, 5, 1, 2, 9, 8]



def sort(tal):
    sorted = True
    
    while (sorted):
        sorted = False
        for i in range(len(tal)):
            for j in range (len(tal) - 1):
                if tal[j] > tal[j +1]:
                    #byter plats
                    tal[j], tal[j + 1] = tal[j + 1], tal[j]
                    sorted = True
                
sort(tal)
print(tal)
    