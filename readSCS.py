from xml.etree.ElementTree import parse as parseXML

with open("puffs.scs11", encoding="utf-8") as file:
    xml = parseXML(file)

print(list(xml.iter()))