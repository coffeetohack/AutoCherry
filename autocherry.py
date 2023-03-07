import os
import subprocess
import xml.etree.ElementTree as ET

# Ask for the CherryTree file path
cherrytree_path = input("Enter the CherryTree file path: ")

# Create the CherryTree file if it doesn't exist
if not os.path.exists(cherrytree_path):
    root = ET.Element("cherrytree")
    tree = ET.ElementTree(root)
    tree.write(cherrytree_path)

while True:
    # Ask for the command and node name
    command = input("Enter the command to run: ")
    node_name = input("Enter the node name: ")
    
    # Run the command and get the output
    output = subprocess.check_output(command, shell=True, text=True)
    print("Output:\n", output)
    
    # Parse the CherryTree file and add the output to the specified node
    root = ET.parse(cherrytree_path).getroot()
    node = root.find(".//node[@name='" + node_name + "']")
    if node is None:
        node = ET.SubElement(root, "node", {"name": node_name})
    else:
        print("Node Found:\n", node)
    node_text = ET.SubElement(node, "rich_text")
    node_text.text = output
    ET.ElementTree(root).write(cherrytree_path)
    #print("Output Written to Node:\n", node_text)
    
    # Ask if the user wants to run another command
    choice = input("\nDo you want to run another command? (Y/N): ")
    if choice.upper() == "N":
        print("Script Executed Successfully")
        break

