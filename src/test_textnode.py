import unittest
from textnode import TextNode, TextType, text_node_to_html_node 


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

class TestConvertFunction(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_img(self):
        node = TextNode("This is an alt text", TextType.IMAGE, "src/img.png")
        html_node = text_node_to_html_node(node)
        print(html_node)
        print(html_node.tag)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "This is an alt text")
        self.assertEqual(html_node.props["src"], "src/img.png")

if __name__ == "__main__":
    unittest.main()
