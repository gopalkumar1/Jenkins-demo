try: 
	from run import app
	import unittest
except Exception as e:
	print("some error")
class FlaskTest(unittest.TestCase):
	# check for response 200	
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get("/fo")
		statuscode = response.status_code
		self.assertEqual(statuscode, 200)
	# checl if content return is application/json
	def test_index_content(self):
		tester = app.test_client(self)
		response = tester.get("/fo")
		self.assertEqual(response.content_type,"application/json")
		self.assertEqual(statuscode, 200)
if __name__ == "__main__":
	unittest.main()
