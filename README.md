# Ella: Customized Web3 Bot Assistant

Introducing Ella! This Python program utilizes the Langchain library to index personal data, including PDFs, for creating a personalized bot assistant. Additionally, it offers cryptocurrency tracking functionality.

## How to Use

### Chat Assistant

- To interact with the chat assistant, run `chat.py`.
- Ella leverages the Langchain LLM to index your personal data by referencing the information it has extracted from your PDFs.
- You can ask questions related to your indexed personal data, initiate engaging conversations, and even reset the conversation history to start fresh.
- Ella can also provide cryptocurrency-related information. You can check cryptocurrency prices by typing "check crypto" or launch pre-built smart contract templates by typing "new contract."

### Cryptocurrency Tracker

- The `crypto_tracker.py` module allows you to track cryptocurrency prices.
- It currently supports tracking for the following cryptocurrencies: BTC, ETH, DOT, AXS, MATIC, GALA, ALU, PBR, UFO, SHIB, ARB, DERC, FTM, LTC, and PHA. (Feel free to customize)

### Smart Contract Generator

- The `smart_contract_generator.py` script enables you to generate smart contract templates.
- You can choose from different contract types, including ERC20, ERC721, and ERC1155.
- The templates are designed to be edited in Visual Studio Code.

## Data Indexing

The Langchain library is used to index personal data, including PDFs, stored in the program's 'data' folder. The indexing process makes it easier for Ella to retrieve relevant information from these documents.

To update the data index with new PDFs, run `create_index.py`. This script will add new PDFs to the program's indexed data.

## Configuration

Before running the chat assistant, make sure to set your OpenAI API key in your environment variables.

## Required Build Tools

All required build tools, including OpenZeppelin smart contracts, can be found in the `requirements.txt` file. You can install these dependencies using `pip install -r requirements.txt`.

## Known Issues

While Ella is a powerful tool, it's important to be aware of a specific behavior. The Langchain LLM is currently capable of interacting with just one indexed PDF at a time. When you attempt to engage with data from a different PDF in your data directory, the bot may respond that it has no access to this information.

To address this limitation, we've implemented a reset feature. Simply type 'reset,' hit enter, and Ella will refresh the chat, allowing Langchain to interact with other PDFs. This feature ensures a seamless experience when working with multiple PDFs in your data directory.

Your feedback and contributions are highly valued as we work towards refining and enhancing Ella's capabilities!

## Contributing

Feel free to contribute to this project. If you have ideas for improvements or want to help expand the functionality, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Enjoy!


