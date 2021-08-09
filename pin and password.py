import random

Set= '1234567890$%^&*_<>QWERTYUIOPASDFGHJKLZXCVBNMqazwsxedcrfvtgbyhnujmikolp'
Set0 ='1234567890'

while True:

    a = input('PIN / Password :')
    A = a.upper()

    try :

        if A == 'PASSWORD':
             x = int(input('Number of passsword:'))
             z = int(input('Password length: :'))

             if z <= 4:
               z = 4
             elif 4 < z < 16 :
               z = z
             elif z >= 16 :
               z = 16
             
             for i in range (x):
               password = ''.join(random.sample(Set, z))
               print('Your password is :{}'.format(password))
        elif A == 'PIN' :
             y = int(input('Number of PIN:'))
             Y = int(input('PIN length:'))

             for i in range(y) :
                PIN = ''.join(random.sample(Set0, Y))
                print('Your password is:{}'.format(PIN))
        else :
             a


        
         
    except:
        print('error')
