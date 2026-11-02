# homomorphic-finance

This is a mini project to show how sensitive data can be encrypted and potentially trained into machine learning frameworks without violating GDPR.

I am using a library named phe to use the built in paillier for the Partial Homomorphic Encryption. The library allowed me to efficiently make this project without having to write the algorithms or the number theory or integer maths to generate keys for encryption or decryption.

How it works:
- Key Generation: A 2048 bit key generation is run to encrypt each specific job role and it's value.
- Local Data Extract: A local script reads the inputs of the file 'salaries.txt'.
- Checks if the data in the salaries are within the Max and Min boundaries to prevent miscalculation.
- Encryption: Before any data leaves the network/file the script turns values into unique cyphertexts.
- Blind Calculation: Receves the ciphertexts and calculates the following using sum() using paillier which automatically adds the plaintext through ciphertext.
- Ones the results are made a private key is used to return and unlock the grand total and divides for the mean.

# Project File Structure:
homomorphic-finance/
|
|- Venv/                  -> Local python dependencies    
|- .gitignore             -> Stops Git from tracking files
|- main.py                -> Main Application
|- README.md              -> Project Documentation
|- requirements.txt       -> Enables the correct libraries import
|- salaries.txt           -> The Dataset file for salaries

# Installation / Setup:
Just follow the instructions below.

Step 1. Please ensure the intergrated terminal is open and showing the correct project path.

Step 2. Check if the files for venv is there. IF NOT then run the command 'python -m venv venv'

Step 3. Run the command '.\venv\Scripts\pip.exe install -r requirements.txt'

Step 4. If you don't have a txt file, create one called 'salaries.txt in the root folder and add your test data.
For example:
Software Engineer:85000.50
Product Manager:92000.00
Data Analyst:68500.25
IT Specialist:72000.00

Step 5. Launch the script. '.\venv\Scripts\python.exe main.py'