""" Estimate CubeSat total mass based on subsystem weights. """

masses = { "Structure": 0.4, "ADCS": 0.15, "EPS": 0.3, "OBC": 0.1, "Comm": 0.25, "Payload": 0.2 }

total_mass = sum(masses.values())
print(f"Total CubeSat Mass: {total_mass:.2f} kg")