import random

quotes =[
    ['The only way to do great work is to love what you do.','- Steve Jobs'],
    ['Success is stumbling from failure to failure with no loss of enthusiasm.','- Winston Churchill'],
    ['Believe you can and you\'re halfway there.','- Theodore Roosevelt']
    # ['',''],
]
randomQuote=random.randint(0,len(quotes)-1)

def get_quote():
    return quotes[randomQuote][0],quotes[randomQuote][1]