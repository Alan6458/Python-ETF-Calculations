import yfinance as yf
# gets history
i = 0
# the file path. Change it to match your project. A backslash is written as \\, not \.
path = 'C:\\file path\\CSV Files\\'
# opens "Table.txt" and puts it into a list
file = open('Table.txt')
content = file.readlines()
while i <= len(content):
    # requests the data. It might not be exactly the same as the graph on some websites.
    new = content[i].replace("\n", "")
    thing = yf.Ticker(new)
    # sets the period to max. You could do a different period of time if you would like.
    data = thing.history(period="max")
    # Detects forbidden Windows files names and changes them
    if new == "CON" or new == "PRN" or new == "AUX" or new == "NUL":
        new = new + " " + new
    # Puts the data into a CSV file
    data.to_csv(path + new + '.csv')
    print(i)
    i += 1
