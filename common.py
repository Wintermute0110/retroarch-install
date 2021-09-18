# --- Python standard library --------------------------------------------------------------------
import subprocess
import sys
import xml.etree.ElementTree as ET

# Read the configuration XML file an return a dictionary with options.
def read_config_file(filename):
    __debug_xml_parser = True
    print('Reading XML configuration file "{}"'.format(filename))
    configuration = {}
    xml_tree = ET.parse(filename)
    xml_root = xml_tree.getroot()
    for category_element in xml_root:
        xml_tag  = category_element.tag
        xml_text = category_element.text if category_element.text is not None else ''
        configuration[xml_tag] = xml_text
        if __debug_xml_parser: print('"{}" : "{}"'.format(xml_tag, xml_text))

    return configuration

def run(arg_list):
    # print(str(arg_list))
    ret = subprocess.call(arg_list)
    if ret != 0:
        print('[ERROR] Got code {} executing command {}'.format(ret, arg_list[0]))
        sys.exit(1)
