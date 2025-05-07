Days_Per_Year:int = 365
Hours_Per_Day:int = 24
Min_Per_Hour:int = 60
Second_Per_Min:int = 60

def main():
    Second_Per_Year:int = (Days_Per_Year * Hours_Per_Day * Min_Per_Hour * Second_Per_Min)

    print(f"There are {Second_Per_Year} seconds in a year!")


main()