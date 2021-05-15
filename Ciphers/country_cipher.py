
# Country Cipher made by Nicholas Johansan
# Just a made up cipher where by words are represented by countries
# Every letter will be replaced by a flag of a country which begins with that letter
# E.g. Hello -> Hungary Ethiopia Latvia Libya Oman
# Then replace the names with their flags in unicode
# There is 2 modes - WhatsApp & Discord
# WhatsApp is for decoding/encoding a msg with this cipher from WhatsApp
# Discord is for decoding/encoding a msg with this cipher from Discord

import json
import random
import re

country_dict = json.load(open("../JSON/country_dict.json", 'r'))["3166-1"]
country_list = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Saint BarthÃ©lemy', 'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands', 'Switzerland', 'Chile', 'China', "CÃ´te d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the', 'Congo', 'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'CuraÃ§ao', 'Christmas Island', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'Falkland Islands (Malvinas)', 'France', 'Faroe Islands', 'Micronesia, Federated States of', 'Gabon', 'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Guinea', 'Guadeloupe', 'Gambia', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory', 'Ireland', 'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Saint Martin (French part)', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Montserrat', 'Martinique', 'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger', 'Norfolk Island', 'Nigeria', 'Nicaragua', 'Niue', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Pitcairn', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of', 'French Polynesia', 'Qatar', 'RÃ©union', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands', 'Saint Helena, Ascension and Tristan da Cunha', 'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Saint Pierre and Miquelon', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Tokelau', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Uganda', 'Ukraine', 'United States Minor Outlying Islands', 'Uruguay', 'United States', 'Uzbekistan', 'Holy See (Vatican City State)', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia', 'Zimbabwe']

def flag(code):
	OFFSET = ord('🇦') - ord('A')
	return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

def deflag(code):
	OFFSET = ord('A') - ord('🇦')
	return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)

def find_countries(alphabet):
	alphabet = alphabet.upper()
	available_countries = list(filter(lambda country: country[0] == alphabet, country_list))
	if len(available_countries) == 0:
		available_countries = ["None"]
	return available_countries

def compile_code(text, c_type):
	compiled_text = ""
	for character in text:
		if not character.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if character == " ":
				if c_type == "discord":
					compiled_text += "     "
				else:
					compiled_text += "   "
			else:
				compiled_text += character
		else:
			countries = find_countries(character)
			alpha_2 = ""
			if "None" in countries:
				compiled_text += f"[{character}]"
			else:
				country = random.choice(countries)
				for country_data in country_dict:
					if country_data["name"] == country:
						alpha_2 = country_data["alpha_2"]
						break
				if c_type == "discord":
					compiled_text += f":flag_{alpha_2.lower()}: "
				elif c_type == "whatsapp":
					compiled_text += f"{flag(alpha_2)}"
	print(compiled_text)

def decompile_code(text, c_type):
	decompiled_text = ""
	if c_type == "whatsapp":
		first = ""
		for character in text:
			if not character.upper() in "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿":
				first = ""
				decompiled_text += character
			else:
				if first == "":
					first = character
				else:
					alpha_2 = deflag(f"{first}{character}")
					for country_data in country_dict:
						if country_data['alpha_2'] == alpha_2:
							decompiled_text += (country_data['name'])[0].lower()
							break
					first = ""
		print(decompiled_text)
	elif c_type == "discord":
		decompiled_text = ""
		for word in text.split("     "):
			for flag_emoji in re.findall(":flag_[a-zA-Z][a-zA-Z]:", word):
				alpha_2 = flag_emoji[6:8].upper()
				for country_data in country_dict:
					if country_data['alpha_2'] == alpha_2:
						decompiled_text += (country_data['name'])[0].lower()
						break
			decompiled_text += " "
		print(decompiled_text)

# Usage - WhatsApp	
#compile_code("a message", "whatsapp")
#decompile_code("🇦🇮   🇲🇳🇬🇶🇸🇳🇸🇯🇦🇲🇬🇼🇪🇬", "whatsapp")

# Usage - Discord
#compile_code("a message", "discord")
#decompile_code(":flag_ad:      :flag_mt: :flag_et: :flag_sm: :flag_se: :flag_ai: :flag_gr: :flag_gq:", "discord")
