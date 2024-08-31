def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if applicable."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate and print the final price
    final_price = calculate_discount(original_price, discount_percent)
    print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")