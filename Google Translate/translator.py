import requests


def translate():

	url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

	text = input("Please enter a phrase you would like to translate: ")
	new_str = text.replace(' ', '%20')
	new_str = text.replace(',', '%2C')

	lang = input("What language would you like to translate to? ")

	payload = "q=" + new_str + "&target=" + lang + "&source=en"
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": "47c7341552msh2af4ad72098aae9p14f307jsn2d384fff1a38",
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}

	response = requests.request("POST", url, data=payload, headers=headers)
	data = response.json()
	translated_value = data['data']['translations'][0]['translatedText']
	print(translated_value)
