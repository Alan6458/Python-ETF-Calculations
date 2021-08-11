import csv
# Calmar ratio - Highest 100 for a history of all time, NOT 1 or 3 years
top100 = []
top = []
finalTop = []
# Reads Table.txt to get ETF names
content = open("Table.txt", "r")
file = content.readlines()
content.close()
# Calculations and stuff
for x in range(len(file)):
    print(x)
    List = []
    # Deletes \n
    fileX = file[x].replace("\n", "")
    # Changes name to match CSV files if the name is forbidden on Windows
    if fileX == "CON" or fileX == "PRN" or fileX == "AUX" or fileX == "NUL":
        fileX = fileX + " " + fileX
    # opens and reads the file
    with open("C:\\file path\\" + fileX + ".csv", 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # gets data from the Close row - Open, High, Low, and Close are all ok
            if row.get('Close') != '':
                # Appends the number if it is not blank
                List.append(float(row.get('Close')))
    N = len(List)
    # Calculates annual return
    annual_rtn = ((List[N-1]-List[0])/List[0])
    i = 0
    i1 = 0
    highestDifference = float(0)
    highPoint = 0
    lowPoint = 0
    # Calculates maximum drawdown. Might not be the most efficient way.
    while i <= N-1:
        # Because i is supposed to be the location of the higher number, the location of the lower number must be higher than i.
        i1 = i
        while i1 <= N-1:
            # checks if the maximum drawdown is higher than the previous one
            if List[i] - List[i1] > highestDifference:
                highestDifference = List[i] - List[i1]
                highPoint = List[i]
                lowPoint = List[i1]
            i1 += 1
        i += 1
    # Maximum drawdown, as a percentage
    diff = (highPoint - lowPoint)/highPoint
    # Final result
    result = annual_rtn / diff
    # top 100
    if len(top100) < 100:
        top100.append(result)
        # keeps track of the name
        top.append(str(result)+" "+file[x])
        top100.sort()
    elif len(top100) == 100 and result > min(top100):
        # removes the minimum number and replaces it with the new high
        top100.remove(min(top100))
        top100.append(result)
        # keeps track of the name
        top.append(str(result)+" "+file[x])
# Sees which ones in "top100" is similar to the ones in "top"
for a in range(len(top100)):
    for b in range(len(top)):
        if top[b].startswith(str(top100[a])):
            # removes the numbers from top
            finalTop.append(top[b].replace(str(top100[a]), "").replace(" ", ""))
# opens or creates data.txt
data = open("data.txt", "a")
# appends the results to data.txt
for c in range(len(finalTop)):
    data.write(finalTop[c])
data.close()
