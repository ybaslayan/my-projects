###  This program converts milliseconds into hours, minutes, and seconds ###

milsecs=input("Enter time in milliseconds ")
milsecs = int(milsecs)
seconds=(milsecs/1000)%60
#seconds = int(seconds)
minutes=(milsecs/(1000*60))%60
#minutes = int(minutes)
hours=(milsecs/(1000*60*60))%24

# print ("%d:%d:%d" % (hours, minutes, seconds))

print ("%d hour/s  %d minute/s %d second/s" % (hours, minutes, seconds))
 







# This code is contributed by dene
