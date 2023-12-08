haha = float(input())

def solve(grade):
    if grade >= 2.00 and grade <= 2.99:
        return 'Fail'
    elif grade >= 3.00 and grade <= 3.49:
        return 'Poor'
    elif grade >= 3.50 and grade <= 4.49:
        return 'Good'
    elif grade >= 4.50 and grade <= 5.49:
        return 'Very Good'
    elif grade >= 5.50 and grade <= 6.00:
        return 'Excellent'

print(solve(haha))

# def my_ass_top():
#     pass
#
#
# def my_ass(01. Programming Fundamentals Mid Exam Retake, my_ass_bottom=None):
#     print('thi is hoho')
#     my_ass_top()
#     my_ass_bottom()

# def multiply_numbers():
#     result = 5 * 5
#     print(result)
# multiply_numbers()
#
# def give_me_another_five():
#     return 5
#     print('This statement will not be printed.')
#     print(give_me_another_five())
