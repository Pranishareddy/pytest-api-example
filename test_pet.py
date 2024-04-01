from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    # TODO...

    assert response.status_code == 200

    for i in response.json():
        # Validate the response schema against the defined schema in schemas.py
        validate(i, schema=schemas.pet)

        assert i['status'] == 'available'

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("pet_id, code", [(3, 404), (4, 404), (5, 404),(6, 404),(7, 404),(8, 404), (9, 404)])
def test_get_by_id_404(pet_id, code):
    # TODO...

    test_endpoint = f"/pets/{pet_id}"
    params = {
        "pet_id": pet_id
    }

    response = api_helpers.get_api_data(test_endpoint, params)

    assert response.status_code == code


@pytest.mark.parametrize("pet_id, code", [(0, 200), (1, 200), (2, 200)])
def test_get_by_id_200(pet_id, code):
    # TODO...

    test_endpoint = f"/pets/{pet_id}"
    params = {
        "pet_id": pet_id
    }

    response = api_helpers.get_api_data(test_endpoint, params)

    assert response.status_code == code