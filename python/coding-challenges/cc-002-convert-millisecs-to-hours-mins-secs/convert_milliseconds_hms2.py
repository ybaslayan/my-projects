###  This program converts milliseconds into hours, minutes, and seconds ###

def convertMillis(millis):
     seconds=(millis/1000)%60
     minutes=(millis/(1000*60))%60
     hours=(millis/(1000*60*60))%24
     return seconds, minutes, hours

def main():
     millis=input("Enter time in milliseconds ")
     con_sec, con_min, con_hour = convertMillis(int(millis))
     print("{0}:{1}:{2}".format(con_hour, con_min, con_sec))

main()






# This code is contributed by dene
