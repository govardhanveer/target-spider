# target-spider
A web crawler developed using the scrapy framework and it does the following :
- Crawl the given URL
- Extract the product information

# Usage
- Clone the repository : `git clone https://github.com/govardhanveer/target-spider.git` 
- Traverse to directory : `cd path_to_your_spider_location/scrapy_test` 
- Activate the virtual enviornment using below command :  
  ```source scrapy_env/bin/activate```
- Run the crawler : ```scrapy crawl targetspider -a url="your_choice_url"```
  - Example - Run below command to your shell / terminal and store extarcted information to `file_name.json`
   ```
   scrapy crawl targetspider -a url="https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208" -o output.json
   ```
- File name `output.json` contains the extracted fields & its associated data
- Sample output <b><i> without using selenium </i></b>
  ```javascript
    {
      "url": "https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208",
      "response_url": "https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208",
      "title": "Toddler Girls' Shanel Fisherman Sandals - Cat & Jack\u2122",
      "tcin": "80859208",
      "upc": "0829576374731",
      "price": null,
      "currency": "USD",
      "description": "She'll be ready for fun in the sun whenever she sports the Shanel Fisherman Sandals from Cat & Jack\u2122. These strappy sandals feature an open design to keep her feet cool and comfy on warm, sunny days, and they're easy to dress up or down thanks to the classic straps of the fisherman-style design. A back sling strap helps provide a firm fit that stays put on her feet as she moves, while the buckle accent conceals a hook-and-loop fastener that makes for adjustable wear as well as making on and off easy.",
      "specs": {
        "Size": "6",
        "Sizing": "Toddler",
        "Care and Cleaning": "Care Instructions Not Provided",
        "Lining Material": "Man Made Materials",
        "Insole Material": "Man Made Materials",
        "Features": "Quarter Strap, Hook and Loop Closure, Open Toe",
        "Upper Shoe Material": "100% Plastic",
        "Sole Material": "100% TPR (Thermoplastic Rubber)",
        "Heel": "Approximately 0.5 Inches No Heel",
        "Shoe Width": "Medium",
        "Footwear outsole details": "Non Marking Outsole"
      }
    }```
- Sample output <b><i> using selenium </i></b>
```javascript
  {
  'url': 'https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208',
  'tcin': '80859208',
  'upc': '0829576374731',
  'og_price': '$16.99',
  'price': '16.99',
  'currency': 'USD',
  'title': "Toddler Girls' Shanel Fisherman Sandals - Cat & Jack™",
  'description': "She'll be ready for fun in the sun whenever she sports the Shanel Fisherman Sandals from Cat & Jack™. These strappy sandals feature an open design to keep her feet cool and comfy on warm, sunny days, and they're easy to dress up or down thanks to the classic straps of the fisherman-style design. A back sling strap helps provide a firm fit that stays put on her feet as she moves, while the buckle accent conceals a hook-and-loop fastener that makes for adjustable wear as well as making on and off easy.",
  'specs': {
    'Size': '6',
    'Sizing': 'Toddler',
    'Care and Cleaning': 'Care Instructions Not Provided',
    'Lining Material': 'Man Made Materials',
    'Insole Material': 'Man Made Materials',
    'Features': 'Quarter Strap, Hook and Loop Closure, Open Toe',
    'Upper Shoe Material': '100% Plastic',
    'Sole Material': '100% TPR (Thermoplastic Rubber)',
    'Heel': 'Approximately 0.5 Inches No Heel',
    'Shoe Width': 'Medium',
    'Footwear outsole details': 'Non Marking Outsole'
    }
  }
```
