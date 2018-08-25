import praw

bot = praw.reddit(user_agent = 'bot', client_id = '', client_secret='', username = '', password = '')

subreddit = bot.subreddit('science')

words = subreddit.stream.comments()

for word in words:
	text = comment.body
	writer = comment.author
	if 'atom' in text.lower():
		message = "NASA will launch a cold atom"
		word.reply(message)
