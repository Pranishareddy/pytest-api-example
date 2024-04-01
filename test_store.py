from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

testdata = [0, 2]
@pytest.mark.parametrize("pet_id", testdata)
def test_create_order_by_id(pet_id):
    test_endpoint = f"/store/order"
    params = {
        "pet_id": pet_id
    }

    response = api_helpers.post_api_data(test_endpoint, params)

    assert response.status_code == 201

    data = response.json()


    # Validate the response schema against the defined schema in schemas.py
    validate(data, schema=schemas.order)

    print("Order ID...", data['id'])
    assert data['pet_id'] == pet_id

testdata = [0, 2]
@pytest.mark.parametrize("id", testdata)
def test_patch_order_by_id(id):
    test_endpoint = f"/store/order/{id}"
    params = {
        "status": "available"
    }

    response = api_helpers.patch_api_data(test_endpoint, params)

    assert response.status_code == 404


