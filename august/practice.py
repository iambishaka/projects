print("===== BIOTECHNOLOGY DNA ANALYZER =====")

dna = input("Enter your DNA sequence: ").upper()

print("\nChoose an option:")
print("1. Count DNA bases")
print("2. Find DNA complement")
print("3. Calculate GC percentage")
print("4. Find gene sequence")
print("5. Check start codon")
print("6. Check stop codon")
print("7. DNA to RNA")

choice = int(input("\nEnter your choice: "))

if choice == 1:
    print("A =", dna.count("A"))
    print("T =", dna.count("T"))
    print("G =", dna.count("G"))
    print("C =", dna.count("C"))

elif choice == 2:
    complement = ""

    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    print("Complement:", complement)

elif choice == 3:
    gc = dna.count("G") + dna.count("C")
    percentage = (gc / len(dna)) * 100
    print("GC Percentage:", percentage, "%")

elif choice == 4:
    gene = input("Enter gene sequence: ").upper()

    if gene in dna:
        print("Gene found!")
    else:
        print("Gene not found!")

elif choice == 5:
    if "ATG" in dna:
        print("Start codon ATG found!")
    else:
        print("Start codon not found.")

elif choice == 6:
    if "TAA" in dna or "TAG" in dna or "TGA" in dna:
        print("Stop codon found!")
    else:
        print("Stop codon not found.")

elif choice == 7:
    rna = dna.replace("T", "U")
    print("RNA:", rna)

else:
    print("Invalid choice.")
