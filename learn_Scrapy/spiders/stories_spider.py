import scrapy

class StoriesSpider(scrapy.Spider):
  name = "stories"

  start_urls = [
     # urls that you want to crawl
      'https://9jatechguru.com.ng/category/smartphone',
      'https://9jatechguru.com.ng/category/technology',
      'https://9jatechguru.com.ng/category/cryptocurrency',
      'https://9jatechguru.com.ng/category/internet',
      'https://9jatechguru.com.ng/category/laptops',
      'https://9jatechguru.com.ng/category/security',
      'https://9jatechguru.com.ng/category/businesses',
      'https://9jatechguru.com.ng/category/blogging',
  ]

# For All Stories
  def parse(self, response):
    # Replace 'path' with the right css path that the data located
    for story in response.css('div.content-area'):
      yield {
          # Things you need to crawl
          'articleTitle': story.css('h2.entry-title a::text').extract_first(),
          'articleLink': story.css('h2.entry-title a::attr(href)').extract_first(),
          'postingDate': story.css('span.posted-on::text').extract_first(),
      }