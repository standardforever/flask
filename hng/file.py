import csv
import json
from hashlib import sha256


def split_string(attributes=""):
    new_lis = []
    count = 0
    attributes = attributes.strip(";")
    lis = attributes.split(';')
    for index in lis:
        new_dict = {}
        liss = index.split(':')
        new_dict["trait_type"] = liss[0].strip(" ")
        new_dict["value"] = liss[1].strip(" ")
        
        new_lis.append(new_dict)
        del new_dict
    return (new_lis)

def csv_to_json(csv_file_path):
    new_lis = []
    """Csv Field names"""
    field_names = ['TEAM NAMES', 'Series Number' ,'Filename',
            'Name', 'Description', 'Gender', 'Attributes', 'UUID', 'HASH']
    """Create a dictionary"""
    data_dict = {
        "format": "CHIP-0007",
        "name": "defualt",
        "description": "defualt",
        "minting_tool": "SuperMinter/2.5.2",
        "sensitive_content": False,
        "series_number": 0,
        "series_total": 420,
        "attribute": [],
        "collection": {
            "name": "Zuri NFT Tickets for Free Lunch",
            "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
            "attributes": [
                {
                "type": "description",
                "value": "Rewards for accomplishments during HNGi9."
                }
            ]
        },
    }

    """Open a csv file handler"""
    with open(csv_file_path, encoding= 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)

        """
        Convert each row into a CHIP-007 JSON,
        Use the generated CHIP-OO7 to create a HASH,
        Append the HASH into a new row
        """

        for row in csv_reader:
            data_dict["name"] = row["Name"]
            data_dict["description"] = row["Description"]
            data_dict["series_number"] = int(row["Series Number"])
            data_dict["attribute"] = split_string(row["Attributes"])
            encode = json.dumps(data_dict, sort_keys=True).encode('utf-8')
            encode = sha256(encode).hexdigest()
            row["HASH"] = encode
            new_lis.append(row)
    with open("filename.output.csv", 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(new_lis)

if __name__ == "__main__":
    csv_to_json('./csv/hng.csv')
