######################################
    # CAUTION: THESE ARE ESTIMATES. Dont come after me if your experience does not match the results of this logic.
    # I've been building small solar projects for ten years, but Im not a solar install pro.
    # I have been calculating cost:benefit for smaller projects for a while though.
######################################
    # Calculate the payback period, total savings, estimated future monthly power bill,
    # and total cost of staying on the grid over a specified number of years.
    # It doesnt matter if it's just PV Panels, or a full hybrid kit. 
    # This just compares the cost of a setup to the projected cost (CAGR) of staying 100% on grid.
######################################
    # Parameters:
    # - cagr (float): Compound Annual Growth Rate (represents annual increase in grid electricity costs).
    # --- get your CAGR from calculate_gridCAGR.py
    # --- enter it below as a positive decimal.  I know it's negative from the script, but trust me. If you dont trust me, look up how CAGR works.
    # --- ex: if CAGR from calculate_gridCAGR.py is -6.1%, 
    # - initial_cost_solar_kit (float): Initial cost of the solar kit.
    # - monthly_power_bill (float): Average monthly power bill from the grid.
    # - num_years (int): Number of years for the calculation.
    # --- 20-25 years is a good estimate for the lifetime of a solar kit.
    # --- if your kit would include batteries with lifetimes shorter than your num_years, you need the cost of replacing them to initial_cost_solar_kit
    # ----- I'll add maintenance cost into the assessment one day soon, but today is not that day.
######################################
    # Returns:
    # - tuple (dont @ me gg): Payback period in months, total savings, estimated future monthly power bill,
    #          total cost of staying on the grid over the specified number of years.
######################################
    # Notes:
    # I'm moving this up into Lambda so I can put a frontend on this. Feel free to yoink that code from this repo.
    # --- lambda_calculate_PeriodPaybackAndCosts.py
######################################

def calculate_payback_period_and_costs(cagr, initial_cost_solar_kit, monthly_power_bill, num_years):

    # Estimate annual savings or earnings from solar kit
    annual_savings_earnings = cagr * initial_cost_solar_kit

    # Estimate monthly savings from solar kit
    monthly_savings = annual_savings_earnings / 12

    # Calculate payback period in months
    payback_period_months = initial_cost_solar_kit / monthly_savings

    # Calculate total savings over the specified number of years
    total_savings = sum(monthly_savings * 12 for _ in range(num_years))

    # Calculate total cost of staying on the grid over the specified number of years with compounded CAGR
    total_cost_on_grid = sum(monthly_power_bill * (1 + cagr) ** year * 12 for year in range(1, num_years + 1))

    # Calculate estimated future monthly power bill with weighted increase
    future_monthly_power_bill = monthly_power_bill * (1 + cagr) ** num_years

    return payback_period_months, total_savings, future_monthly_power_bill, total_cost_on_grid

# input values - change these to your parameters
cagr = 0.06  # Example CAGR (6% annual increase in grid electricity costs is pretty normal)
initial_cost_solar_kit = 23000.00  # Example initial cost of the solar kit in dollars
monthly_power_bill = 350.00  # Example average monthly power bill from the grid in dollars
num_years = 25  # Number of years for the calculation

# Calculate payback period, total savings, estimated future monthly power bill, and total cost of staying on the grid
payback_period_months, total_savings, future_monthly_power_bill, total_cost_on_grid = calculate_payback_period_and_costs(
    cagr, initial_cost_solar_kit, monthly_power_bill, num_years
)

# Output results
print(f"Payback Period in Months: {payback_period_months:.2f} months")
print(f"Total Savings Over {num_years} Years: ${total_savings:.2f}")
print(f"Estimated Future Monthly Power Bill: ${future_monthly_power_bill:.2f}")
print(f"Total Cost of Staying on the Grid Over {num_years} Years: ${total_cost_on_grid:.2f}")
