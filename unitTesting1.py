#unite test case for three stirng methods
import unittest #importing class library

#creating a class
#this is where the unit test goes for testing the function
#passing the class library
class TestStringMethods(unittest.TestCase): 

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		#this is what is going to be tested
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):

		#create a string variable
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])

		#chech tht s.split fail when the seperator is not a string

		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
	unittest.main() #calliing the main function to make sure that the unit test runs appropriately. 