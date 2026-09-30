import csv
from pathlib import Path
import phonenumbers
from phonenumbers import PhoneNumberFormat

def inrternational_number(raw_number, region="IN"):
    # Parse the raw number string with a default region (e.g., 'IN' for India)
    parsed_number = phonenumbers.parse(raw_number, region)
    
    # Check if the number is valid
    if not phonenumbers.is_valid_number(parsed_number):
        raise ValueError("Invalid phone number")
    
    # Format into E.164 international standard (+14155552671)
    e164_format = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
    
    # You can now save `e164_format` to your database or file
    return e164_format

# Example usage:
# Input can be a local format or full international string
# Output: +919812343242




p = Path('acc_data.csv')

headers = ["account","type","number","date","end_date"]

if not p.exists():
    with open("acc_data.csv","w",newline="") as f:
        w = csv.DictWriter(f,fieldnames=headers)
        w.writeheader()



while True:


    main = input("1.add rent account\n2.search by account\n3.remove account\n4.edit account\n:")


    if main == "1":

        typ = ""

        l = {"1" : "ultimate xbox gamepass","2" : "premium xbox gamepass","3" : "rockstar account"}

        account = input("enter your account\n:")

        typee = input("enter account type\n1.ultimate xbox gamepass\n2.premium xbox gamepass\n3.rock star account\n4.others\n:")

        for i in l:
           if typee in i:

               typ = l[i]
         
        if typee == "4":
            typ = input("enter other account type\n:")


        region = input("enter number format\n:")
        raw_number = input("enter phone number\n:")

        num = inrternational_number(raw_number, region)

        print(num)

        


          1
        