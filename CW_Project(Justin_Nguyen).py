# 1. Basic Training: Add item to an Array
# Add the value "codewars" to the websites array.
# After your code executes the websites array should == ["codewars"]

# The websites array has already been defined for you using the following code:

# websites = []

# solution :
# websites == []
# websites.append("codewars")

# link: https://www.codewars.com/kata/511f0fe64ae8683297000001

# 2. Even or Odd - Which is Greater?

# Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

    # If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

    # If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

    # If the total of both even and odd numbers are identical return: "Even and Odd are the same"

# solution:

# def even_or_odd(s):
#     even_sum = 0
#     odd_sum = 0
    
#     for char in s:
#         num = int(char)
        
#         if num % 2 == 0:
#             even_sum += num
            
#         else: 
#             odd_sum += num
            
#     if even_sum > odd_sum:
#         return "Even is greater than Odd"
    
#     elif odd_sum > even_sum:
#         return "Odd is greater than Even"
    
#     else:
#         return "Even and Odd are the same"

# link: https://www.codewars.com/kata/57f7b8271e3d9283300000b4

# 3. The Hashtag Generator

# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 chars it must return false.
#     If the input or the result is an empty string it must return false.

# Examples

# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

# solution:
# def generate_hashtag(s):
#     if not s:
#         return False
    
#     words = s.split()
    
#     words = [word.capitalize() for word in words]
    
#     s = ''.join(words)
    
#     s = '#' + s
    
#     if len(s) > 140:
#         return False
    
#     return s

# link: https://www.codewars.com/kata/52449b062fb80683ec000024

# 4. Thinkful - String Drills: Quotable

# This function should take two string parameters: a person's name (name) and a quote of theirs (quote), and return a string attributing the quote to the person in the following format:

# '[name] said: "[quote]"'

# For example, if name is 'Grae' and 'quote' is 'Practice makes perfect' then your function should return the string

# 'Grae said: "Practice makes perfect"'

# Unfortunately, something is wrong with the instructions in the function body. Your job is to fix it so the function returns correctly formatted quotes.

# Click the "Train" button to get started, and be careful with your quotation marks.

# solution:
# def quotable(name, quote):
#     return f'{name} said: "{quote}"'

# link: https://www.codewars.com/kata/5859c82bd41fc6207900007a

# 5. Stolen police records

# A crime scene has been discovered, and among the evidence is a list of agents, with no apparent connection.

# Your job in the records department is to match this list with police records to find an exact match.

# Your function will receive a list as the first parameter, the stolen record, followed by a list of lists, the database.

# A match is found only if it contains the same names in the same order, no more, no less. Your code should return None if the first parameter is an empty list. The database will always contain more than one list. A match should return "Match found". If no matches are found, your code should return "No matches".

# Example: agents(["John", "Sarah"], [["John", "Sarah"], ["Mary", "David"]]) == "Match found"


# solution: 
# def agents(list_found, list_records):
#     if not list_found:
#         return None
#     if list_found in list_records:
#         return "Match found"
#     else:
#         return "No matches"

# link : https://www.codewars.com/kata/5a5bef7a5c770d08cd0032fa