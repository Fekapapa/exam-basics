# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases
#alma = [3, 6, 7 , 9] 6.3
class Odd_Averager(object):
    def odd_average(self, numbers = [0]):
        summarize = 0
        counter = 0
        for number in numbers:
            if number % 2 == 1:
                summarize += number
                counter += 1
        if counter == 0:
            average = 0
        else:
            average = summarize / counter
        return average
