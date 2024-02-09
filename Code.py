import csv

# Define ad groups based on product categories for more targeted advertising
ad_groups = {
    'Cakes': ['birthday cakes', 'wedding cakes', 'custom cakes'],
    'Breads': ['gluten-free bread', 'artisan bread', 'whole wheat bread'],
    'Pastries': ['croissants', 'muffins', 'scones', 'danishes'],
    'Special Offers': ['discount', 'special offer']
}

# Define your list of keyword modifiers
modifiers = ['buy', 'order', 'delivery', 'near me', 'online', 'best', 'reviews']

# Define negative keywords
negative_keywords = ['free', 'how to make', 'recipe']

# Function to generate keywords for each ad group with match types
def generate_keywords_for_ad_groups(ad_groups, modifiers):
    keywords = []
    for ad_group, products in ad_groups.items():
        for product in products:
            for modifier in modifiers:
                # Generate keywords in different match types
                broad = f"{modifier} {product}"
                phrase = f"\"{modifier} {product}\""
                exact = f"[{modifier} {product}]"
                keywords.extend([(broad, "Broad", ad_group), (phrase, "Phrase", ad_group), (exact, "Exact", ad_group)])
    return keywords

# Generate keywords with ad groups
keywords_with_ad_groups = generate_keywords_for_ad_groups(ad_groups, modifiers)

# Path for the CSV file, adjusted to your specified path
csv_file_path = '/Users/vj/Downloads/bakery_keywords.csv'

# Output keywords with ad groups to CSV, corrected function name to match your setup
def output_keywords_with_ad_groups_to_csv(keywords, negative_keywords, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Keyword", "Match Type", "Campaign", "Ad Group"])
        # Write keywords
        for keyword, match_type, ad_group in keywords:
            writer.writerow([keyword, match_type, "BakeryCampaign", ad_group])
        # Write negative keywords at the end, associated with all ad groups
        for ad_group in ad_groups.keys():
            for negative in negative_keywords:
                writer.writerow([negative, "Negative", "BakeryCampaign", ad_group])

# Call the function to output the keywords
output_keywords_with_ad_groups_to_csv(keywords_with_ad_groups, negative_keywords, csv_file_path)

print("Keywords have been generated and saved to:", csv_file_path)
