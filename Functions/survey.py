print ('hellow sir', 'we are doing a survey' , 'press Y to continue or N to pass on')
def survey() :
    print ('what is your name')
    name = input()
    print ('what is your age')
    age = input()
    if int(age) < 18 :
        print ('are you a minor', 'if yes then press Y')
        realage = input()
        if realage != 'Y' :
            print ("you are a liar")
        else :
            print('well its a adult survey', 'you can continue')
    else :
        print ('continue sir')
    print ('what is your gender')
    gender = input()
    print ('what is your job')
    job = input()
    print ('what is your salary')
    salary = input()
    print ('how many siblings do you have')
    sibling = input()
user = input()
if user != 'N' :
    survey()
else :
    print ('thank you') 
    