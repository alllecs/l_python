from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

"""
#READ XML
print(root) #<Element 'studentsList' at 0x7f2f84cc5638>
print(root.tag, root.attrib) #studentsList {}

for child in root:
    print(child.tag, child.attrib)

print(root[0][0].text)

for element in root.iter("scores"): #перебрать все элементы в поддереве, #findall - только среди детей
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)
"""

"""
#WRITE XML
#tree.write("example_copy.xml")
greg = root[0]
module1 = next(greg.iter("module1"))
print(module1, module1.text) #70 баллов в 1м модуле

module1.text = str(float(module1.text) + 30)
#tree.write("example_modified.xml")

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
greg = root[0]
certificate = greg[2]
certificate.set("type", "with distinction") #добавить type
tree.write("example_modified.xml")
"""

"""
#ADD Elements
greg = root[0]
description = ElementTree.Element("description") #1й аргумент, ТЕГ, который мы хотим создать
description.text = "Showed excellent skills during the course"
greg.append(description) #Добавить описание 
tree.write("example_modified.xml")
"""

"""
#Delete
tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()
greg = root[0]
description = greg.find("description") #найти вхождения тега
greg.remove(description) #удалить элемент
tree.write("example_modified.xml")
"""

"""
#Creat tree
root = ElementTree.Element("student")

first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"

second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"

scores = ElementTree.SubElement(root, "scores")
module1 = ElementTree.SubElement(scores, "module1")
module1.text = "100"
module2 = ElementTree.SubElement(scores, "module2")
module2.text = "80"
module3 = ElementTree.SubElement(scores, "module3")
module3.text = "90"

tree = ElementTree.ElementTree(root)
tree.write("student.xml")
"""

































