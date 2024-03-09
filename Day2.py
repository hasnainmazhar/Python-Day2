# 16. Operator Challenge - III
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
quotient = numerator // denominator
remainder = numerator % denominator
print(f"Quotient: {quotient}, Remainder: {remainder}")

# 17. Escape Sequences and Print Formatting
print("This line includes a backslash (\\) followed by a quote (\").")

# 18. Type Casting and Comments
user_height_cm = float(input("Enter your height in centimeters: "))
user_height_meters = user_height_cm / 100
print(f"Height in meters: {user_height_meters}")
# Comment: Converting user's height from centimeters to meters.

# 19. Operators and Conditional Print
number_to_check = int(input("Enter a number: "))
if number_to_check % 2 == 0:
    print("Even")
else:
    print("Odd")

# 20. Print Formatting and Comments
print('This message includes both single (\') and double (") quotes.')
# Comment: To include quotes in a string, use different types of quotes or escape them with a backslash.

# 21. Operator Challenge - IV
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14 * (radius ** 2)
print(f"Area of the circle: {area_circle}")

# 22. Escape Sequences and Print Formatting
print("123 Main Street,\nCity,\tCountry.")
# Comment: Proper line breaks and tabs enhance the readability of address formatting.

# 23. Type Casting and Operator Challenge
input_number_challenge_2 = float(input("Enter a number: "))
result_challenge_2 = int(input_number_challenge_2) ** 2
print("Result after type casting and squaring:", result_challenge_2)

# 24. Operators and Print Formatting
item_price_1 = 10.99
item_quantity_1 = 2
item_price_2 = 5.49
item_quantity_2 = 3
total_cost = item_price_1 * item_quantity_1 + item_price_2 * item_quantity_2
print(f"Total cost of items: {total_cost}")

# 25. Conditional Statements and Comments
person_age = int(input("Enter your age: "))
if 13 <= person_age <= 19:
    print("Teenager")
# Comment: Checking if the person's age falls within the teenage range.

# 26. Escape Sequences and Print Formatting
print("This message includes a new line (\n) and a backspace character (\b).")
# Comment: New line and backspace characters serve different formatting purposes.

# 27. Operator Challenge - V
num1_challenge_3 = float(input("Enter the first number: "))
num2_challenge_3 = float(input("Enter the second number: "))
num1_challenge_3, num2_challenge_3 = num2_challenge_3, num1_challenge_3
print(f"After swapping: Number 1 = {num1_challenge_3}, Number 2 = {num2_challenge_3}")

# 28. Type Casting and Print Formatting
input_float_challenge = float(input("Enter a floating-point number: "))
converted_int_challenge = int(input_float_challenge)
print(f"The integer value of {input_float_challenge} is {converted_int_challenge}.")

# 29. Conditional Statements and Comments
given_number = float(input("Enter a number: "))
if given_number > 0:
    print("Positive")
elif given_number < 0:
    print("Negative")
else:
    print("Zero")
# Comment: Checking if the given number is positive, negative, or zero.

# 30. Escape Sequences and Print Formatting
print("This message includes a Unicode character: \u03A9")
# Comment: Unicode characters enhance text representation and support various symbols.

# 31. Operator Challenge - VI
num1_challenge_4 = float(input("Enter the first number: "))
num2_challenge_4 = float(input("Enter the second number: "))
num3_challenge_4 = float(input("Enter the third number: "))
num4_challenge_4 = float(input("Enter the fourth number: "))
average_challenge_4 = (num1_challenge_4 + num2_challenge_4 + num3_challenge_4 + num4_challenge_4) / 4
print(f"Average of four numbers: {average_challenge_4}")

# 32. Type Casting and Conditional Print
user_age_str_challenge = input("Enter your age: ")
user_age_int_challenge = int(user_age_str_challenge)
if user_age_int_challenge < 12:
    print("Child")

# 33. Operators and Print Formatting
base_triangle = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base_triangle * height_triangle
print(f"Area of the triangle: {area_triangle}")

# 34. Escape Sequences and Print Formatting
print("This message includes a percent symbol: 20%")
# Comment: The percent symbol can be included directly without escape sequences.

# 35. Type Casting Challenge
decimal_number_challenge = float(input("Enter a decimal number: "))
converted_int_challenge_2 = int(decimal_number_challenge)
print(f"Original Value: {decimal_number_challenge}, Converted to Integer: {converted_int_challenge_2}")
