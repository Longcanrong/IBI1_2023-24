import xml.dom.minidom
import xml.sax
import matplotlib.pyplot as plt
from datetime import datetime
import os
import xml.sax.handler
from xml.sax.xmlreader import AttributesImpl

class GO_handler(xml.sax.ContentHandler):
    def __init__(self) -> None:
        self.counter = {
            "molecular_function":0,
            "biological_process":0,
            "cellular_component":0
        }
        self.start_time = 0
        self.end_time = 0
        self.process_time = 0
        self.currentElement = ""
        self.current_text = []  #String buffer
    
    def startElement(self, name: str, attrs: AttributesImpl) -> None:
        if name == "namespace":
            self.currentElement = name
        self.current_text = []
    
    def endElement(self, name: str) -> None:
        content = ''.join(self.current_text)
        if self.currentElement == "namespace" and content in self.counter.keys():
            self.counter[content] += 1
            self.currentElement = None
    
    def characters(self, content: str) -> None:
        self.current_text.append(content)

def count_go_terms_sax(xml_path):
    # Using SAX API to calculate the frequency
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = GO_handler()
    parser.setContentHandler(handler)
    parser.parse(xml_path)
    return handler

def plot_ontology_terms(count):
    labels = ['molecular_function', 'biological_process', 'cellular_component']
    value = count.values()
    plt.figure(figsize=(8, 5))
    plt.bar(labels, value, color=['blue', 'green', 'red'])

    plt.title('Gene Ontology Terms by Category')
    plt.xlabel('Ontology')
    plt.ylabel('Number of Terms')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

os.chdir('F:\Desktop\IBI\Practical14')
count = {'molecular_function': 0 , 'biological_process': 0, 'cellular_component': 0}
xml_path = "go_obo.xml"
# Use DOM API parsing XML
start_time_dom = datetime.now()
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
namespaces = collection.getElementsByTagName('namespace')
for namespace in namespaces:
    ontology = namespace.firstChild.nodeValue.strip()
    if ontology == 'molecular_function': count['molecular_function'] += 1
    if ontology == 'biological_process': count['biological_process'] += 1
    if ontology == 'cellular_component': count['cellular_component'] += 1
print(count)
plot_ontology_terms(count)
end_time_dom = datetime.now()
time_dom = end_time_dom - start_time_dom
print(f"time of DOM API: {time_dom.total_seconds()}")

# Use SAX API parsing XML
start_time_sax = datetime.now()
sax_handler = count_go_terms_sax('go_obo.xml')
print(sax_handler.counter)
plot_ontology_terms(sax_handler.counter)
end_time_sax = datetime.now()
time_sax = end_time_sax - start_time_sax
print(f"time of SAX API: {time_sax.total_seconds()}")

# The time of SAX API is quickest!