from xml.etree import ElementTree

#tree = ElementTree.parse("example_input.xml")
#root = tree.getroot()
root = ElementTree.fromstring(input())

def getChildren(r, level):
    level += 1
    for child in r:
        if not child.attrib['color'] in colors:
            colors[child.attrib['color']] = 0
        colors[child.attrib['color']] += level
        getChildren(child, level)

colors = {}
colors[root.attrib['color']] = 0
colors[root.attrib['color']] += 1
getChildren(root, 1)
colors_sort = list(colors.items())
colors_sort.sort(key=lambda x: x[0], reverse=True)
print(colors_sort)
print(" ".join(map(str, map(lambda x: x[1], colors_sort))))


"""
for ch in root:
    print(ch.attrib['color'])
    if not color_dic[ch.attrib['color']]:
        color_dic[ch.attrib['color']] = 1
    color_dic[ch.attrib['color']] += 1
    for ch2 in ch:
        if not color_dic[ch2.attrib['color']]:
            color_dic[ch2.attrib['color']] = 1
        color_dic[ch2.attrib['color']] += 2
        print(ch2.attrib['color'])
for child in root.iter("cube"):
    print(child.tag, child.attrib)
"""
