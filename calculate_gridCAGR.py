######################################
    # CAUTION: THESE ARE ESTIMATES. Dont come after me if your experience does not match the results of this logic.
    # I've been building small solar projects for ten years, but Im not a solar install pro.
    # I have been calculating cost:benefit for smaller projects for a while though.
######################################
    # Solar System vs Utility Cost Comparison

    # This Python script calculates the Compound Annual Growth Rate (CAGR) and estimates the future cost per kWh
    # to compare the cumulative cost of buying power from a utility company versus investing in a solar system.

    # Usage:
    # 1. Adjust the 'start_year_cost', 'end_year_cost', and 'investment_years' variables as needed.
    # 2. Run the script to obtain the CAGR and future cost per kWh.
######################################
    # Parameters:
    # - start_value (float): Initial value.
    # 
    # - end_value (float): Final value.
    # - num_years (int): Number of years.

    # Returns:
    # - float: CAGR.
######################################
    # Notes:
    # I'm moving this up into Lambda so I can put a frontend on it, but I havent converted this part yet. Probably should have done it first.
######################################

from decimal import *

# Function to calculate Compound Annual Growth Rate (CAGR)
def calculate_cagr(start_value, end_value, num_years):
    return (end_value / start_value) ** (1 / num_years) - 1

# Function to calculate future cost per kWh for intermediate years
def calculate_future_cost(start_value, cagr, num_years):
    """
    Calculate future cost per kWh for intermediate years.

    Parameters:
    - start_value (float): Initial cost per kWh.
    - cagr (float): Compound Annual Growth Rate.
    - num_years (int): Number of years.

    Returns:
    - float: Future cost per kWh.
    """
    return start_value * (1 + cagr) ** num_years

# Example input values
start_year = 1996
start_year_cost = 0.643  # Cost per kWh in the start year
end_year = 2020
end_year_cost = 0.12    # Cost per kWh in the end year
cagr_timespan = end_year - start_year
investment_years = 20   # Number of years for the comparison

# Calculate CAGR
cagr = calculate_cagr(start_year_cost, end_year_cost, investment_years)
converted_cagr = cagr *-100
print(converted_cagr)
projected_kWhCost_increase = Decimal(converted_cagr)
print(projected_kWhCost_increase)

# Calculate future cost per kWh for intermediate years
future_cost = calculate_future_cost(end_year_cost, cagr, investment_years)

# Output results
print(f"CAGR: {cagr:.1%}. Based on inputted cost/kWh trend over {cagr_timespan} years from {start_year}-{end_year}, \n cost per kWh will likely go up about {projected_kWhCost_increase:.2}% per year if the trend continues.")
print(f"Future cost per kWh in {investment_years} years: ${future_cost:.4f}")
