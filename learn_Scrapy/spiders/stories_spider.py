import scrapy

class StoriesSpider(scrapy.Spider):
  name = "stories"

  start_urls = [
     # urls that you want to crawl
      'https://9jatechguru.com.ng/category/smartphone',
      'https://9jatechguru.com.ng/category/technology',
  ]

# For All Stories
  def parse(self, response):
    # Replace 'path' with the right css path that the data located
    for story in response.css('path'):
      yield {
          # Things you need to crawl
          'articleTitle': story.css('.entry-title::text').extract(),
          'articleLink': story.css('.entry-title a::attr(href)').extract(),
          'postingDate': story.css('.date').extract(),
      }