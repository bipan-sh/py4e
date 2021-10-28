import xml.etree.ElementTree as ET 

fhand = open('plant_catalog.xml')

reader = fhand.read()

catalog = ET.fromstring(reader)

plant = catalog.findall('PLANT/COMMON')
print(len(plant))


for item in catalog:
    print('\nName: ', item.find('COMMON').text)
    print('Scientific name: ', item.find('BOTANICAL').text)
    print('Price: ', item.find('PRICE').text)