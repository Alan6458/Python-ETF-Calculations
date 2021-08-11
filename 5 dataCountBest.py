import random
import pandas
import pandas as pd
import numpy as np
number = 0
best = [0, "nothing"]
newList = [""]

# Picks the best from the top 10. Same as dataCount.py
def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    returns = np.sum(mean_returns @ weights) * 252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    return std, returns


def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    results = np.zeros((num_stocks, num_portfolios))
    weights_record = []
    for i in range(num_portfolios):
        weights = np.random.random(num_stocks)
        weights /= np.sum(weights)
        weights_record.append(weights)
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)
        results[0, i] = portfolio_std_dev
        results[1, i] = portfolio_return
        results[2, i] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


def display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    results, weights = random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate)

    max_sharpe_idx = np.argmax(results[2])
    sdp, rp = results[0, max_sharpe_idx], results[1, max_sharpe_idx]
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx], index=all_df.columns, columns=['allocation'])
    max_sharpe_allocation.allocation = [round(i * 100, 2) for i in max_sharpe_allocation.allocation]
    max_sharpe_allocation = max_sharpe_allocation.T

    min_vol_idx = np.argmin(results[0])
    sdp_min, rp_min = results[0, min_vol_idx], results[1, min_vol_idx]
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx], index=all_df.columns, columns=['allocation'])
    min_vol_allocation.allocation = [round(i * 100, 2) for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T
    roundrp = round(rp, 2)
    roundsdp = round(sdp, 2)
    roundrpmin = round(rp_min, 2)
    roundsdpmin = round(sdp_min, 2)

    print("-" * 80)
    print("Maximum Sharpe Ratio Portfolio Allocation\n")
    print("Annualised Return:", round(rp, 2))
    print("Annualised Volatility:", round(sdp, 2))
    print("\n")
    print(max_sharpe_allocation)
    print("-" * 80)
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min, 2))
    print("Annualised Volatility:", round(sdp_min, 2))
    print("\n")
    print(min_vol_allocation)

    if best[0] < roundrp/roundsdp:
        best.clear()
        best.append(roundrp/roundsdp)
        best.append(str(max_sharpe_allocation))
    if best[0] < roundrpmin/roundsdpmin:
        best.clear()
        best.append(roundrpmin/roundsdpmin)
        best.append(str(min_vol_allocation))
    return max_sharpe_allocation, min_vol_allocation


while number < 500:
    print(number)
    stock_codes = []
    # Your file below
    file = open('data 10.txt')
    content = file.readlines()
    while len(stock_codes) < 5:
        Number = random.randrange(0, 9)
        contentNumber = content[Number].replace("\n", "")
        if contentNumber == "CON" or contentNumber == "PRN" or contentNumber == "AUX" or contentNumber == "NUL":
            contentNumber = contentNumber + " " + contentNumber
        if contentNumber not in stock_codes:
            stock_codes.append(contentNumber)
    stock_codes.sort()
    stockcodes = ' '.join(stock_codes)
    num_stocks = len(stock_codes)
    stock_daily_quotes = {}
    notIn = any(stockcodes not in newList[a] for a in range(len(newList)))
    if notIn:
        newList.append(stockcodes)
        for code in stock_codes:
            if code == "CON" or code == "PRN" or code == "AUX" or code == "NUL":
                code = code + ' ' + code
            df = pandas.read_csv('C:\\file path\\CSV Files\\' + code + '.csv')
            df[code] = df['Close']
            stock_daily_quotes[code] = df[code]
        all_df = pd.concat([value for _, value in stock_daily_quotes.items()], axis=1)

        all_df.head()

        all_df = all_df.dropna()

        returns = all_df.pct_change()
        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        num_portfolios = int(25000 / 2.5 * num_stocks)
        risk_free_rate = 0.005
        max_sharpe_alloc, min_vol_alloc = display_simulated_ef_with_random(mean_returns, cov_matrix, num_portfolios,
                                                                           risk_free_rate)
        number += 1
print(best)
