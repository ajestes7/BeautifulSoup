from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unittest

def getSumSpans(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('span')

    numSum = 0

    for link in tags:
        for character in link:
                numSum += int(character)

    return numSum

def followLinks(url, numAnchor, numTimes):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    for num in range(numTimes):
        html = urlopen(url, context = ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        c_name = soup.find_all('a')
        newName = c_name[numAnchor-1]
        url = newName.get('href')
    name = newName.text
    return name

def getGradeHistogram(url):
    """ return a sorted tuple with the grade range (such as 90, 80, etc) and the number of grades in that range
        url -- a uniform resource locator - address for a web page
    """

    pass


class TestHW7(unittest.TestCase):

    def test_sumSpan1(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_42.html"), 2553)

    def test_sumSpan2(self):
        self.assertEqual(getSumSpans("http://py4e-data.dr-chuck.net/comments_132199.html"), 2714)

    def test_followLinks1(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Fikret.html",3,4), "Anayah")

    def test_followLinks2(self):
        self.assertEqual(followLinks("http://py4e-data.dr-chuck.net/known_by_Charlie.html",18,7), "Shannah")

    #def test_getGradeHistogram(self):
    #    self.assertEqual(getGradeHistogram("http://py4e-data.dr-chuck.net/comments_42.html"), [(90, 4), (80, 4), (70, 7), (60, 7), (50, 6), (40, 3), (30, 5), (20, 4), (10, 6), (0, 4)])


unittest.main(verbosity=2)
