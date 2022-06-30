# memlearn: understanding the blockchain data through machine learning and visualisation

import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime as dt

from difficulty_adjustment import get_difficulty_adjustment
from fees import get_fees


# df = get_difficulty_adjustment(60,10)
period = '24h'
df = get_fees(period)
# print(df.to_string())

c = 100000000 # conversion to BTC
s = 625000000 # block subsidy

# print(f"Average Block Rewards: {(df.avgRewards.mean()-s)/c}")

# sns.lineplot(df.timestamp.map(lambda x: dt.fromtimestamp(x)), (df.avgRewards-s)/c)
# sns.lineplot(df.timestamp.map(lambda x: dt.fromtimestamp(x)), df.avgRewards/c)
# sns.color_palette("flare", as_cmap=True)
# sns.despine()
# plt.show()

sns.color_palette("flare", as_cmap=True)
sns.barplot(df.timestamp.map(lambda x: dt.fromtimestamp(x)), (df.avgRewards-s)/c)
plt.show()