
# Google Ads Keyword Generator for Bakery Campaigns

## Overview
This project provides an automated tool to generate targeted keywords for Google Ads campaigns specifically designed for bakeries. It streamlines the creation of ad groups and keywords, optimizing for search intents and including match types and negative keywords for improved ad targeting and efficiency.

## Features
- **Automated Keyword Generation**: Quickly generates keywords by combining product names with search intent modifiers.
- **Structured Ad Groups**: Categorizes keywords into specific ad groups for targeted advertising (Cakes, Breads, Pastries, Special Offers).
- **Match Types**: Includes broad, phrase, and exact match types for each keyword to control ad display precision.
- **Negative Keywords**: Integrates negative keywords to exclude irrelevant traffic, enhancing ad spend efficiency.
- **CSV Output**: Outputs the generated keywords into a CSV file, ready for direct import into Google Ads.

## How to Use
1. Ensure Python is installed on your system.
2. Download the script and the README file to your local machine.
3. Customize the `products`, `modifiers`, and `negative_keywords` in the script as needed for your campaign.
4. Run the script using Python to generate the CSV file.
5. Import the CSV file into your Google Ads account.

## Customization
- Modify the `products` and `modifiers` lists in the script to match your bakery's offerings and the search intents you want to target.
- Adjust the `negative_keywords` list to exclude searches that are not relevant to your business.

## Importing to Google Ads
- Navigate to the Keywords section of your Google Ads account.
- Choose the option to import keywords.
- Upload the generated CSV file and map the columns accordingly.
