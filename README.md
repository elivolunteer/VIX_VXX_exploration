# VIX VXX Exploration

## Purpose: 
Find and examine the correlation between the VIX, VXX, and VIX futures. Intro exploration for UTK's submission to the Southeastern Hedge Fund Competition (SEHFC)

## Background Research
VIX is a calcuated 30-day impled volatility in S&P 500 options. Therefore it is not something one can buy, instead derivatives on the VIX must be traded (i.e. options, futures).
The VXX is an ETF made up of VIX futures and it rolls its contracts on a daily basis.

#### VIX Futures Basics
Value of a VIX Futures contract is $100 times the index. There are mondthly and weekly contracts that usually fall on a wednesday before the following month;s standard Friday SPX option expired. They are settled in the am by a special caluclation of SPX options ([CBOE]).

#### VXX Basics
The ETF is run by Barclays and contains rolling long positions in first and second month VIX futures. The rollover creates an almost constant loss, so historically the VXX has a slip around 5%-10%. Investor fee is 0.89%. Calculation of spot price based on options price is outlined in prospectus ([Barclays]).

## Hypothesis
Due to constant rollover of futures, the VXX will fall (down 78% in last 5 years). This provides the oppurtunity to short the VXX. There would be a semi constant gain, though a relativly low gain. This would be mostly offset by the small chances of large swings in implied volatililty. During the COVID crash, the VXX hit a new high. 

To compensate for this risk VIX options can be bought to mitigate risk [**THIS NEEDS TO BE FLESHED OUT**]

Since the VXX has rolling VIX futures, there is some exploitable difference in the spot prices of the VXX, VIX futures and VIX options. This data analysis will explore the relationships between the three.

## VIX and VXX Exploration
-> VIX_VXX.ipynb




[CBOE]: https://www.cboe.com/tradable_products/vix/vix_options/specifications/
[Phillip_Capital]: https://www.phillipcapital.com/CFE-5-Things-Trader-Should-Know-About-VIX#:~:text=VIX%20Futures%20are%20AM%20settled%20contracts.&text=The%20SOQ%20is%20calculated%20using,disseminated%20using%20the%20ticker%20VRO. 
[MRA]:http://www.macroriskadvisors.com/layout/pdf/VIX_Primer_Part1.pdf
[Barclays]: https://ipathetn.barclays/ipath/details/341408/download-content/7718068