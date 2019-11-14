import re
import datetime
from os import listdir
from os.path import isfile

date_articles_regex = r"\d+\/\d+\/\d+ \{.*\}"
date_regex = r"^\d+\/\d+\/\d+"
link_regex = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]" + \
             r"[a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}" + \
             r"|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

articles_by_date = {}
files = [f for f in listdir('.') if isfile(f) and f.endswith('.md')]
for file in files:
    with open(file) as f:
        content = f.read()
        articles_by_date_read = re.findall(date_articles_regex, content, re.DOTALL)
        for article_and_date in articles_by_date_read:
            date = re.match(date_regex, article_and_date).group(0)
            articles_by_date[date] = []
            articles = re.findall(link_regex, article_and_date, re.DOTALL)
            for art in articles:
                articles_by_date[date].append(art)

print(articles_by_date)


def format_date(dt: datetime) -> str:
    """
    Given a datetime object, convert it to a string in the form of "day/month/year"
    """
    return '/'.join(list(reversed(str(dt).split('-'))))


today_date = datetime.date.today()
date_to_repetition = today_date - datetime.timedelta(days=5)
date_to_repetition_str = format_date(date_to_repetition)
print('Today is {}'.format(format_date(today_date)))
print('Date to repetition is {}\n\n'.format(date_to_repetition_str))

if date_to_repetition_str in articles_by_date.keys():
    print("Please read:\n{}".format('\n'.join(articles_by_date[date_to_repetition_str])))
else:
    print("You have no articles to read today!")
