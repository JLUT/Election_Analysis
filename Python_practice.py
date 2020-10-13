"""voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
  print(f"County {counties_dict['county']} has {counties_dict['registered_voters']} registered voters")"""

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
  for county, registered_voters in counties_dict:
    print(f"county{'county'} has {'registered_voters'} registered voters.")   