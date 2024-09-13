# This is a basic prototype of the diagnostic app
# To extend this, consider integrating a more sophisticated user interface, a database, and external APIs.

# Sample data: Diagnostics database
diagnostics = {
    "washing_machine": {
        "whirlpool": {
            "model_123": {
                "no_power": {
                    "steps": [
                        "Check if the appliance is plugged in.",
                        "Ensure the power outlet is working.",
                        "Check the circuit breaker.",
                        "Inspect the power cord for damage."
                    ],
                    "parts": ["Power cord", "Circuit breaker"],
                    "recommendation": "If the issue persists, consider contacting a professional electrician."
                },
                "leaking_water": {
                    "steps": [
                        "Inspect the water inlet hoses for cracks or leaks.",
                        "Check the door seal for any damage.",
                        "Ensure the drain hose is securely attached and not clogged."
                    ],
                    "parts": ["Water inlet hose", "Door seal", "Drain hose"],
                    "recommendation": "If leaks continue, contact a professional technician."
                }
            }
        }
    },
    # Add more appliances, makes, and models as needed.
}

def get_diagnostic(appliance_type, make, model, issue):
    """
    Function to get diagnostics based on the appliance type, make, model, and issue.
    """
    try:
        diagnostic = diagnostics[appliance_type][make][model][issue]
        print(f"Step-by-step guidance to fix '{issue}' on {make} {model}:")
        for i, step in enumerate(diagnostic["steps"], start=1):
            print(f"{i}. {step}")

        print("\nParts you may need:")
        print(", ".join(diagnostic["parts"]))

        print(f"\nRecommendation: {diagnostic['recommendation']}")

    except KeyError:
        print("Unable to determine the cause. Please reach out to a professional.")

def main():
    print("Welcome to the Home Project Diagnostic App")

    # Input from user
    appliance_type = input("Enter the type of appliance (e.g., washing_machine): ").lower()
    make = input("Enter the make of the appliance (e.g., whirlpool): ").lower()
    model = input("Enter the model of the appliance (e.g., model_123): ").lower()
    issue = input("Describe the issue (e.g., no_power, leaking_water): ").lower()

    # Get diagnostic recommendation
    get_diagnostic(appliance_type, make, model, issue)

if __name__ == "__main__":
    main()
