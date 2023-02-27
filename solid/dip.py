class NewsPaper:
    """This is a low-level module"""

    def publish(self, news):
        return f"{news} news paper"


class Facebook:
    """This is a low-level module"""

    def publish(self, news):
        return f"{news} - share this post on {news}"


class NewsPerson:
    """This is a high-level module"""

    def publish(self, news, publisher=None):
        print(publisher.publish(news))


if __name__ == "__main__":
    person = NewsPerson()
    person.publish("hello", NewsPaper())
    person.publish("facebook", Facebook())
