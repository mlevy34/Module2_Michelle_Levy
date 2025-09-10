"""
Michelle Levy, the purpose of this assigment is to convert a certain amount of minutes to how many hours and minutes it is.
"""



#Declare the conversion rate, over here, we use this to help convert hours into minutes
HOUR_CONV = 60
"""
When this function is called, it will display the question that the users will be asked. That question is how many minutes would you like to calculate? Then, once the user puts in how many minutes they want to calculate,
the function will first determine the amount of hours by diving the minutes by 60, and then find the minutes by using te % sign to determine the remainder of the minutes divided by 60.Once the hours and minutes
are calculated, the results will be printed to the user and they will receive their answer.
"""
def minutes_to_hours_and_minutes() :
    # The question that will be displayed for the users to answer
    question = "How many minutes would you like to calculate?"
    # The input the user puts in will be saved into the variable minutes
    minutes = int(input(question))
    # Determine the number of full hours by diving the total number of minutes by 60
    num_hours = minutes//HOUR_CONV
    # Determine the number of minutes after finding the total number of hours by finding the REMAINDER of minutes/60
    num_minutes = minutes % HOUR_CONV
    # Display the final result of total hours and minutes
    print(num_hours , "hours","and",num_minutes,"minutes")


# Calling the function
minutes_to_hours_and_minutes()
