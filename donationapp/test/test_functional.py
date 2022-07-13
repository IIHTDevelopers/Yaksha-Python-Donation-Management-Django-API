#python manage.py test donationapp.test.test_functional
from rest_framework.test import APITestCase
from donationapp.models import NGOModel,DonorModel,DonationModel,DonationRequestModel
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NGOModel.objects.create(
        ngo_id= 1,
        ngo_name= "Ngo1",
        username="ngouser1",
        password= "ngopwd1",
        address= "#301,Plaza estate ,Hyderabad",
        phone_number= 9934567845,
        started_in= "2020-09-09",
        documents= "sample documents"
        )

        obj=DonorModel.objects.create(
        donar_id= 1,
        ngo_id= 1,
        donar_name= "Donar1",
        username= "donaruser1",
        password= "donarpwd1",
        email_id= "donar@gmail.com",
        phone_number= 98856498648,
        address= "Tirupathi")

        DonationModel.objects.create(
        donation_id= 1,
        donar_id=1,
        ngo_id= 1,
        donation_type= "Type1",
        amount= "10000.00",
        donation_date= "2022-04-13"
        )

        DonationRequestModel.objects.create(
        request_id= 1,
        amount= "25000.00",
        donar_id= 1,
        ngo_id= 1,
        donation_end_date= "2022-06-20"
        )

#NGO

    def test_get_all_ngo(self):
        url='http://127.0.0.1:8000/ngo/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllNgos", True, "functional")
            print("TestGetAllNgos = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllNgos", False, "functional")
            print("TestGetAllNgos = Failed")
    def test_get_single_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetSingleNgo", True, "functional")
            print("TestGetSingleNgo = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleNgo", False, "functional")
            print("TestGetSingleNgo = Failed")

    def test_post_ngo(self):
        url='http://127.0.0.1:8000/ngo/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567845,
        "started_in": "2020-09-09",
        "documents": "sample documents"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostNgo", True, "functional")
            print("TestPostNgo = Passed")
        else:
            test_obj.yakshaAssert("TestPostNgo", False, "functional")
            print("TestPostNgo = Failed")

    def test_update_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567840,
        "started_in": "2020-09-09",
        "documents": "sample documents"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TesUpdateNgo", True, "functional")
            print("TesUpdateNgo = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateNgo", False, "functional")
            print("TesUpdateNgo = Failed")

    def test_delete_ngo(self):
        url='http://127.0.0.1:8000/ngo_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteNgo", True, "functional")
            print("TestDeleteNgo = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteNgo", False, "functional")
            print("TestDeleteNgo = Failed")

#Donar

    def test_get_all_donar(self):
        url='http://127.0.0.1:8000/donar/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllDonar", True, "functional")
            print("TestGetAllDonar = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDonar", False, "functional")
            print("TestGetAllDonar = Failed")

    def test_get_single_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetSingleDonar", True, "functional")
            print("TestGetSingleDonar = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleDonar", False, "functional")
            print("TestGetSingleDonar = Failed")

    def test_post_donar(self):
        url='http://127.0.0.1:8000/donar/'
        data= {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@gmail.com",
        "phone_number": 98856498648,
        "address": "Tirupathi"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostDonar", True, "functional")
            print("TestPostDonar = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonar", False, "functional")
            print("TestPostDonar = Failed")

    def test_update_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        data=  {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@yahoo.com",
        "phone_number": 98856498640,
        "address": "Tirupathi"
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TesUpdateDonar", True, "functional")
            print("TesUpdateDonar = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateDonar", False, "functional")
            print("TesUpdateDonar = Failed")

    def test_delete_donar(self):
        url='http://127.0.0.1:8000/donar_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteDonar", True, "functional")
            print("TestDeleteDonar = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDonar", False, "functional")
            print("TestDeleteDonar = Failed")

    def test_get_donar_by_ngo(self):
        url='http://127.0.0.1:8000/donar_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDonarByNgo", True, "functional")
            print("TestGetDonarByNgo = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonarByNgo", False, "functional")
            print("TestGetDonarByNgo = Failed")

#Donation

    def test_get_all_donation(self):
        url='http://127.0.0.1:8000/donation/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetAllDonation", True, "functional")
            print("TestGetAllDonation = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDonation", False, "functional")
            print("TestGetAllDonation = Failed")
    def test_get_single_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetSingleDonation", True, "functional")
            print("TestGetSingleDonation = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleDonation", False, "functional")
            print("TestGetSingleNgo = Failed")

    def test_post_donation(self):
        url='http://127.0.0.1:8000/donation/'
        data= {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "10000.00",
        "donation_date": "2022-04-13",
        "donar_id": 1
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostDonation", True, "functional")
            print("TestPostDonation = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonation", False, "functional")
            print("TestPostDonation = Failed")

    def test_update_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        data=     {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "11000.00",
        "donation_date": "2022-04-13",
        "donar_id": 1
        }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TesUpdateDonation", True, "functional")
            print("TesUpdateDonation = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateDonation", False, "functional")
            print("TesUpdateDonation = Failed")

    def test_delete_donation(self):
        url='http://127.0.0.1:8000/donation_pk/1/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteDonation", True, "functional")
            print("TestDeleteDonation = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDonation", False, "functional")
            print("TestDeleteDonation = Failed")

    def test_get_donation_by_donar(self):
        url='http://127.0.0.1:8000/donation_donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDonationByDonar", True, "functional")
            print("TestGetDonationByDonar = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationByDonar", False, "functional")
            print("TestGetDonationByDonar = Failed")

    def test_get_donation_by_ngo(self):
        url='http://127.0.0.1:8000/donation_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDonationByNgo", True, "functional")
            print("TestGetDonationByNgo = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationByNgo", False, "functional")
            print("TestGetDonationByNgo = Failed")


#DonationRequest

    def test_post_donation_request(self):
        url='http://127.0.0.1:8000/donation_request/'
        data=     {
        "request_id": 1,
        "amount": "25000.00",
        "donar_id": 1,
        "ngo_id": 1,
        "donation_end_date": "2022-06-20"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostDonationRequest", True, "functional")
            print("TestPostDonationRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonationRequest", False, "functional")
            print("TestPostDonationRequest = Failed")

    def test_get_donation_request_by_donar(self):
        url='http://127.0.0.1:8000/donation_request_donar_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDonationRequestByDonar", True, "functional")
            print("TestGetDonationRequestByDonar = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationRequestByDonar", False, "functional")
            print("TestGetDonationRequestByDonar = Failed")

    def test_get_donation_request_by_ngo(self):
        url='http://127.0.0.1:8000/donation_request_ngo_pk/1/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetDonationRequestByNgo", True, "functional")
            print("TestGetDonationRequestByNgo = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationRequestByNgo", False, "functional")
            print("TestGetDonationRequestByNgo = Failed")
