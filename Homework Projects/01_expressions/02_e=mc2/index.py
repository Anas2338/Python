C: int = 299792458

def main():
    mass_in_kg = float(input("Enter kilos of mass: "))

    energy_in_joules = mass_in_kg * (C ** 2)

    print("e = m * C^2...")
    print(f"m = {mass_in_kg}")
    print(f"c = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")


main()
