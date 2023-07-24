# Image Commodity Searcher

[![License Badge](https://img.shields.io/github/license/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/kevin19930919/ImageCommoditySearcher)](https://github.com/kevin19930919/ImageCommoditySearcher/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Image Commodity Searcher is a Python codebase that allows users to search for commodities based on images. It utilizes image captioning and keyword generation techniques to provide accurate and relevant search results. The codebase consists of several modules and functions that handle image processing, caption generation, keyword generation, and integration with external APIs.

## Functionalities

- Image caption generation: Given an input image, the codebase can generate a descriptive caption for the image using a pre-trained image captioning model.
- Keyword generation: The codebase can convert the generated image caption into a set of keywords that can be used for searching commodities online.
- Translation: The codebase can translate the generated keywords into Traditional Chinese, making it suitable for users who prefer to search for commodities in Chinese.

## Installation

To install Image Commodity Searcher, follow these steps:

1. Clone the GitHub repository:

   ```
   git clone https://github.com/kevin19930919/ImageCommoditySearcher.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Dependencies

The codebase has the following dependencies:

- PIL (Python Imaging Library): Used for image processing and manipulation.
- line-bot-sdk: Used for integrating with the LINE Messaging API.
- transformers: Used for the image captioning model and keyword generation.
- torch: Required by the transformers library for GPU acceleration.

## Usage

To use Image Commodity Searcher, follow these steps:

1. Import the necessary modules and classes:

   ```python
   from PIL import Image
   from image_commodity_searcher.image_caption import ImageCaptionHandler
   from image_commodity_searcher.keyword_generator import KeywordGenerator
   from linebot import LineBotApi, WebhookHandler
   from linebot.models import *
   import os
   import configparser
   from util.keyword_parser import parse
   ```

2. Initialize the LineBotApi and WebhookHandler objects with the appropriate channel access token and channel secret:

   ```python
   secrets = configparser.ConfigParser()
   secrets.read('secret.ini')
   CHANNEL_SECRET = secrets['DEFAULT']['CHANNEL_SECRET']
   CHANNEL_ACCESS_TOKEN = secrets['DEFAULT']['CHANNEL_ACCESS_TOKEN']

   line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
   handler = WebhookHandler(CHANNEL_SECRET)
   ```

3. Create an instance of the ImageCaptionHandler class:

   ```python
   image_caption_handler = ImageCaptionHandler()
   ```

4. Load an image and generate a caption for it:

   ```python
   image = Image.open('image.jpg')
   caption = image_caption_handler.generate_caption(image)
   ```

5. Create an instance of the KeywordGenerator class:

   ```python
   OPENAI_API_KEY = secrets['DEFAULT']['OPENAI_API_KEY']
   keyword_generator = KeywordGenerator(key=OPENAI_API_KEY)
   ```

6. Generate keywords from the caption:

   ```python
   keywords = keyword_generator.generate(caption)
   ```

7. Parse the generated keywords:

   ```python
   result = parse(keywords)
   ```

## Authors

The Image Commodity Searcher codebase is maintained by Kevin Chen.

## Contributing

Contributions to the Image Commodity Searcher codebase are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

To contribute code changes, follow these steps:

1. Fork the GitHub repository.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Push your branch to your forked repository.
5. Open a pull request on the GitHub repository.

## Support

If you need support or have any questions, please contact Kevin Chen at [email protected]

## Commercial Support

For commercial support inquiries, please contact Kevin Chen at [email protected]

## License

Image Commodity Searcher is licensed under the [MIT License](https://github.com/kevin19930919/ImageCommoditySearcher/blob/main/LICENSE).