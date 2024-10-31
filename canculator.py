def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt user for original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numbers for both the price and discount percentage.")
