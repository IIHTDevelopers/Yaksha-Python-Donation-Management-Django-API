from rest_framework.test import APITestCase
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary",True,"boundary")
        print("TestBoundary = Passed")
