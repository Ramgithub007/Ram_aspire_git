#this is a comment.,this contains an integer
quantity = 30
#this variable contains a float
unit_price = 49.99
#this variable contains multiplication of quantity and price
extended_price = quantity*unit_price
#show the results
print(extended_price)

first_name = "ram" 
last_name = "krishna" 

print(first_name,last_name)


x = 10
if x == 0:
    print("x is zero")
else:
    print("x is",x)
print("all done")


print(f"Subtotal : ${quantity * unit_price:,.2f}")



sales_tax_rate = 0.065
print(f"Sales Tax Rate width {sales_tax_rate:>20,.2%}")
variable_for_f = f"using variable sales tac rate {sales_tax_rate:.2%} "
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
main_total = subtotal + sales_tax
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_main_total = "$" + f"{main_total:,.2f}"


output2 = f"""
Subtotal:  {s_subtotal:>10}
Salestax:  {s_sales_tax:>10}
maintotal: {s_main_total:>10}


"""

print(output2)






print(variable_for_f)


user1 = "ajab who he was the lucky charm at both times he wished"
user2 = "sasi who secretly wishes inside his heart"
user3 = "sathya who openly wishes and thinks success for me"
user4 = "arun all above"
output = f"""
 first name : &${user1:>21} 
 second name : &${user2:>29} 
 third name :  &{user3:>20} 
  fourth name : &${user4:>9}  """
print(output)




print(math.hex)
