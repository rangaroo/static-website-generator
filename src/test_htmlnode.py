import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node = HTMLNode(props = {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_2(self):
        node = HTMLNode(props = {
    "href": "tryhackme.org",
    "target": "dashboard",
        })
        self.assertEqual(node.props_to_html(), ' href="tryhackme.org" target="dashboard"')

    def test_3(self): 
        node = HTMLNode(props = {
    "href": "tryhackme.org",
    "target": "dashboard",
        })

        self.assertNotEqual(node.props_to_html(), ' href="tryhackme.org" target=""')

class TestLeafNode(unittest.TestCase):
    def test_1(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertNotEqual(node, "<p>This is a paragraph of text.</p>")

    def test_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')

    def test_3(self):
        node = LeafNode("h1", "Hello World!", {"class": "bold, align-center, font-size-18"}).to_html()
        self.assertEqual(node, '<h1 class="bold, align-center, font-size-18">Hello World!</h1>')

class TestParentNode(unittest.TestCase):
    def test_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        self.assertEqual(node, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_2(self):
        node = ParentNode(
            "h1",
            [
                LeafNode("span", "child")
            ],
        ).to_html()
        self.assertEqual(node, "<h1><span>child</span></h1>")

if __name__ == "__main__":
    unittest.main()
