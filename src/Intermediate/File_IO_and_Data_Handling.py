"""
Now that we have covered file I/O operations in Python, let's explore how to handle different data formats such as CSV, JSON, and XML.
-----------------------Handling CSV Files-------------------------
CSV (Comma-Separated Values) is a common data format used for storing tabular data.
Python provides a built-in csv module to read from and write to CSV files.
Here's an example of how to read a CSV file:
"""
import csv
with open('data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
# You see in above code we opened a CSV file named 'data.csv' in read mode.
# We used the csv.reader() function to read the file and iterated through each row to print its contents.
"""
-----------------------Writing to a CSV File-------------------------
You can also write data to a CSV file using the csv module. Here's an example:
"""
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Alice', 30, 'New York'])
    csv_writer.writerow(['Bob', 25, 'Los Angeles'])
# You see in above code we opened a CSV file named 'output.csv' in write mode.
# We used the csv.writer() function to write rows of data to the file.

"""
-----------------------Handling JSON Files-------------------------
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
Python provides a built-in json module to work with JSON data.
Here's an example of how to read a JSON file:
"""
import json
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
# You see in above code we opened a JSON file named 'data.json' in read mode
# We used the json.load() function to parse the JSON data and print its contents.

"""
-----------------------Writing to a JSON File-------------------------
You can also write data to a JSON file using the json module. Here's an example:
"""
with open('output.json', 'w') as file:
    data = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
    json.dump(data, file)
# You see in above code we opened a JSON file named 'output.json' in write mode.
# We created a dictionary named data and used the json.dump() function to write the data to the file.

"""
-----------------------Handling XML Files-------------------------
XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.
Python provides a built-in xml.etree.ElementTree module to work with XML data.
Here's an example of how to read an XML file:
"""
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
# You see in above code we parsed an XML file named 'data.xml' using the ET.parse() function.
# We got the root element of the XML tree and iterated through its child elements to print their tags and attributes.

"""
-----------------------Writing to an XML File-------------------------
You can also write data to an XML file using the xml.etree.ElementTree module. Here's an example:
"""
root = ET.Element('data')
item1 = ET.SubElement(root, 'item')
item1.set('name', 'item1')
item1.text = 'This is item 1'
item2 = ET.SubElement(root, 'item')
item2.set('name', 'item2')
item2.text = 'This is item 2'
tree = ET.ElementTree(root)
tree.write('output.xml')
# You see in above code we created an XML structure with a root element named 'data'
# We added two child elements named 'item' with attributes and text.
# Finally, we wrote the XML structure to a file named 'output.xml' using the tree.write() function.

"""
-----------------------Summary-------------------------
In this module, we learned how to handle different data formats such as CSV, JSON, and XML using Python's built-in modules.
We covered reading from and writing to these file formats, which is essential for data handling and manipulation in various applications.
"""

"""
------------------------------Practice time!----------------------
1. Create a CSV file named "students.csv" with columns "Name", "Age", and "Grade". Write a Python script to read the file and print the names of students who have scored above 85 in Grade.
2. Create a JSON file named "config.json" that contains configuration settings for an application (e.g., "theme", "language", "autosave"). Write a Python script to read the file and print the configuration settings.
3. Create an XML file named "books.xml" that contains a list of books with attributes like "title", "author", and "year". Write a Python script to read the file and print the titles of books published after the year 2000.
"""