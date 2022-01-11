import random
import hashlib
import string
from tqdm import tqdm


amountmined = 0
amountwanted = 5000000
amount=amountwanted

for i in tqdm(range(amountwanted)):
	letters = string.ascii_lowercase
	
	coinattemp =  ''.join(random.choice(letters) for i in range(10))
 
	if int((hashlib.md5(coinattemp.encode()).hexdigest()),16) < 8635311173685500060942228817600819483 :
		#testIfExists()
		amountmined = amountmined + 1

print("amount mined:",amountmined)
print(amountmined/amountwanted)

