import json
import base64

def decode_vmess(vmess_link):
    """Decodes a base64-encoded vmess link."""
    # Remove the "vmess://" prefix
    vmess_link = vmess_link[8:]
    
    # Decode the base64 string
    decoded_bytes = base64.urlsafe_b64decode(vmess_link + '==')
    decoded_str = decoded_bytes.decode('utf-8')
    
    # Parse the JSON string
    return json.loads(decoded_str)

def encode_vmess(vmess_dict):
    """Encodes a vmess dict into a base64-encoded vmess link."""
    # Convert the dict back to a JSON string
    json_str = json.dumps(vmess_dict, separators=(',', ':'))
    
    # Encode the JSON string as base64
    encoded_bytes = base64.urlsafe_b64encode(json_str.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    
    # Add the "vmess://" prefix
    return f"vmess://{encoded_str}"

def change_ip(vmess_link, new_ip):
    """Changes the IP address in the vmess link to a new IP."""
    vmess_dict = decode_vmess(vmess_link)
    vmess_dict['add'] = new_ip
    return encode_vmess(vmess_dict)

def main():
    input_file = "links.txt"  # Input file containing the Vmess links
    output_file = "vv"  # Output file to save the modified Vmess links
    new_ip = "34.245.87.65"  # New IP address to replace the old one

    # Read the Vmess links from the input file
    with open(input_file, "r") as file:
        vmess_links = file.read().splitlines()

    # Modify the IP address in each Vmess link
    modified_links = [change_ip(link, new_ip) for link in vmess_links]

    # Save the modified Vmess links to the output file
    with open(output_file, "w") as file:
        for link in modified_links:
            file.write(link + "\n")

    print(f"Modified Vmess links have been saved to {output_file}")

if __name__ == "__main__":
    main()
