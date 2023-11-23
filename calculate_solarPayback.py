def calculate_payback_period_and_costs(cagr, initial_cost_solar_kit, monthly_power_bill, num_years):
    """
    Calculate the payback period, total savings, estimated future monthly power bill,
    and total cost of staying on the grid over a specified number of years.
    Try to be as accurate as possible pricing a solar kit that will completely offset your bill when averaged.

    Parameters:
    - cagr (float): Compound Annual Growth Rate (represents annual increase in grid electricity costs).
    - initial_cost_solar_kit (float): Initial cost of the solar kit.
    - monthly_power_bill (float): Average monthly power bill from the grid.
    - num_years (int): Number of years for the calculation.

    Returns:
    - tuple: Payback period in months, total savings, estimated future monthly power bill,
             total cost of staying on the grid over the specified number of years.
    """
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

# Example input values
cagr = 0.06  # Example CAGR (6% annual increase in grid electricity costs)
initial_cost_solar_kit = 23000.0  # Example initial cost of the solar kit in dollars
monthly_power_bill = 350.0  # Example average monthly power bill from the grid in dollars
num_years = 25  # Number of years for the calculation, 20-25 is a good estimate for the lifetime of a solar kit.

# Calculate payback period, total savings, estimated future monthly power bill, and total cost of staying on the grid
payback_period_months, total_savings, future_monthly_power_bill, total_cost_on_grid = calculate_payback_period_and_costs(
    cagr, initial_cost_solar_kit, monthly_power_bill, num_years
)

# Output results
print(f"Payback Period in Months: {payback_period_months:.2f} months")
print(f"Total Savings Over {num_years} Years: ${total_savings:.2f}")
print(f"Estimated Future Monthly Power Bill: ${future_monthly_power_bill:.2f}")
print(f"Total Cost of Staying on the Grid Over {num_years} Years: ${total_cost_on_grid:.2f}")
