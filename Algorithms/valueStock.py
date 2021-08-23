class ValueStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 8, 22)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.AddEquity("SPY", Resolution.Daily)
        
        self.AddUniverseSelection(FineFundamentalUniverseSelectionModel(self.SelectCoarse, self.SelectFine))
        self.NUM_STOCK = 10
        # We buy and hold the top 10 stocks at the begining of the current month and HOLD forever
        # Can update strategy to rebalance monthly or annually 
        self.Schedule.On(self.DateRules.MonthStart("SPY"), self.TimeRules.AfterMarketOpen("SPY"), self.Rebalance)
        self.invested = False
        
    def Rebalance(self):
        pass
        
    def SelectCoarse(self, coarse):
        # Filter out stocks with price less than $1
        filter_price = [c for c in coarse if c.Price > 1]
        # sorted_dollar_volume = sorted([c for c in filter_price if c.HasFundamentalData], key=lambda c:c.Volume, reverse=True)
        
        return [c.Symbol for c in filter_price]
        
    def SelectFine(self, fine):
        # Filter stocks with fundamentals of interest
        filtered_fine = [f for f in fine if f.OperationRatios.GrossMargin.OneMonth
                                            and f.OperationRatios.NormalizedNetProfitMargin.OneMonth
                                            and f.OperationRatios.NormalizedROIC.ThreeMonths]
        
        
        
        sortedByfactor1 = sorted(filtered_fine, key=lambda x: x.OperationRatios.GrossMargin.OneMonth, reverse=True)
        sortedByfactor2 = sorted(filtered_fine, key=lambda x: x.OperationRatios.NormalizedNetProfitMargin.OneMonth, reverse=True)
        sortedByfactor3 = sorted(filtered_fine, key=lambda x: x.OperationRatios.NormalizedROIC.ThreeMonths, reverse=True)
    
        stock_dict = {}
        
        num_stocks = len(filtered_fine)
        # Smoke check if there are enough stocks that meet the fitler criteria
        self.Debug(f"{num_stocks}")
        
        for i, ele in enumerate(sortedByfactor1):
            rank1 = i
            rank2 = sortedByfactor2.index(ele)
            rank3 = sortedByfactor3.index(ele)
            # Calculate the score. The lower the better.
            score = [rank1/num_stocks,
                     rank2/num_stocks,
                     rank3/num_stocks]
            score = sum(score)
            stock_dict[ele] = score
        
        # Sort stocks by score and get the top 10
        self.sorted_stock = sorted(stock_dict.items(), key=lambda x:x[1])[:10]
        # for i in range(len(self.sorted_stock)):
        #     x = self.sorted_stock[i][0]
        #     self.Debug(f"{x.Symbol}: PE: {x.ValuationRatios.NormalizedPERatio:.2f} \
        #             PB: {x.ValuationRatios.PBRatio:.2f} \
        #             FCF: {x.ValuationRatios.FCFYield:.2f} \
        #             Score: {self.sorted_stock[i][1]:.2f}")
            
        return [s[0].Symbol for s in self.sorted_stock]

    def OnData(self, data):
        if self.invested:
            return
        
        weight = 1.0 / self.NUM_STOCK
        for stock in self.sorted_stock:
            self.SetHoldings(stock[0].Symbol, weight)
            
        self.invested = True
