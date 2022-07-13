#python manage.py test donationapp.test.test_exceptional
from rest_framework.test import APITestCase
from donationapp.models import NGOModel,DonorModel,DonationModel,DonationRequestModel
from donationapp.test.TestUtils import TestUtils
class DonationManagementAPIExceptionalTest(APITestCase):
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

    def test_get_all_ngo_error(self):
        url='http://127.0.0.1:8000/ngox/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("TestGetAllNgosError", True, "exception")
            print("TestGetAllNgosError = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllNgosError", False, "exception")
            print("TestGetAllNgosError = Failed")
    def test_get_single_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetSingleNgoError", True, "exception")
            print("TestGetSingleNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleNgoError", False, "exception")
            print("TestGetSingleNgoError = Failed")

    def test_post_ngo_error(self):
        url='http://127.0.0.1:8000/ngo/'
        data= {
        "ngo_id": 1,
        "ngo_name": "Ngo1",
        "username": "ngouser1",
        "password": "ngopwd1",
        "address": "#301,Plaza estate\r\nHyderabad",
        "phone_number": 9934567845,
        # "started_in": "2020-09-09",
        # "documents": "sample documents"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostNgoError", True, "exception")
            print("TestPostNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestPostNgoError", False, "exception")
            print("TestPostNgoError = Failed")

    def test_update_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("TesUpdateNgoError", True, "exception")
            print("TesUpdateNgoError = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateNgoError", False, "exception")
            print("TesUpdateNgoError = Failed")

    def test_delete_ngo_error(self):
        url='http://127.0.0.1:8000/ngo_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteNgoError", True, "exception")
            print("TestDeleteNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteNgoError", False, "exception")
            print("TestDeleteNgoError = Failed")

#Donar

    def test_get_all_donar_error(self):
        url='http://127.0.0.1:8000/donarx/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("TestGetAllDonarError", True, "exception")
            print("TestGetAllDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDonarError", False, "exception")
            print("TestGetAllDonarError = Failed")

    def test_get_single_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetSingleDonarError", True, "exception")
            print("TestGetSingleDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleDonarError", False, "exception")
            print("TestGetSingleDonarError = Failed")

    def test_post_donar_error(self):
        url='http://127.0.0.1:8000/donar/'
        data= {
        "donar_id": 1,
        "ngo_id": 1,
        "donar_name": "Donar1",
        "username": "donaruser1",
        "password": "donarpwd1",
        "email_id": "donar@gmail.com",
        # "phone_number": 98856498648,
        # "address": "Tirupathi"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostDonarError", True, "exception")
            print("TestPostDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonarError", False, "exception")
            print("TestPostDonarError = Failed")

    def test_update_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("TesUpdateDonarError", True, "exception")
            print("TesUpdateDonarError = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateDonarError", False, "exception")
            print("TesUpdateDonarError = Failed")

    def test_delete_donar_error(self):
        url='http://127.0.0.1:8000/donar_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteDonarError", True, "exception")
            print("TestDeleteDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDonarError", False, "exception")
            print("TestDeleteDonarError = Failed")

    def test_get_donar_by_ngo_error(self):
        url='http://127.0.0.1:8000/donar_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDonarByNgoError", True, "exception")
            print("TestGetDonarByNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonarByNgoError", False, "exception")
            print("TestGetDonarByNgoError = Failed")

#Donation

    def test_get_all_donation_error(self):
        url='http://127.0.0.1:8000/donationx/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("TestGetAllDonationError", True, "exception")
            print("TestGetAllDonationError = Passed")
        else:
            test_obj.yakshaAssert("TestGetAllDonationError", False, "exception")
            print("TestGetAllDonationError = Failed")
    def test_get_single_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetSingleDonationError", True, "exception")
            print("TestGetSingleDonationError = Passed")
        else:
            test_obj.yakshaAssert("TestGetSingleDonationError", False, "exception")
            print("TestGetSingleNgoError = Failed")

    def test_post_donation_error(self):
        url='http://127.0.0.1:8000/donation/'
        data= {
        "donation_id": 1,
        "ngo_id": 1,
        "donation_type": "Type1",
        "amount": "10000.00",
        # "donation_date": "2022-04-13",
        # "donar_id": 1
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostDonationError", True, "exception")
            print("TestPostDonationError = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonationError", False, "exception")
            print("TestPostDonationError = Failed")

    def test_update_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
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
        if response.status_code==500:
            test_obj.yakshaAssert("TesUpdateDonationError", True, "exception")
            print("TesUpdateDonationError = Passed")
        else:
            test_obj.yakshaAssert("TesUpdateDonationError", False, "exception")
            print("TesUpdateDonationError = Failed")

    def test_delete_donation_error(self):
        url='http://127.0.0.1:8000/donation_pk/111/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestDeleteDonationError", True, "exception")
            print("TestDeleteDonationError = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteDonationError", False, "exception")
            print("TestDeleteDonationError = Failed")

    def test_get_donation_by_donar_error(self):
        url='http://127.0.0.1:8000/donation_donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDonationByDonarError", True, "exception")
            print("TestGetDonationByDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationByDonarError", False, "exception")
            print("TestGetDonationByDonarError = Failed")

    def test_get_donation_by_ngo_error(self):
        url='http://127.0.0.1:8000/donation_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDonationByNgoError", True, "exception")
            print("TestGetDonationByNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationByNgoError", False, "exception")
            print("TestGetDonationByNgoError = Failed")


#DonationRequest

    def test_post_donation_request_error(self):
        url='http://127.0.0.1:8000/donation_request/'
        data=     {
        "request_id": 1,
        "amount": "25000.00",
        "donar_id": 1,
        # "ngo_id": 1,
        # "donation_end_date": "2022-06-20"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPostDonationRequestError", True, "exception")
            print("TestPostDonationRequestError = Passed")
        else:
            test_obj.yakshaAssert("TestPostDonationRequestError", False, "exception")
            print("TestPostDonationRequestError = Failed")

    def test_get_donation_request_by_donar_error(self):
        url='http://127.0.0.1:8000/donation_request_donar_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDonationRequestByDonarError", True, "exception")
            print("TestGetDonationRequestByDonarError = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationRequestByDonarError", False, "exception")
            print("TestGetDonationRequestByDonarError = Failed")

    def test_get_donation_request_by_ngo_error(self):
        url='http://127.0.0.1:8000/donation_request_ngo_pk/111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestGetDonationRequestByNgoError", True, "exception")
            print("TestGetDonationRequestByNgoError = Passed")
        else:
            test_obj.yakshaAssert("TestGetDonationRequestByNgoError", False, "exception")
            print("TestGetDonationRequestByNgoError = Failed")
