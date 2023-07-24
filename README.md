# Image Commodity Searcher

[![License Badge](https://img.shields.io/github/license/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Image Commodity Searcher is a Python codebase that allows users to search for commodities based on images. It utilizes image captioning and keyword generation techniques to generate keywords from image descriptions, which can then be used to search for relevant commodities.

## Functionalities

- Generate keywords from image descriptions
- Translate keywords into Traditional Chinese
- Search for commodities based on keywords

## Installation

To install Image Commodity Searcher, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/kevin19930919/ImageCommoditySearcher.git
   ```

2. Change to the project directory:

   ```
   cd ImageCommoditySearcher
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Dependencies

The following dependencies are required to run Image Commodity Searcher:

- Python 3.7 or higher
- OpenAI
- PIL
- Flask
- line-bot-sdk
- torch
- transformers

## Usage

To use Image Commodity Searcher, follow these steps:

1. Import the necessary modules:

   ```python
   from PIL import Image
   from image_caption import ImageCaptionHandler
   from keyword_generator import KeywordGenerator
   from flask import Flask, request, abort
   from linebot import LineBotApi, WebhookHandler
   from linebot.exceptions import InvalidSignatureError
   from linebot.models import *
   import os
   import configparser
   from util.keyword_parser import parse
   ```

2. Initialize the necessary objects:

   ```python
   image = Image.open(filename)
   image_caption_handler = ImageCaptionHandler()
   keyword_generator =  KeywordGenerator(key=OPENAI_API_KEY)
   ```

3. Generate a caption for the image:

   ```python
   caption = image_caption_handler.generate_caption(image)
   ```

4. Generate keywords from the caption:

   ```python
   result = parse(keyword_generator.generate(caption))
   ```

## Authors

Image Commodity Searcher is developed and maintained by Kevin Chen.

## Contributing

Contributions to Image Commodity Searcher are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the [GitHub repository](https://github.com/kevin19930919/ImageCommoditySearcher/issues). 

To contribute code, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request on the main repository.

## Support

If you need support or have any questions, please contact Kevin Chen at [email protected]

## Commercial Support

For commercial support, please contact Kevin Chen at [email protected]

## License

Image Commodity Searcher is licensed under the [MIT License](https://github.com/kevin19930919/ImageCommoditySearcher/blob/main/LICENSE).