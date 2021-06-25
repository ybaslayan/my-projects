###  This program converts milliseconds into hours, minutes, and seconds ###

def main():
    millis=input("Enter time in milliseconds ")
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = round(int(seconds), 2)
    minutes=(millis/(1000*60))%60
    minutes = round(int(minutes), 2)
    hours= round(( (millis/(1000*60*60))%24 ), 2)
#days = round((millis/1000*60*60*24)%24, 2)
    days = round((millis/86400000), 2)
    print(f"Days:{days}, Hours:{hours}, Minutes:{minutes}, Seconds:{seconds}")

main()





# This code is contributed by dene
