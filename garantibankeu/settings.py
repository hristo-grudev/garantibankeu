BOT_NAME = 'garantibankeu'

SPIDER_MODULES = ['garantibankeu.spiders']
NEWSPIDER_MODULE = 'garantibankeu.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'garantibankeu.pipelines.GarantibankeuPipeline': 100,

}

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
