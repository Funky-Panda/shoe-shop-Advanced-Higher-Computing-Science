from tabulate import tabulate
import os

def getShoes():
    print("Please enter the shoe size of each shoe that you have sold today!")
    sizes = []
    for i in range(20):
        currentShoe = validateShoe(i)
        sizes.append(currentShoe)
        counts = countSizes(sizes)
        createSizeTable(counts)
    return sizes
    # return [5, 6, 5, 6, 8, 6, 9, 6, 6, 6, 5, 8, 7, 7, 7, 7, 7, 7, 6, 7]
    

def validateShoe(currentIndex):
    while True:
        try:
            currentShoe = int(input(f"Shoe {currentIndex+1}: "))
            if currentShoe < 4 or currentShoe > 12:
                print("Please enter an adult shoe size between 4 and 12")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return currentShoe

def countSizes(sizes):
    counts = {}
    for i in range(len(sizes)):
            count = 0
            for j in range(len(sizes)):
                if sizes[i] == sizes[j]:
                    count += 1
            counts[sizes[i]] = count    
    return counts
    
def createSizeTable(data):
    os.system("clear")
    headers = ["Shoe Sizes", "Each Size Sold"]
    table_data = [[size, count] for size, count in data.items()]
    print(tabulate(table_data, headers=headers, tablefmt="rounded_outline"))

def getMostPopular(sizes):
    mostPopularSold = next(iter(sizes.items()))[1]
    mostPopularSize = next(iter(sizes.items()))[0]
    duplicates = []
    
    for size, count in sizes.items():
        if count > mostPopularSold:
            mostPopularSold = count
            mostPopularSize = size

    for size, count in sizes.items():
        if mostPopularSold == count:
            duplicates.append(size)
    
    if len(duplicates) == 1:
        print(f"The most popular sold shoe size was {mostPopularSize}. Which sold {mostPopularSold} shoes!")
    else:
        print(f"The most popular sold shoes size are {', '.join(str(d) for d in duplicates)}. Which sold {mostPopularSold} shoes!")

    
sizes = getShoes()
counts = countSizes(sizes)
createSizeTable(counts)
getMostPopular(counts)