import os
from phe import paillier

def salary_analytics():
    print("Hommorphic Salary Analysis")

    #System setup for key creation 
    print("2048-bit keys initialising...")
    public_key, private_key = paillier.generate_paillier_keypair()
    print("Keys Generated")
    
    #Taking data and encrypting it
    encrypted_salaries = {}
    data_file = "salaries.txt"
    
    if not os.path.exist:
        print(f"The file is not found...")
        return
    
    print("Reading the encrypted text file... from"'{data_file}'"Double checking if it's available...")
    
    with open(date_file, "r") as file:
        for line in file:
            #This is to clean things for more readablitiy.
            line = line.strip()
            if not line or ":" not in line:
                continue
            
            #This is the spliting
            role, amount_str = line.split(":",1)
            amount = float(amount_str)

            #This is to put the amount to encryption before the outside can touch any value.            
            encrypted_salaries[role] = public_key.encrypt(amount)
            
            
        


    
    