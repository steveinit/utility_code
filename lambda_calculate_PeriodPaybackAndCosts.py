##########################################
# This is calculate_solarPayback.py, but in Lambda.
# Im working on a frontend for this to be user friendly.
# For now, you can alter the parameters in calculate_solarPayback.py to
# do the same calculations in python.
##########################################



import json

def calculate_payback_period_and_costs(cagr, initial_cost_solar_kit, monthly_power_bill, num_years):
    # Your calculation logic here
    annual_savings_earnings = cagr * initial_cost_solar_kit
    monthly_savings = annual_savings_earnings / 12
    payback_period_months = initial_cost_solar_kit / monthly_savings
    total_savings = sum(monthly_savings * 12 for _ in range(num_years))
    future_monthly_power_bill = monthly_power_bill * (1 + cagr) ** num_years
    total_cost_on_grid = sum(monthly_power_bill * (1 + cagr) ** year * 12 for year in range(1, num_years + 1))

    return {
        "payback_period_months": payback_period_months,
        "total_savings": total_savings,
        "future_monthly_power_bill": future_monthly_power_bill,
        "total_cost_on_grid": total_cost_on_grid,
        "num_years": num_years,
    }

def lambda_handler(event, context):
    try:
        # Parse input from the event
        input_data = json.loads(event["body"])

        # Call the calculation function
        result = calculate_payback_period_and_costs(
            input_data["cagr"],
            input_data["initial_cost_solar_kit"],
            input_data["monthly_power_bill"],
            input_data["num_years"],
        )

        # Return the result
        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # Adjust this based on your frontend's domain
            },
        }
    except Exception as e:
        # Handle errors gracefully
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # Adjust this based on your frontend's domain
            },
        }
