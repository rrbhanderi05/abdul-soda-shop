# The list of all items
varieties = ['vimto', 'cola', 'jeera', 'orange', 'masala', 'mango', 'beer']
available_items = ['vimto', 'cola', 'jeera', 'orange', 'masala', 'mango', 'beer']
#orders
orders = {'henis' : 'vimto', 
          'jaymin' : 'vimto',
          'shubham' : 'cola', 
          'darshak' : 'shing - cola', 
          'devendra' : 'masala', 
          'smit' : 'chash - soda', 
          'vyom' : 'beer', 
          'abhi' : 'orange', 
          'ishant' : 'jeera', 
          'jenil' : 'jeera'}
# checking if any item is out of the stock and greeting
print("Welcome To Abdul Soda Shop !")
is_empty = input("\nIs any soda is out of stock (y/n) ?")
# list that shows items which are not available
empty_stock = []
# if any item is out of stock removing it
out_of_stock = True
if is_empty == 'y' :
    print("All Varieties Are : \n")
    for varity in varieties :
        print(f"{varity.title()}")
    while out_of_stock :
        not_available = input("\nWhich of The List Is Not Available (Enter d to done.): ")
        if not_available == 'd' :
            out_of_stock = False
        else :
            try :
                index_not_available_item = available_items.count(not_available)
                removed = available_items.pop(index_not_available_item)
                empty_stock.append(removed)
                print(f"{not_available.title()} removed successfully.")
            except ValueError :
                print(f"\nInvalid Input '{not_available}', maybe it's not available. Please Try Again !")
                continue

# if everything is available
for customer, order in orders.items() :
    if order not in varieties and empty_stock :
            print(f"\nSorry {customer.title()}, We Don't Sell {order.title()}.")
    elif order in empty_stock :
            print(f"\nSORRY {customer.upper()}, WE ARE RUNNING OUT OF THE STOCK {order.title()} CURRENTLY. PLEASE BUY SOMETHING ELSE !")
    else :
            print(f"\nHere's Your {order.title()} {customer.title()}.")

