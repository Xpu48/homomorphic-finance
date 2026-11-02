import os
from phe import paillier

def salary_analytics():
    print("Hommorphic Salary Analysis")

    #System setup for key creation 
    print("2048-bit keys initialising...")
    public_key, private_key = paillier.generate_paillier_keypair()
    print("Keys Generated")
    
    #The range for salary boundary
    MIN_SALARY = 15000.00
    MAX_SALARY = 250000.00
    
    #Taking data and encrypting it within dictionary
    encrypted_salaries = {}
    data_file = "salaries.txt"
    
    if not os.path.exists(data_file):
        print(f"The file is not found...")
        return
    
    print("Reading the encrypted text file... from"'{data_file}'"Double checking if it's available...")
    
    with open(data_file, "r") as file:
        for line in file:
            #This is to clean things for more readablitiy.
            line = line.strip()
            if not line or ":" not in line:
                continue
            
            #This is the spliting, looking for the first : only
            role, amount_str = line.split(":",1)
            amount = float(amount_str)
            
            #Checks to see if it's within bounds to prevent any misuse of data resulting in the wrong calculation.
            if amount < MIN_SALARY or amount > MAX_SALARY:
                print(f"=========== Warning: Salary of {role} ===========")
                print(f"Salary for {role} is out of bounds.")
                print(f"Amount: {amount} is not within the range of {MIN_SALARY} to {MAX_SALARY}.")
                print("Skipping this entry...")
                continue
            
            #This is to put the amount to encryption before the outside can touch any value.            
            encrypted_salaries[role] = public_key.encrypt(amount)
            
            #This is to print the encrypted salary for each role
            cyphertext = encrypted_salaries[role]
            print(f"Encrypted salary for {role}: {cyphertext.ciphertext()}")
    
    print("==========================================================")
    print("All salaries are encrypted and stored in the dictionary.")
    
    encrypted_sum = sum(encrypted_salaries.values())
    print(f"Encrypted sum of all salaries: {encrypted_sum.ciphertext()}")
    
    #Unlocks the final total salary and average salary for the employees
    final_summary = private_key.decrypt(encrypted_sum)
    total_employees = len(encrypted_salaries)
    average_salary = final_summary / total_employees
    
    print("=========== Final Summary ===========")
    print(f"Total Employees: {total_employees}")
    print(f"Total Salary: {final_summary}")
    print(f"Average Salary: {average_salary}")
    print(f"List of Jobs: {list(encrypted_salaries.keys())}")
    print("=====================================")
    
if __name__ == "__main__":
    salary_analytics()
            
    
        


    
    