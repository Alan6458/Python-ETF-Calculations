Calculating the Calmar ratio and portfolio optimization using randomized efficient frontier with Pythonthe by using the top 1600 US ETFs.
Note that calculations are for all time, but this could be changed.
Run at your own risk if you do not understand the code at all.

Please run in this order:

1. getNames.py:
Scrapes data from a website to obtain the names of the top 1600 ETFs
2. getData.py:
Uses yfinance to get the history of the top 1600 ETFs
3. ratio.py:
Uses the Calmar ratio to make a list of 100 ETFs with the highest Calmar ratio
4. dataCount.py or dataCountBest.py:
Uses randomized efficient frontier to find the combination of ETFs with the largest annualized return and the lowest annualized volatility


getNames.py uses the website https://etfdb.com/etfs/country/us/ and scrapes data from the table to get the top 1600 ETF names.

  The URL used to scrape the data is not the same as the one shown here because it uses lazyloading (if you open the website, it would take a second or two for the first table to load). The URL shown in getNames.py was obtained through Chrome dev tools (network tab), which could be accessed by right clicking on a site in chrome and then slelecting "Inspect". As far as I know, the inspect function could be disabled by your school or company. One way I use it is by waiting for the page to load, then clicking on "page 2" and seeing if anything new pops up. As far as I know, the current link does not work.
  Everything is repeated 65 times because there are a total of 65 pages, each with a small list of ETFs. Because all of the ETFs are repeated several times in the link, we should make sure that it is not the same as the one before it. If it is not, then the result would be printed. If it is, then the result would not be printed and the program will continue with the next ETF that starts with href=\"/etf/, which should be about 12 characters after the first one. After the program is finished running, copy and paste the results into Table.txt.

The printed results:
![Graph Example Image](https://github.com/Alan6458/Python-ETF-Calculations/blob/main/Images/Names.png?raw=true)

getData.py uses yFinance to get the history of the top 1600 ETFs (from getNames.py) and puts them into CSV files for later use.

  In case you don't know, yfinance is a free, open source API that was made after the official Yahoo Finance API was decommissioned in 2015. You can install it using "pip install yfinance" in the terminal, but it already comes preinstalled in Anaconda. The documentation for yfinance is here: https://pypi.org/project/yfinance/ This time, I'm going to be using the Ticker() function (ticker = yf.Ticker("name of stock")), which accesses ticker data, and the history() function (history = yf.history(period="")), which accesses the history of the ticker. Periods of time (period=) that could be fetched inclued minutes, hours, days, weeks, months, and years (m, h, d, wk, mo, y). A start and end (start= and end=) may also be used. The .download function could be used to fetch data for multiple tickers, but I didn't use it this time. "import yfinance as yf" or "import yfinance" could both be used to import yfinance.
  Using the open() function, getData.py opens Table.txt, which contains the top 1600 or so ETFs that we got from getNames.py. Next, the readlines() function is used to read all the lines in Table.txt and puts those lines into the list "content". Then, the while statement seen on line 9 would repeat the same amount of times as there is EFTs in Table.txt. For example, if there are 1000 ETFs or 1000 lines in Table.txt, it would repeat 1000 times because the length of "content" is 1000.
  In the while statement, variable "new" is declared as content but without the \n. This is important because in many situations, the \n would be included. Using Yahoo Finance, ticker data for the ETF represented as "new" would be requested as history. You could change the period of time to anything you like, but we'll just request the maximum period available. The if statement on line 16 is extremely important if you're using the Windows operating system, because the file names CON, PRN, AUX, and NUL are forbidden in Windows. If the ETF's name does match the previously mentioned 4 forbidden file names, then it would be changed. This happens after the history is requested because if it was before, then there would be no ETF that matches the name, meaning that the history we would later save will be blank. There would also be an error that says the file is not found.
  In the final few lines, we use the .to_csv function to put the data we collected into a .csv file. Make sure to change the path string to a path you already have, or it could make an additional unwanted folder. If you're wondering why I'm using .csv files instead of .txt files, it's because it's much easier to read the data from a CSV file than a text file. The while loop at the start could be changed into a for loop, just change it to "for i in range(len(content))" and delete the i += 1 at the end.
  
The CSV file should look like this:
![Graph Example Image](https://github.com/Alan6458/Python-ETF-Calculations/blob/main/Images/CSV%20Example.png?raw=true)
I used the Rainbow CSV plugin in Pycharm, so yours might look a bit different.


ratio.py uses the Calmar ratio (Portfolio Return/Annual Rate of Return) to make a list of ETFs from getNames.py with CSV files from getData.py with the highest Calmar ratio.

  First, Table.txt is opened for reading and the content of the file is put into a list called "file". Next, a new variable is created which deletes the \n from file. An if statement detects if the current name is CON, PRN, AUX, or NUL, and if so, changes them to match the file names. The files are read from the row "Close" (but Open, High, Low, and CLose are all acceptable).
  The Annual Return is calculated on row 29. After that, some variables are set for calculating the Maximum Drawdown. The location of the higher number, i, is chosen and because the smaller number must be after that, i1, the location of the smaller number, is set to i. An if statement determines if the difference of i and i1 is greater than the current greatest difference. This would take about one to fifteen seconds to calculate, but after that, the maximum drawdown is turned into a percentage and the final result is calculated.
  But, we want the top 100. Another if statement determines if the length of top100 is less than 100, and if so, appends the result to the end. If not, and the result is larger than the smallest value in top100, the smallest value is removed and the result is appended to top100. However, you might notice that there's also a list called "top". This is because we want a record of all the values that has ever been in top100. Because we want only floats in top100 and there's no way to see which float corresponds to which ETF, we would need to append both the result and the name of the ETF to top, but only the result to top100.
  After everything is calculated, we can compare the values from top100 to top. If it matches, the value is put into the list "finalTop", without the value or whitespace. Finally, "finalTop" is written into data.txt.

Results of ratio.py:
![Graph Example Image](https://github.com/Alan6458/Python-ETF-Calculations/blob/main/Images/Data.png?raw=true)


dataCount.py optimizes a portfolio through using efficient frontier (with 10 ETFs at a time), and dataCountBest does the same but with 5 ETFs at a time and only the top 10 ETFs.

  dataCount.py and dataCountBest.py is very similar, so I will only be doing one explaination for both. Because this is (mostly) unoriginal, I will only be explaining the code I wrote and briefly explain the code that I didn't. Link to original (I think) is https://zhuanlan.zhihu.com/p/100900447
  First, we can ignore all the functions and come back to them later. The while loop takes ETFs from data.txt and puts them into stock_codes, making sure that there are no repeats. After that, data is read from the CSV files, similar to how it was done earlier. Last of all, one function is used, which uses the other two to calculate the maximum sharpe allocation and the minimum volatility. All of this is put into a text document and printed. A graph would be made and saved to the files, and the program would move to the next set of ETFs to test.
  
Example of the graph:
![Graph Example Image](https://github.com/Alan6458/Python-ETF-Calculations/blob/main/Images/Example.png?raw=true)

See the comments in the files for more information.

Pycharm Community and Anaconda Individual Edition were used.
To install something, click on Terminal in Pycharm and type "pip install" and the thing you want to install.
To run a file in Pycharm, right click on the tab and select "Debug".
