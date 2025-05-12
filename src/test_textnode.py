import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("Hello", TextType.ITALIC)
        node2 = TextNode("World", TextType.ITALIC)

        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("Hello", TextType.ITALIC)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Hello", TextType.ITALIC, "www")
        node2 = TextNode("Hello", TextType.ITALIC, "ddd")
        self.assertNotEqual(node, node2)
if __name__ == "__main__":
    unittest.main()
