class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine class")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._author = author
            self._magazine = magazine
            self._title = title
            #adding article to author's list of articles
            author._articles.append(self)
            #adding article to magazine's list of articles
            magazine._articles.append(self)
            #adding article to list of all articles
            Article.all.append(self)
        else:
            raise ValueError("Titles must be of type str and between 5 and 50 characters, inclusive")
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("author must be an instance of Author class")
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("magazine must be an instance of Magazine class")
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Names must be of type str and longer than 0 characters")
        # initialize list of articles by author
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        #ensuring name is not changeable after it is set
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change name after it is set")
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Names must be of type str and longer than 0 characters")
    def articles(self):
        return self._articles
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
class Magazine:
    all = []
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be string between 2 and 16 characters.")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Categories must be of type str and longer than 0 characters")
        #initialize list of articles in magazine

        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be string between 2 and 16 characters.")
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Categories must be of type str and longer than 0 characters")
    def add_article_instance(self, article):
        self._articles.append(article)
    def articles(self):
        return self._articles
    def contributors(self):
        return list(set(article.author for article in self._articles))
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            if article.author not in author_count:
                author_count[article.author] = 0
            author_count[article.author] += 1
        return [author for author, count in author_count.items() if count > 2] or None
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))