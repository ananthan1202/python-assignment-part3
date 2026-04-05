#Task 1 
#File read and write 
file_name ="python_notes.txt"
#Notes 
notes=[
    "Topic 1: Variables store data. Python is dynamically typed."
    "Topic 2: Lists are ordered and mutable."
    "Topic 3: Dictionaries store key-value pairs."
    "Topic 4: Loops automate repetitive tasks."
    "Topic 5: Exception handling prevents crashes."
]
#Write Mode Part A
with open(file_name,"w",encoding="utf-8") as file:
    for line in notes:
        file.write(line+"\n")

print("File written successfully") #(overwrite mode)

#Append mode 
#(adding own lines )
extra_lines= [
    "Topic 6:Functions help to reuse blocks of codes."
    "Topic 7:Classes bundle data and behaviour together into reusable blueprints called objects."
]
with open(file_name,"a",encoding="utf-8") as file:
    for line in extra_lines:
        file.write(line +"\n")

print("Lines appended.")

#Read Part B 
print("\nReading file:\n")
with open(file_name,"r",encoding="utf-8") as file:
    for i, line in enumerate(file,start=1):
        print(f"{i}. {line.strip()}") #Reading files and printing line by line with numbering 

#######################################################################################################################
#Task 2 Api Integration 
import requests
Base_URL= "https://dummyjson.com/products"
#Step 1 — Fetch and Display Products:
def fetch_products():
    url= f"{Base_URL}?limit=20" #gets 20 product frpm api
    try:                                   # snding GET request
        response = requests.get(url)
        data= response.json()
        products= data["products"]

        print("\nID | Title | Category | Price | Rating") # prints format table 
        print("-" * 60)
# Displaying product details 
        for p in products:
            print(f"{p['id']} | {p['title']} | {p['rating']}")
#fetch products from api
            return products
    except Exception as e:
        print("Error fetching products:",e)
        return[]

#Step 2 — Filter and Sort:
def filter_and_sort(products):
    print("\nFiltered Products (Rating >= 4.5):")
    filtered = [p for p in products if p["rating"] >= 4.5] #filter products with high rating
#sorting of price in descending order
    filtered.sort(key=lambda x: x["price"],reverse=True) #sorting by highest first
    for p in filtered:
        print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")

#Step 3 - Searching by category 
def search_laptop():
    url = f"{Base_URL}/category/laptops"
    try:
        response = requests.get(url)
        data = response.json()
        print("\nLaptop Products:") # fetches only laptops 
        for p in data["products"]:
            print(f"{p['title']} - $ {p['price']}") # prints name and price 
    except Exception as e:
        print("ERROR FETCHING LAPTOPS:",e)

#Step 4 - Post Request 
def create_products():
    url = f"{Base_URL}/add"

    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"} #sends new product data 
    
    try:
        response = requests.post(url,json=new_product)
        data= response.json()
        print("\nPost Responses:")
        print(data)
    except Exception as e:
        print("Error Creatin Product", e) #mock api

#Main
def main():
    products = fetch_products()
    filter_and_sort(products)
    search_laptop()
    create_products()

if __name__=="__main__":
    main()

###########################################################################################################################

#Task 3 — Exception Handling
#Part A Guarded Calculator 
def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return"Error: Invald input types"

#testing
print(safe_divide(10,2))
print(safe_divide(10,0))
print(safe_divide("ten",2))

#Part B Guarded File Reader:
def read_file_safe(filename):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File Operations Attempt Complete.")

#Testing
print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))

#Part C Safe API Calls
import requests
def fetch_products():
    try:
        response= requests.get("https://dummyjson.com/products?limit=5", timeout=5)
        print(response.json())
    except requests.exceptions.ConnectionError:
        print("Connection failed.Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:",e)
fetch_products()

#Part D Input Validation Loop:
import requests
while True:
    user_input= input("Enter product ID (1-100) or 'quit': ")
    if user_input.lower()=="quit":
        break
    if not user_input.isdigit():
        print("Invalid input. Enter a number.")
        continue
    product_id = int(user_input)
    if product_id < 1 or product_id > 100:
        print("ID must be between 1-100")
        continue
    try:
        response = requests.get(f"https://dummyjson.com/products/{product_id}")
        if response.status_code == 404:
            print("Product not found.")
        else:
            data = response.json()
            print("Title:", data["title"])
            print("Price", data["price"])
    except Exception as e:
        print("Error:", e)

#####################################################################################################################################

#TASK 4 - Logging to file 
#Step 1 Logger function 
from datetime import datetime
def log_error(message):
    with open("error_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now()
        file.write(f"[{timestamp}] {message}\n") # function to log error into a file with timestamp
#Step 2 Trigerring of errors 
#Connection error
import requests
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api")
except requests.exceptions.ConnectionError:
    log_error("Error in fetch_products ConnectionError - No connection could be made.")
#HTTP 404 Error 
response= requests.get("https://dummyjson.com/products/999")
if response.status_code !=200:
    log_error("Error in lookup_product HTTP Error -404 Not found for product ID 999")

#sTEP 3 PRINT LOG FILE 
with open("error_log.txt","r", encoding="utf-8") as file:
    print ("\n --- Error Log ---")
    print(file.read())

##################################################################################################################################

