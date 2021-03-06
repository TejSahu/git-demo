"""Split example
string = "Hello, welcome to my world"
print(string.split(" "))"""

# Shopping receipts program
p1_item, p1_price = "Balls", 4.95
p2_item, p2_price = "Pens", 2.50
p3_item, p3_price = "Monitor", 450.00

# create a company name and address
company_name = "Coding Temple Inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# end message
message = "Thank you for shopping with us today"

print('*' * 50)
print("\t\t{}".format(company_name))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

print('=' * 50)

print("\tProduct Name\tProduct Price")
print("\t{}\t\t ${}".format(p1_item, p1_price))
print("\t{}\t\t ${}".format(p2_item, p2_price))
print("\t{}\t\t ${}".format(p3_item, p3_price))

print('=' * 50)
total = p1_price + p2_price + p3_price
print("\t\t   Total ${}".format(total))

# Output thank you message
print("\n\t{} \n".format(message))

print('*' * 50)