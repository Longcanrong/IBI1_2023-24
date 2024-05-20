import xml.dom.minidom
import xml.sax
import matplotlib.pyplot as plt
from datetime import datetime
import os
class GoTermsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.ontologies = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.current_namespace = ''
        self.current_tag = ''

    def startElement(self, tag, attributes):
        self.current_tag = tag

    def endElement(self, tag):
        if tag == 'namespace':
            self.current_namespace = ''

    def characters(self, content):
        if self.current_tag == 'namespace':
            self.current_namespace = content.strip()

        if self.current_namespace in self.ontologies and self.current_tag == 'term':
            self.ontologies[self.current_namespace] += 1

def parse_go_terms_with_sax(xml_file):
    handler = GoTermsHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    return handler.ontologies

def plot_ontology_terms(count1,count2,count3):
    labels = ['molecular_function', 'biological_process', 'cellular_component']
    values = [count1,count2,count3]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'green', 'red'])

    plt.title('Gene Ontology Terms by Category')
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

os.chdir('F:\Desktop\IBI\Practical14')
count1 = 0
count2 = 0
count3 = 0

# Use DOM API parsing XML
start_time_dom = datetime.now()
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
namespaces = collection.getElementsByTagName('namespace')
for namespace in namespaces:
    ontology = namespace.firstChild.nodeValue.strip()
    if ontology == 'molecular_function': count1 += 1
    if ontology == 'biological_process': count2 += 1
    if ontology == 'cellular_component': count3 += 1
print(count1, count2, count3)
plot_ontology_terms(count1,count2,count3)
end_time_dom = datetime.now()
time_dom = end_time_dom - start_time_dom
print(f"time of DOM API: {time_dom.total_seconds()}")

# Use SAX API parsing XML
start_time_sax = datetime.now()
ontologies = parse_go_terms_with_sax("go_obo.xml")
print(count1, count2, count3)
plot_ontology_terms(count1,count2,count3)
end_time_sax = datetime.now()
time_sax = end_time_sax - start_time_sax
print(f"time of SAX API: {time_sax.total_seconds()}")

# The time of SAX API is quickest!