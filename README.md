# target-spider
A web crawler developed using the scrapy framework and it does the following :
- Crawl the given URL
- Extract the product information

# Usage
- Clone the repository
- Traverse to directory <b><i> 'path_to_your_machine/' </i></b>
- Activate the virtual enviornment or use  <b><i> 'source scrapy_env/bin/activate'</i></b>
- Run the crawler : <b><i> scrapy crawl targetspider -a url="your_choice_url" </i></b>
  - Example - Run below command to your shell / terminal <hr>
   <i> scrapy crawl targetspider -a url="https://www.target.com/p/toddler-girls-shanel-fisherman-sandals-cat-jack/-/A-81204099?preselect=80859208" -o output.json </i>
