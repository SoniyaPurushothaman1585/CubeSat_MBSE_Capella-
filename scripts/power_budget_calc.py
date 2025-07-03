""" Estimate CubeSat average power consumption. """

subsystems = { "ADCS": 0.5, "EPS": 0.2, "OBC": 1.0, "Comm": 2.0, "Payload": 1.5 }

total_power = sum(subsystems.values())
print(f"Total Average Power Consumption: {total_power:.2f} W")