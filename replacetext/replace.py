data = '''
20 ლარ�?ს ჩათვლ�?თ გადახდაზე - 50 თეთრ�?. 
20 ლარზე მეტ�?ს გადახდაზე - 1 ლარ�?.

'''

new_str = ""

for line in data.split('\n'):
	new_str += line.replace('�?','ი') + '\n'

print(new_str)
