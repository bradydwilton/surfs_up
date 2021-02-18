# Surf's Up Weather Analysis

### Overview
This analysis was performed over one year of weather data for the Hawaiian island of Oahu. The data was provided in a SQLite file, which was read by a python script to determine if the weather on the island is suitable for opening a Surf and Ice Cream shop.

### Results
_Bulleted list that addresses three key differences between June and December weather_
For the analysis, the temperatures of June and December were compared (results shown below).

<img src='june pic'><img src='dec pic'>

The analysis of temperature data between June and December indicate that the island's temperatures are consistent enough to support the Surf & Ice Cream show. Specific evidence supporting the claim is as follows:
  1. The average temperatures are not too different (75F in June, 71F in December)
  2. The maximum temperatures for both months are similar (85F in June, 83F in December)
  3. The low temperatures are farther apart than the high and average temps (8F difference from June to December)  

These three points are futher demonstrated by the higher standard deviation of December temperatures (3.75F) versus June (3.25F), indicating that there is a higher level of variation in the winter weather. This is what would be expected based on the three points above, as the high and average temperatures are similar, but the lows of December are further away than the rest of the data.

### Summary

The results of the temperature analysis indicate that this is a prime location for the Surf & Ice Cream shop. However, further investigation into the amount of precipitation is warranted before a final decision is made. To perform this analysis, two additional queries could be performed, one for June and one for December, to show the summary statistics for the amount of precipitation received in each month. The results of those two queries are shown below:

<img src='precipJune'><img src='precipDec'>
