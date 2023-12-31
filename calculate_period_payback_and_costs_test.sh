curl -X POST -H "Content-Type: application/json" -d '{
    "cagr": 0.06,
    "initial_cost_solar_kit": 25000.0,
    "monthly_power_bill": 350.0,
    "num_years": 25
  }' https://de1zp3s6ti.execute-api.us-east-1.amazonaws.com/calculate_payback
 
  


# To calculate your CAGR, run calculate_gridCAGR.py with your parameters.

# The above curl works in the current stage against the API gateway and Lambda.
# Feel free to test it out. The API gateway is rate limited pretty low (1 hit/sec).
# If you get back a 429 Too Many Requests, wait a bit and try again.