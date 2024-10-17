# Open the file and read the contents
with open('output.txt', 'r') as file:
    # Read all lines, strip whitespace/newlines, and join them by commas
    ports = ','.join([line.strip() for line in file])

# Write the comma-separated ports to a new file (ports.txt)
with open('ports.txt', 'w') as output_file:
    output_file.write(ports)
