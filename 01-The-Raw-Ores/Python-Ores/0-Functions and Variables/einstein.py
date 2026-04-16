SPEED_OF_LIGHT = 300000000;

def main():
    m = int(input("Enter the mass in(kg) value to calculate energy: "));
    e = energyFormula(m);
    print("The energy is:", e, "Joules");


def energyFormula(mass):
    return mass * SPEED_OF_LIGHT;
    

main()