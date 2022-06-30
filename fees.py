from api_calls import Fees
import pandas as pd

def get_fees(period):

  # set up dataframe for fee data
  cols = ("avgHeight", "timestamp", "avgRewards")
  df = pd.DataFrame(columns=cols)
  f = Fees(period)
  df = pd.DataFrame.from_dict(f.all_fees, orient='columns')
  return df
