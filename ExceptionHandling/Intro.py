def disp(a,b):
    try:
        print('Task Started')
        print(a/b)  #ZeroDivisionError
    except:
        print("Some error Handled")
    else:
        print('Task executed without any exception')
    finally:
        print('Task Ended')

disp(10,0)
disp(10,5)
disp(20,2)

# Task Started
# Some error Handled
# Task Ended
# Task Started
# 2.0
# Task executed without any exception
# Task Ended
# Task Started
# 10.0
# Task executed without any exception
# Task Ended


'''
try: Used to keep the logic in which we may get some error.

except: Will be exceuted when exception occurrs in try block logic

else: Will be exceuted when try block logic will be excuted without any error

finally: Will always executed irrespective of exception occurred or not.

'''