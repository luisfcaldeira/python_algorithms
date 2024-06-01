

def insertionSort(yourList: list):
    A = yourList.copy()
    for j in range(1, len(A)):
        chave = A[j]
        i = j - 1

        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave
        print(A)

    return A


    
if __name__ == '__main__': 

    elements = [5, 6, 7, 1, 2, 3, 4]

    new_elements = insertionSort(elements)
    print('-' * 100)
    print(elements)
    print(new_elements)  