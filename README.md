# Modified-Butterfly-Spread-Finder

In security trading, **options** are a form of financial derivatives that is the agreement between two parties to buy or sell an underlying security at a specific price (**strike price**) by a predetermined date.

Although options can be used to hedge, they are inherently risky by themselves, as they involve higher risk and profit compared to just trading the underlying security. However, when multiple of them are combined into a **spread**, they become a versatile tool that can be adapted in a variety of situations and trading strategies.

One popular strategy, the **Butterfly Spread**, is constructed with a bull and bear spread and is charactized by fixed risk and profits. It is a common tool used to trade volatility, as they capture a profit when the underlying security moves either above or below the spread.

However, if you wanted to trade volatility, but were bullish on a security, the butterfly spread wont be as efficient as you do not expect the security to move below the bottom wing.

In comes the

Python application used for finding Modified Butterfly Spreads that meet certain requirements, such as underlying security, probability of profit, and near profit/loss
    \begin{itemize}
        \item Utilized Questrade's REST API along with various HTTPS methods to request live market data, and interpret the JSON responses
        \item Used OAuth 2.0 along with manual access tokens to increase security
        \item Practiced efficient algorithm design when sending requests and filtering through spreads

This application uses live market data to find Modified Butterfly Spreads that fit within the following requirements:
* underlying security
* type of spread
* days til expiry (**DTE**)
* probability of profit (**PoP**)
* downside protection
* (profit / loss) / maximum risk (**PLMR**)

It does this through Questrade's REST API and Requests library for Python. 

how it works

Future plans
* implement a Monte Carlo simulation on filtered spreads to more accurately calculate PoP
* utilize MatPlotLib to construct a risk curves to visually represent each spread
* create a method that prints out a strategy plan for a specific spread
* use PyQt5 to create a GUI
* utilize the account and position portion of the API to 
* actively look at the price of the security and send a notification when it moves towards the downside
