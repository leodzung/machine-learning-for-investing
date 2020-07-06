class FactorUniverseSelectionModel():
    
    def __init__(self, algorithm):
        self.algorithm = algorithm
    
    def SelectCoarse(self, coarse):
        """
        Return a list of CoarseFundamental objects. 
        The most important properties of this object are: Price, DollarVolume and HasFundamentalData
        """
        self.algorithm.Log("Generating universe...")
        universe = self.FilterDollarPriceVolume(coarse)
        return [c.Symbol for c in universe]

    def SelectFine(self, fine):
        universe = self.FilterFactor(self.FilterFinancials(fine))
        # self.algorithm.Log(f"Universe consists of {len(universe)} securities")
        self.algorithm.securities = universe
        return [f.Symbol for f in universe]
    
    def FilterDollarPriceVolume(self, coarse):
        """
        Select top 1000 stocks that have:
        - Price > $1
        - Has Fundamental Data
        """
        filter_dollar_price = [c for c in coarse if c.Price > 1]
        sorted_dollar_volume = sorted([c for c in filter_dollar_price if c.HasFundamentalData], key=lambda c: c.DollarVolume, reverse=True)
        return sorted_dollar_volume[:1000]

    def FilterFinancials(self, fine):
        """ Filter out Financial Services industry """
        filter_financials = [f for f in fine if f.AssetClassification.MorningstarSectorCode != MorningstarSectorCode.FinancialServices]
        return filter_financials
    
    def FilterFactor(self, fine):
        """
        Sort the stocks by Cash Return (Free Cash Flow / Enterprise Value)
        Get the top 50 to long
        Get the bottom 50 to short
        """
        filter_factor = sorted(fine, key=lambda f: f.ValuationRatios.CashReturn, reverse=True)
        return filter_factor[:50] + filter_factor[-50:]