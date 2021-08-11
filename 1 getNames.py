import requests
# gets top 1600 or so ETFs
i = 0
while i <= 65:
    # this is the url I'm using to get the top 1600 or so ETFs
    url = 'https://etfdb.com/data_set/?tm=88057&cond={%22by_type%22:[%22Etfdb::EtfType%22,1930,null,false,' \
          'false]}&no_null_sort=true&count_by_id=&limit=25&sort=assets_under_management&order=desc&limit=25' \
          '&offset=' + str(i * 25)
    html = requests.get(url).content
    if html == "":
        print(str(i) + " is empty")
    ht = html.decode()
    printStr = ''
    printStrBefore = ''
    # prints the data
    while ht.find('href=\\"/etf/') > 0:
        # the ETF name begins here:
        start = ht.find('href=\\"/etf/')
        # clears the unnecessary stuff
        printStr = ht[start + 12:start + 16].replace('/', '').replace('#', '').replace("\\", '')
        # makes sure that it isn't the same as the one before
        if printStr != printStrBefore:
            # prints the ETF
            print(printStr)
        # sets the current ETF name as the past ETF name
        printStrBefore = printStr
        # Continues with the next ETF
        ht = ht[start + 17:]
    i += 1
# make sure to copy and paste the printed stuff into Table.txt
