import os

# Path to your Visual Studio Code executable
VSCODE_PATH = "code"

def launch_smart_contract_template(contract_type):
    # Define the directory where your smart contract templates are stored
    templates_directory = "smart_contracts"

    # Map contract types to their corresponding template filenames
    template_mapping = {
        "ERC20": "ERC20.sol",
        "ERC721": "ERC721.sol",
        "ERC1155": "ERC1155.sol"
    }

    if contract_type in template_mapping:
        template_filename = template_mapping[contract_type]
        template_path = os.path.join(templates_directory, template_filename)

        # Launch Visual Studio Code with the smart contract template
        os.system(f"{VSCODE_PATH} {template_path}")
        return "Smart contract template launched in Visual Studio Code. You can start editing now!"
    else:
        return "Invalid contract type. Please choose a valid contract type."

# Prompt the user to select the contract type
def prompt_contract_type():
    contract_types = ["ERC20", "ERC721", "ERC1155"]
    valid_input = False
    contract_type = ""

    print("Available contract types:")
    for i, contract in enumerate(contract_types):
        print(f"{i+1}. {contract}")

    while not valid_input:
        user_input = input("Please enter the corresponding number: ")
        if user_input.isdigit():
            index = int(user_input) - 1
            if index >= 0 and index < len(contract_types):
                contract_type = contract_types[index]
                valid_input = True
        if not valid_input:
            print("Invalid input. Please enter a valid number.")

    return contract_type.upper()

# Main entry point of the script
def main():
    contract_type = prompt_contract_type()
    response = launch_smart_contract_template(contract_type)
    print(response)

if __name__ == "__main__":
    main()
