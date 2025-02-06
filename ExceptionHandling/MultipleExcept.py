def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError occurred and handled')
    except NameError:
        print("NameError occurred and handled")
    except TypeError:
        print("TypeError occurred and handled")
    except:
        print("Some error occurred and handled")

disp(10,'kodnest')