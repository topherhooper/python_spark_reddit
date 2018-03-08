from reddit_main import SubReddit, subreddit_top_submission_nsj
from spark_main import SparkContext, nsj_to_df


def test_reddit():
    sr = SubReddit()
    sr.set_praw()
    sr.set_subreddit(subreddit_name='WritingPrompts')
    for sub in sr.top_submissions(n=10):
        print sub.get['title']
        # print "Title", sub.title
        # print "Score", sub.score
        # print "Subtext", sub.selftext
        break

def test_spark():
    subreddit = 'Space'
    fields = ['title']
    sc = SparkContext("local", "Simple App")
    data = subreddit_top_submission_nsj(subreddit, fields)
    ll_data = nsj_to_df(nsj=data, sc=sc)

    # https://stackoverflow.com/questions/39880269/pyspark-typeerror-condition-should-be-string-or-column
    # https://stackoverflow.com/questions/14290857/sql-select-where-field-contains-words
    a_rows = ll_data.filter("title LIKE '%a%'").count()
    b_rows = ll_data.filter("title LIKE '%b%'").count()

    print "Lines with a: %i, lines with b: %i" % (a_rows, b_rows)


if __name__ == '__main__':
    test_spark()
