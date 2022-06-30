from api_calls import DifficultyAdjustment
import pandas as pd
import time


def get_difficulty_adjustment(s,n):

  # set up dataframe for difficulty adjument data
  cols = ('progress_percent', 'difficulty_change', 'estimated_retarget_date', 'remaining_blocks', 'remaining_time', 'previous_retarget', 'next_retarget_height', 'time_avg', 'time_offset')
  
  df = pd.DataFrame(columns=cols)
  i = 0
  
  while i < n: # loop through number of iterations
    da = DifficultyAdjustment()
    df.loc[len(df.index)] = [da.progress_percent, da.difficulty_change, da.estimated_retarget_date, da.remaining_blocks, da.remaining_time, da.previous_retarget, da.next_retarget_height, da.time_avg,da.time_offset]
    i+=1
    time.sleep(s) # wait for s seconds

  return df
  