""" This script checks traceability between subsystem requirements and mission objectives. """

requirements = { "ADCS": ["Stabilization", "Pointing Accuracy"], "EPS": ["Battery", "Power Output"], "OBC": ["Interfaces", "Processor"], "Comm": ["Frequency Band", "Data Rate"], "Payload": ["Function", "Interface"] }

objectives = [ "Design a CubeSat for relaying signals", "Develop subsystem requirements", "Perform trade-off studies" ]

for subsystem, reqs in requirements.items():
    print(f"\nSubsystem: {subsystem}")
    for req in reqs:
        print(f" - Requirement: {req} -> Traceable")