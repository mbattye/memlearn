# api calls for memlearn

import requests


class DifficultyAdjustment:
  def __init__(self):
    self.response = requests.get("https://mempool.space/api/v1/difficulty-adjustment")
    if self.response.status_code == 200:
      self.progress_percent = self.response.json()['progressPercent']
      self.difficulty_change = self.response.json()['difficultyChange']
      self.estimated_retarget_date = self.response.json()['estimatedRetargetDate']
      self.remaining_blocks = self.response.json()['remainingBlocks']
      self.remaining_time = self.response.json()['remainingTime']
      self.previous_retarget = self.response.json()['previousRetarget']
      self.next_retarget_height = self.response.json()['nextRetargetHeight']
      self.time_avg = self.response.json()['timeAvg']
      self.time_offset = self.response.json()['timeOffset']

class Fees: # choose from 24h, 3d, 1w, 1m, 3m, 6m, 1y, 2y, 3y
  def __init__(self, period):
    self.period = period
    assert isinstance(self.period, str)
    self.response = requests.get(f"https://mempool.space/api/v1/mining/blocks/rewards/{self.period}")
    if self.response.status_code == 200:
      self.all_fees = self.response.json()
    else:
      ValueError()
