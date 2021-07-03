import requests
import re
import sys
import json

breached = False
def main():
	while True:
		print("Please enter the domain name followed by TLD\nExample: google.com\n")
		urlInput = input("Search domain: ")
		if urlInput.isnumeric()==False:
			is_breached(urlInput)
			if breached == True: 
				print("What would you like to do next?")
				print("1. See every breached info")
				print("2. See certain info")
				print("3. Try a different domain")
				print("4. Exit program")
				while True:
					userSelection = int(input("Pick a number: "))
					if userSelection==1:
						everything(urlInput)
					elif userSelection==2:
						promptOptions()
						specInfo = input("Pick a keyword to see info: ")
						moreInfo(urlInput,specInfo)
					elif userSelection==3:
						break
					elif userSelection==4:
						sys.exit()
					else:
						print("Please enter a valid number")
			if breached == False:
				print("What would you like to do next?")
				print("1. Try a different domain")
				print("2. Exit program")
				while True:
					userSelection = int(input("Pick a number: "))
					if userSelection==1:
						print("\n")
						break
					elif userSelection==2:
						sys.exit()
					else:
						print("Please enter a valid number")
		else:
			print("Cannot enter just numbers. Please try again\n")

#getting url and the response it provides us
url = 'https://haveibeenpwned.com/api/v3/breaches'
response= requests.get(url)


def jprint(obj):#properly indents list of dictionaries
	text = json.dumps(obj,sort_keys=True, indent=4)
	print(text)


def is_breached(urlInput):#checks if userinput is in any dicts domain
	for dictionary in response.json():
		if str(urlInput) in dictionary['Domain']:
			description(urlInput,dictionary['Description'])
			global breached
			breached = True
			return breached
	print(f'\n{urlInput}, this site has not been breached\n')


def moreInfo(urlInput,userInput):
	for dictionary in response.json():
		if str(urlInput) in dictionary['Domain']:
			string = dictionary[str(userInput)]
			print(f'{userInput}: {string}\n')


def everything(urlInput):
	for dictionary in response.json():
		if str(urlInput) in dictionary['Domain']:
			jprint(dictionary)


def description(userinput,dict):
	string = dict
	string = re.sub('<[^>]+>', '', string)
	string = string.replace("&quot;unverified&quot;","unverified")
	print(f'\nDestription: {string}')
	print(f'\n{userinput}, was breached.\n')


def promptOptions():
	print("AddedDate:    Date added into the database.")
	print("BreachDate:   Date the domain was breached.")
	print("DataClasses:  Types of info breached.")
	print("IsFabricated: Does it contain legitamate data?")
	print("IsRetired:    If the data is being redistributed or not.")
	print("IsSensitive:  Adult domain breached?")
	print("IsSpamList:   Targeted for spamming?")
	print("IsVerified:   100% proven it has been breached?")
	print("LogoPath:     Link to site's logo")
	print("ModifiedDate: Last modified date in system")
	print("Name:         Site name")
	print("PwnCount:     How many people were affected?")
	print("Title:        Title of breached site")


if __name__ == "__main__":
	main()

	
