def calculate_discount(price, discount_percentage):
    if discount_percent >= 20:
       discount_amount = price * (discount_percent/100)
       final_price = price - discount_amount 
       return final_price
    else:
        return price
    
    #prompting the user for input
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage:"))

     # Validate if the discount_percentage is between 0 and 100
     if 0 <=discount_percentage <=100:
        result = calculate_discount (original_price, discount_percentage)   
        print(f"The final price after applying the discount is:${result:.2f}")
     else:
        print("Please enter a valid discount percentage between 0 and 100.")
     except ValueError:
        print("Invalid input.Please enter numeric values for the price and the discount percentage.")