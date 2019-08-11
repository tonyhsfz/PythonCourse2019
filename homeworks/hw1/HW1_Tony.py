from random import uniform

# Create a class for portfolio which includes cash, stock, mutual funds, bonds, and transaction history
class Portfolio:
    def __init__(portfolio):
        portfolio.cash = 0
        portfolio.stock = {}
        portfolio.mu_fund = {}
        portfolio.bonds = {}
        portfolio.transaction = []

    # print(portfolio) will return all items in the portfolio
    def __str__(portfolio):
        # convert the dictionary into a string
        stocklist = []
        for item in portfolio.stock:
            stocklist.append(str(item) + " : " + str(round(portfolio.stock[item],2)))
        # convert the dictionary into a string
        mu_fundlist = []
        for item in portfolio.mu_fund:
            mu_fundlist.append(str(item) + " : " + str(round(portfolio.mu_fund[item],2)))
        # convert the dictionary into a string
        bondslist = []
        for item in portfolio.bonds:
            bondslist.append(str(item) + " : " + str(round(portfolio.bonds[item],2)))
        return """Your portfolio has:
        Cash: %s dollar(s)
        Stocks: %s
        Mutual Funds: %s
        Bonds: %s """ % (str(round(portfolio.cash,2)), str(stocklist), str(mu_fundlist), str(bondslist))

    # create a function for adding cash
    def addCash(portfolio, amount):
        # notice that adding non-positive number is not allowed
        if amount > 0:
            amount = round(amount, 2)
            portfolio.cash += amount
            portfolio.transaction.append("Added " + str(amount) + " dollar(s) of cash to your portfolio.")
        else: print("Warning: You can only add a positive amount of cash to your portfolio. Please input a positive number.")

    # create a function for buying stocks
    def buyStock(portfolio, amount, stock):
        money = amount * stock.price
        # stocks can only be purchased in whole units
        if type(amount) != int:
            print("Warning: You can only buy whole units of stocks. Please input a whole number.")
        # non-positive amount is not allowed
        elif amount <= 0:
            print("Warning: You can only buy positive amount of stocks. Please input a positive whole number.")
        # make sure the client has enough money to buy the stocks
        elif portfolio.cash < money:
            print("Warning: You don't have enough money. Please reduce the amount of your purchase.")
        else:
            portfolio.cash -= money
            # if the stock already exists in the portfolio, then change the amount
            # if it does not exist, then create a new key for the stock
            if stock.symbol in portfolio.stock.keys():
                portfolio.stock[stock.symbol] += amount
            else: portfolio.stock[stock.symbol] = amount
            portfolio.transaction.append("Bought " + str(amount) + " share(s) of stock " + stock.symbol + " to your portfolio.")
            portfolio.transaction.append("Spent " + str(money) + " dollar(s) of cash to buy stocks " + stock.symbol + ".")

    # Create a function for buying mutual funds
    def buyMutualFund(portfolio, amount, mf):
        # non-positive numbers are not allowed
        if type(amount) != float and type(amount) != int and amount <= 0:
            print("Warning: You can only buy positive shares of mutual funds. Please input a positive number.")
        # make sure the client has enough money to buy the mutual funds
        elif portfolio.cash < amount:
            print("Warning: You don't have enough money. Please reduce the amount of your purchase.")
        else:
            amount = round(amount, 2)
            portfolio.cash -= amount
            # if the mutual fund already exists in the portfolio, then change the amount
            # if it does not exist, then create a new key for the stock
            if mf.symbol in portfolio.mu_fund.keys():
                portfolio.mu_fund[mf.symbol] += amount
            else: portfolio.mu_fund[mf.symbol] = amount
            portfolio.transaction.append("Bought " + str(amount) + " share(s) of mutual fund " + mf.symbol + " to your portfolio.")
            portfolio.transaction.append("Spent " + str(amount) + " dollar(s) of cash to buy mutual funds " + mf.symbol + ".")

    # create a function for selling stocks
    # NOTICE: You should enter the name of the stock instead of the symbol!
    def sellStock(portfolio, stock, amount):
        amount = round(amount, 2)
        # make sure the client has enough stocks to sell
        if stock.symbol in portfolio.stock.keys():
            if amount <= portfolio.stock[stock.symbol]:
                portfolio.stock[stock.symbol] -= amount
                # randomly generates the selling price
                price = round(uniform(0.5 * stock.price, 1.5 * stock.price), 2)
                total = round(price * amount, 2)
                portfolio.cash += total
                portfolio.transaction.append("Sold " + str(amount) + " share(s) of stock " + stock.symbol + " at " + str(price) + " dollar(s) per share.")
                portfolio.transaction.append("Earned " + str(total) + " dollar(s) of cash selling stocks " + stock.symbol + ".")
            else:
                print("Warning: You don't have enough shares of stocks to sell in your portfolio. \n\tPlease check your portfolio to see how many shares you have.")
        else:
            print("Warning: You haven't bought any of this type of stocks before. \n\tPlease check your portfolio to see which type of stocks you could sell.")

    # create a function for selling mutual funds
    # NOTICE: You should enter the name of the stock instead of the symbol!
    def sellMutualFund(portfolio, mf, amount):
        amount = round(amount, 2)
        # make sure that the client has enough mutual funds to sell
        if mf.symbol in portfolio.mu_fund.keys():
            if amount <= portfolio.mu_fund[mf.symbol]:
                portfolio.mu_fund[mf.symbol] -= amount
                # randomly generates the selling price
                price = round(uniform(0.9, 1.2), 2)
                total = round(price * amount, 2)
                portfolio.cash += total
                portfolio.transaction.append("Sold " + str(amount) + " share(s) of mutual funds " + mf.symbol + " at " + str(price) + " dollar(s) per share.")
                portfolio.transaction.append("Earned " + str(total) + " dollar(s) of cash selling mutual funds " + mf.symbol + ".")
            else:
                print("Warning: You don't have enough shares of mutual funds to sell in your portfolio. \n\tPlease check your portfolio to see how many shares you have.")
        else:
            print("Warning: You haven't bought any of this type of mutual funds before. \n\tPlease check your portfolio to see which type of stocks you could sell.")

    # create a function for withdrawing cash
    def withdrawCash(portfolio, amount):
        amount = round(amount, 2)
        if amount > 0:
            # make sure that the client does not over-withdraw from the account
            if portfolio.cash < amount:
                print("Warning: You don't have enough cash to withdraw from your portfolio.")
            else:
                portfolio.cash -= amount
                portfolio.transaction.append("Withdrew " + str(amount) + " dollar(s) of cash from your portfolio.")
        else: print("Warning: You can only withdraw a positive amount of cash from your portfolio. Please input a positive number.")

    # create a function for transaction history
    def history(portfolio):
        # if there is not transaction
        if len(portfolio.transaction) == 0:
            print("You don't have any transaction record.")
        else:
            print("Your transaction history is as follow:")
            for items in portfolio.transaction:
                print("\t" + items)

