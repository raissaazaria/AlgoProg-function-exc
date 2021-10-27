def num_atoms (grams,weight = 196.97):
    mol = weight/grams
    atomNumbers = 6.022*(10**23) / mol
    print(atomNumbers)

num_atoms(10)
num_atoms(10,12.001)
num_atoms(10,1.008)
