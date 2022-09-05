import random
from turtle import clear
from hashlib import sha256
import time
from time import sleep

class User:

    ##DEFINES THE ATTRIBUTES OF THE USER CLASS
    def __init__(self, address, trust, age, location, friendslist, success, failure, energysource):
        self.address = address
        self.trust = trust
        self.age = age
        self.location = location
        self.friendslist = friendslist
        self.success = success
        self.failure = failure
        self.energysource = energysource
        friendslist = []


    ##ONE USER MUST RANDOMLY BE CHOSEN AS A "TRANSACTOR"
    def transaction(self):
        return "{} wants to spend money!".format(self.address)

    ##WRITE A FUNCTION FOR THE CONSENSUS MECHANISM.
    ##TYPE IS MEANT TO REPRESENT WHAT KIND OF VALIDATOR THE TRANSACTOR MIGHT WANT
    ##TRUE MEANS THE VALIDATOR WILL BE 'TRUSTED'
    ##FALSE MEANS THE VALIDATOR WILL BE 'NEW'
    def pof(self):
        type = random.choice([True, False])
        if type == True and len(self.friendslist)>0:
            print(f"{self.address} has opted for a Trusted Validator.")
            ##POTENTVALIDATOR MEANS POTENTIAL VALIDATOR

            potentvalidator = random.choice(self.friendslist)
            
            ##FOR HIGH AND MEDIUM TRUST, WHEN ENERGY SOURCE IS GIVEN TOP PRIORITY, AND LOCATION SECOND
            if potentvalidator.location == self.location and potentvalidator.trust>=0.9 and potentvalidator.energysource == True:
               validator = potentvalidator
               print('Transaction fee for Trusted entity: high')
            elif potentvalidator.location == self.location and potentvalidator.trust>=0.75 and potentvalidator.energysource == True:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: high')
            elif potentvalidator.location != self.location and potentvalidator.trust>=0.9 and potentvalidator.energysource == True:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: high')
            elif potentvalidator.location != self.location and potentvalidator.trust>=0.75 and potentvalidator.energysource == True:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: high')
            
            ##FOR NON-RENEWABLE ENERGY SOURCES

            elif potentvalidator.location == self.location and potentvalidator.trust>=0.9 and potentvalidator.energysource == False:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: medium')                
            elif potentvalidator.location == self.location and potentvalidator.trust>=0.75 and potentvalidator.energysource == False:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: medium')            
            elif potentvalidator.location != self.location and potentvalidator.trust>=0.9 and potentvalidator.energysource == False:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: medium')
            elif potentvalidator.location != self.location and potentvalidator.trust>=0.75 and potentvalidator.energysource == False:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: medium')
            
            ##FOR LOWEST TRUST, LOCATION MUST BE THE SAME, AND HERE ENERGY SOURCE IS STILL GIVEN A PRIORITY
            elif potentvalidator.location == self.location and potentvalidator.trust>=0.5 and potentvalidator.energysource == True:
               validator = potentvalidator
               print('Transaction fee for Trusted entity: low')
            elif potentvalidator.location == self.location and potentvalidator.trust>=0.5 and potentvalidator.energysource == False:
                validator = potentvalidator
                print('Transaction fee for Trusted entity: low')
            else:
                print(f"No Trusted Validators found, price has been reduced! {self.address} will use a New Validator!")
                validator = random.choice(list)
        else:
            print(f"{self.address} has opted for a New Validator.")
            validator = random.choice(list)
            print('Transaction fee for new entity: low')

            ##THE FOLLOWING IF STATEMENT IS TO MAINTAIN A FRIENDSLIST OF 3 PEOPLE. THIS IS A STATIC NUMBER, BUT IT CAN BE DYNAMIC
            if len(self.friendslist) == 3:
                self.friendslist.pop(2)
                self.friendslist.insert(0, validator)
            else:
                self.friendslist.insert(0,validator)
        print(f"{validator.address} has been chosen as validator for {self.address}'s transaction.")
        validator.age += 1


        ##THIS IS WHERE THE FAILURE OR SUCCESS OF A TRANSACTION MUST BE DETEREMINED
        ##FOR THE SAKE OF THIS MODEL, THE CHANCE OF FAILURE IS 1 IN 10
       
        chanceoffailure = random.randint(0,9)
        if chanceoffailure == 1:
            print(f"{validator.address} failed their validation!")
            validator.failure += 1
            validator.trust = (validator.success/(validator.failure + validator.success))
            print(f"{validator.address}'s trust has decreased to {validator.trust}!")
            
        else:
            print(f"{validator.address} succeeded in their validation!")
            validator.success += 1
            validator.trust = (validator.success/(validator.failure + validator.success))
            print(f"{validator.address}'s trust has increased to {validator.trust}!")
            # time.sleep(10.085)


            if transactor.location == "HongKong" and validator.location == "India":
                time.sleep(0.085)
            elif transactor.location == "India" and validator.location == "HongKong":
                time.sleep(0.085)
            elif transactor.location == "India" and validator.location == "Japan":
                time.sleep(0.123)
            elif transactor.location == "Japan" and validator.location == "India":
                time.sleep(0.123)
            elif transactor.location == "Japan" and validator.location == "HongKong":
                time.sleep(0.044)
            elif transactor.location == "HongKong" and validator.location == "Japan":
                time.sleep(0.044)
            else:
                time.sleep(0)

            
            User.Blockchain.addblock(self, User.mainchain)


        print(f"{validator.address}'s age has increased to {validator.age}!")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(f"{current_time}")
        
        ##IF THE TRANSACTION FAILS, IT CANNOT BE MINTED INTO THE BLOCKCHAIN
        ##HENCE THE MINTING PROCESS MUST BE A FUNCTION
        
    class Blockchain:

        def __init__(self, ledger):
            self.ledger = ledger
            

        def addblock(self, blockchain):
            
            transaction_string = f"{self.address} wants to invest 'x' tokens!"
            hashed_string = sha256(transaction_string.encode('utf-8')).hexdigest()
            print(hashed_string)
            
            User.mainchain.ledger.append(hashed_string)

    
    mainchain = Blockchain([])
            

user1 = User("User1", 0, 0, "Japan", [], 0, 0, True)
user2 = User("User2", 0, 0, "Japan", [], 0, 0, False)
user3 = User("User3", 0, 0, "Japan", [], 0, 0, False)
user4 = User("User4", 0, 0, "India", [], 0, 0, False)
user5 = User("User5", 0, 0, "India", [], 0, 0, True)
user6 = User("User6", 0, 0, "India", [], 0, 0, True)
user7 = User("User7", 0, 0, "India", [], 0, 0, False)
user8 = User("User8", 0, 0, "HongKong", [], 0, 0, False)
user9 = User("User9", 0, 0, "HongKong", [], 0, 0, True)
user10 = User("User10", 0, 0, "HongKong", [], 0, 0, True)



list = []

list.append(user1)
list.append(user2)
list.append(user3)
list.append(user4)
list.append(user5)
list.append(user6)
list.append(user7)
list.append(user8)
list.append(user9)
list.append(user10)


i = 1
while i <= 100:

    transactor = random.choice(list)
    print(f"The user named {transactor.address} would like to make a transaction!")

    ##OBVIOUSLY, A USER CAN'T VALIDATE THEMSELVES
    list.remove(transactor)
    
    User.mainchain.ledger = []

    transactor.pof()

    list.append(transactor)

    print("=======================================================")

    i += 1