# create a class for stock
class Stock:
    def __init__(self, price, symbol):
        # price can only be positive numbers
        if price > 0:
            self.price = round(price, 2)
            self.symbol = symbol
        else: print("Warning: The price of stock can only be a positive number. Please input a positive number.")

# create a class for mutual funds
class MutualFund:
    def __init__(self, symbol):
        self.symbol = symbol

# create a class for bonds
class Bonds:
    def __init__(self, price, symbol):
        # price can only be positive numbers
        if price > 0:
            self.price = round(price, 2)
            self.symbol = symbol
        else: print("Warning: The price of bonds can only be a positive number. Please input a positive number.")


# Testing the script
# Create a portfolio
portfolio1 = Portfolio()
# add cash
portfolio1.addCash(180)
# what if adding negative number? warning should occur and stop the transaction
portfolio1.addCash(-10)
# create different types of stock
s = Stock(20, "HFH")
y = Stock(5, "STL")
# buy stocks
portfolio1.buyStock(5, s)
portfolio1.buyStock(3, y)
# create different types of mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
# buy mutual funds
portfolio1.buyMutualFund(10.3, mf1)
portfolio1.buyMutualFund(20, mf2)
# sell stocks
portfolio1.sellStock(s, 1)
# what if the client over-sell its stocks? warning should occur and stop the transaction
portfolio1.sellStock(s, 5)
portfolio1.sellStock(y, 5)
# sell mutual funds
portfolio1.sellMutualFund(mf2, 5.1)
portfolio1.sellMutualFund(mf1, 5.1)
# withdraw cash
portfolio1.withdrawCash(10)
# view transaction history
portfolio1.history()
# view portfolio details
print(portfolio1)
