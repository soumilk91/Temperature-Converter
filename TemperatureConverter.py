import sys
import os
import time

print "--------------- Soumil's Temperature Converter ---------------"
abc=0
while(abc!=1):
        
    ab=0
    while(ab!=1): 
        try:
            a=float(raw_input("\nPlease Enter the temperature value"))
            ab=1
        except:
            print"\n Please enter a numeric value . Text is not permitted "
    print "\n Is this temperature in kelvin , centigrade or fahrenheit ???"
    print "\n Press 1 for Kelvin"
    print "\n Press 2 for Centigrade"
    print "\n Press 3 for Fahrenheit"
    ###################### Taking input from the user about the current temperature unit ###############
    c=0
    while(c!=1):
        
        try:
            b=int(raw_input(""))
            
            if (b==1 or b==2 or b==3):
                c=1
            else:
                print "Please enter a valid option (1 or 2 or 3)"
        
    
        except:
            print "\n Wrong option Please enter a numeric value "
    
    
    #################### Taking input from user about desired temperature unit #######################
    
    print"\n What do you want to convert it in ????"
    print "\n Press 1 for Kelvin"
    print "\n Press 2 for Centigrade"
    print "\n Press 3 for Fahrenheit"
    c=0
    while(c!=1):
        
        try:
            d=int(raw_input(""))
            
            if (d==1 or d==2 or d==3):
                c=1
            else:
                print "Please enter a valid option (1 or 2 or 3)"
        
    
        except:
            print "\n Wrong option Please enter a numeric value "
            
    ####################### Conversion cha matter ######################################
    
    ############################### When options are same ############################
    if (b==d):
        print "\n Are even in your senses ??????? You are choosing the same options"
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
    
    
    
    
            
        
    
    
    
    ############################# Kelvin to Centigrade #######################
    if (b==1 and d==2):
        print "\n Converting degree kelvin to degree centigrade.... Please wait"
        time.sleep(3)
        p=a-273.15
        print "\n The temperature in degree Centigrade is : %f"%p
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
    
    
    
    
    
   
    
    
    ############################ Kelvin to Fahrenheit ########################
    
    if (b==1 and d==3):
        print "\n Converting degree Kelvin to degree fahrenheit ...... please wait"
        time.sleep(3)
        p=(a*(9/5))-459.67
        print "\n The temperature in degree Fahrenheit is : %f"%p
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
        
    
    
    
    
    
    
    ############################ Celsius to Kelvin ###########################
    
    if (b==2 and d==1):
        print "\n Converting degree Centigrade to degree Kelvin ..... please wait"
        time.sleep(3)
        p=a+273.15
        print "\n The temperature in degree Kelvin is : %f"%p
        
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
        
    
    
    
    
    
        
    ############################# Celsius to Fahrenheit ########################
    
    if (b==2 and d==3):
        print "\n Converting degree Centigrade to degree Fahrenheit .... please wait"
        time.sleep(3)
        p=(a*1.8)+32
        print "\n The temperature in degree Fahrenheit is : %f"%p
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
        
    
    
    
    
    
    
    
    ############################# Fahrenheit to Kelvin ############################
    if (b==3 and d==1):
        print "\n Converting degree Fahrenheit to degree Kelvin"
        time.sleep(3)
        p=(a+459.67)/(9/5)
        print"\n The temperature in degree Kelvin is : %f"%p
        
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
    
    
    
    
    
        
    ########################### Fahrenheit to Celsius ############################
    if (b==3 and d==2):
        print"\n Converting degree Fahrenheit to degree Centigrade "
        time.sleep(3)
        p=(a-32)/(9/5)
        print "\n The temperature in degree Centigrade is : %f"%p
        
        
        ch=raw_input("\nAre you done using Soumil's Temperature Converter  ??? y or n")
        if (ch=="y" or ch =="Y"):
            print"\n Thank you ..... See you again .............."
            abc=1
    
    
    
    
    
    
     
    
    
        



    


    
    

        
    