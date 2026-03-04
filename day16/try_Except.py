'''try:
    if a>10:
        print("good")

except NameError:
    print('a is not defined')'''


'''else:
    print('no errors')

finally:
    print("End of the block")

#handling multiple exceptions

try:
    a={1:1,2:4,3:9}
    print(a[4])

except NameError:
    print('a is not defined')
    
except ValueError:
    print("Enter the requested datatype")

except TypeError:
    print("Data types are different")

except ZeroDivisionError:
    print("Cant divide with Zero")

except IndexError:
    print("The index is not present")

except KeyError:
    print("In dic this key is niot present")
    
    

else:
    print('no errors')

finally:
    print("End of the block")
'''


'''
try:
    a=a+'8'
    print(a[4])
    
except  (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) a
    print('f Error occured: {e}')

else:
    print('No Errors')

finally:
    print("End of the block")'''

'''
try:
    a=int(input())
    print(a[4])

except Exception as e:
    print(f'Error Occured: {e}')
else:
    print('No errors')

finally:
    print("End of the block") '''
'''
try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive Value")

except Exception as e:
    print(f'Error Occured: {e}')

else:
    print('No Errors')

finally:
    print("End of the block")'''
#
while True:
    print("\n ----ATM Simulation Menu ----")
    print("1.Check average transation(ZeroDivisionError)")
    print("2.Withdraw With Invalid Input (ValueError)")
    print("3.Deposite with invalid datatype (TypeError)")
    print("4.Access Invalid Transaction History (Indexerror)")
    print("5.Access non Existent Account (KeyError)")
    print("6.Read Missing Transaction log file (FileNotFoundError)")
    print("7.exit")


    choice = input("Select an option (1-7): ")

    if choice == "1":
        Zero_division_error_case()
    elif choice == "2":
        Value_error_case()
    elif choice == "3":
        type_error_case()
    elif choice == "4":
         Index_error_case()
    elif choice == "3":
         Key_error_case()
    elif choice == "3":
         File_Not_Found_error_case()



#
def value_error_case():
    try:

        withdrawl_amount = int("100 /")
        print("Withdrawing:",withdrawal_amount)
    except ValueError:
        print("Error: Invalid value entered. Please enter a numeric





#

def type_error_case():
    try:

        balance = 500
        deposit_amount = "100"
        new_balance = balance+deposite_amount
        print("New Balance:",new_balance)
    except TypeError:
        print("error: Incompatible data types .Cannot add string 

         
               
