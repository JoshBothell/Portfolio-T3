#Josh Bothell
#9/18
# change sorter

def change():
    #1 get input from user
    total_change = int(input("How much change do you have in your pocket: "))
    #2 calculate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickels = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left // 1
    #3 display it back to user
    print(" Quarters: ", quarters, "\n Dimes: ", dimes, "\n Nickels: ", nickels, "\n Cents: ", cents)


change()
    
def change2(total_change):
    #1 get input from argument
    total_change = total_change
    #2 calculate total for q n d p
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickels = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left // 1
    #3 return value
    return quarters, dimes, nickels, cents


total_change = int(input("How much change do you have in your pocket: "))
quarters, dimes, nickels, cents = change2(total_change)
print(" Quarters: ", quarters, "\n Dimes: ", dimes, "\n Nickels: ", nickels, "\n Cents: ", cents) 
