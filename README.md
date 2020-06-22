# Machine Learning for Investing

## Investing for everyone?

### Lower barrier of entry

For the last few years, the financial investment market has been more open. The entry barrier is lower as fresh, agile players entering the financial market and competing with traditional financial institutions by providing easy to use trading experience and above all, waiving all kinds of fee. Robinhood is one of the pioneers - it doesn't charge any trading fee and constantly enhances the user experience in their apps. Recently closed a round of $280M series F on May 04, 2020, Robinhood is valuated at $8.3B. Such competition forces traditional players, such as TD Ameritrade, to follow suits and waive fee for their users.

This has a huge impact of lowering the barrier for people who has spare money and wanted to invest. Not everyone has thousands or millions of dollars readily available for trading/investing. If you have just a few hundreds of dollars, it doesn't justify to open a trading account (this used to has a fee) and pay for transaction fee and commission (if you are using a brokerage account).

Also, some financial institutions, such as M1 Finance, starts to offer an option to purchase fractional share, which is a fraction equity of a full share. This makes some big stocks such as Amazon (2.460,60 per share at the time of writing) much more accessible, and thus, provides more opportunities to diversify one's porfolio.

### Why machine learning?

For an average, beginner trader, it takes time to build a sustainable trading strategy. It even take more time to achieve the knowledge enough to research different trading strategies and choose one that suits one's budget (how much money do you have?), investing horizon time (how long that you can keep the trading budget untouched until you need to spend it?), and risk apetite (how much you are willing to lose temporarily/permanently?).

In an ideal world, an algorithm would take the aforementioned paramenters (budget, timeline, and risk) to develop a trading algorithm with a reasonable and sustainable return. This calls for machine learning to search, build, and backtest a trading strategy that suitable for each trader's profile.

## Pipeline
//TODO

### Feature Engineer
//TODO

### Strategy Selection
//TODO

### Back Testing
//TODO

### Paper Trading

After back testing the strategy, the next step is to verify that the strategy is not overfitting. We would need to run the strategy against real-time market data to see how it performs. This is called "Paper Trade", which refers to the practice that aspiring traders used to practice on paper before risking their money in live trading.

There are many that offer paper trading feature and others who offer quantitative trading. Quantopian, for example, is a well-known platform that used to provide both services. Unfortunately, they shut down their paper trading feature in 2018, forcing their members to find an alternative. 

During my research for an alternative, I found [Alpaca] (https://alpaca.markets/), which is new yet getting more an more popularity among the quantitative trading professionals. Alpaca is a commission-free, algorithmic trading platform with a growing community. They have a free paper trading which allows testing your algoritm with real and live market data. Below is a screenshot when I am testing my long short algorithm in Alpaca's paper trading. 

# Resources
1. [Quantopian] (https://www.quantopian.com/contest/resources)
2. [Alpaca Trade APIs] (https://github.com/alpacahq/alpaca-trade-api-python)
