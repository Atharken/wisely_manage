import csv
from pathlib import Path
import phonenumbers
from phonenumbers import PhoneNumberFormat
from datetime import date, timedelta


regions = {
    "1": ("IN", "India"),
    "2": ("US", "United States"),
    "3": ("GB", "United Kingdom"),
    "4": ("CA", "Canada"),
    "5": ("AU", "Australia"),
    "6": ("AE", "United Arab Emirates"),
    "7": ("SA", "Saudi Arabia"),
    "8": ("SG", "Singapore"),
    "9": ("DE", "Germany"),
    "10": ("FR", "France"),
    "11": ("JP", "Japan"),
    "12": ("CN", "China"),
    "13": ("PK", "Pakistan"),
    "14": ("BD", "Bangladesh"),
    "15": ("NP", "Nepal")
}

def search(x):
    new_l = []
    with open("acc_data.csv","r",newline="") as f:
        r = csv.DictReader(f)
        l1 = list(r)

        for i in l1:
            if x.strip().lower() == i['account'].strip().lower():
              new_l.append(i)


    return new_l


def remove():

        with open("acc_data.csv","r",newline="") as f:
          r = csv.DictReader(f)
          l1 = list(r)

        return l1
                
             







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


    main = input("1.add rent account\n2.search by account\n3.remove account\n4.edit account\n5.exit\n:")


    if main == "1":

        


        typ = "" #____________type

        l = {"1" : "ultimate xbox gamepass","2" : "premium xbox gamepass","3" : "rockstar account"}

        account = input("enter your account\n:")  #_____________account

        

        typee = input("enter account type\n1.ultimate xbox gamepass\n2.premium xbox gamepass\n3.rock star account\n4.others\n:")
        
        for i in l:
           if typee in i:

               typ = l[i]
         
        if typee == "4":
            typ = input("enter other account type\n:")

        print(regions)
        region = input("enter number format\n:")
        
        raw_number = input("enter phone number\n:")

        num = inrternational_number(raw_number, region.upper())   #_____________number

        print(num)

        current_date = date.today()    #________________start

        print(current_date)
        try:

            end = int(input("enter rent time period\n: "))
        except ValueError:
            print("enter numeric value only !!!")
            continue

        end_date = current_date + timedelta(days=end)        #____________end

        data = {"account" : account,"type" : typ,"number" : num,"date" : current_date,"end_date" : end_date}
        with open("acc_data.csv","a",newline="") as f:
            w = csv.DictWriter(f,fieldnames=headers)
            w.writerow(data)

    elif main == "2":

        print("===search by account===")
        x = input("enter your account\n:")

        y = search(x)

        print(y)

    elif main == "3":

        l = []

        option = input("1.by search\n2.by all index")

        if option == "1":

            x = input("enter your account\n:")

            y = remove()

            for index, value in enumerate(y):
                l.append(value)
                if value['account'] == x:
                    print(f"{index}  {value}")
            try:
                rem = int(input("enter index to remove\n:"))
            except ValueError:
                print("wrong input enter numeric value")
                continue
            l.pop(rem)     

            with open("acc_data.csv","w",newline="") as f:
                        w = csv.DictWriter(f,fieldnames=headers)
                        w.writeheader()
                        w.writerows(l)
        elif option == "2":

            y = remove()

            l = []

            for index,value in enumerate(y):
                print(f"index - {index} {value}")
                l.append(value)

            try:
                rem = int(input("enter index to remove\n:"))
            except ValueError:
                print("wrong input enter numeric value")
                continue
            l.pop(rem)     

            with open("acc_data.csv","w",newline="") as f:
                        w = csv.DictWriter(f,fieldnames=headers)
                        w.writeheader()
                        w.writerows(l)


    elif main == "5":
        break
            

    
        #edit and remove next time also polish this code too