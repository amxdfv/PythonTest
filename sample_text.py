import pytest

from request_logic import request_logic
from constants.constants import USER_ID, USER_DATA


class TestSample(object):

    @pytest.fixture
    def user_id(self):
        return USER_ID

    @pytest.fixture
    def user_data(self):
        return USER_DATA

    @pytest.mark.order(1)
    def test_request_get(self, user_id):
        res = request_logic.send_request_get(user_id)
        assert res['id'] == user_id
        assert res['Name'] == 'Ира'
        assert res['Age'] == 49
        assert res['Address'] == 'Тверь'
        assert res['Car'] == 'Волга'

    @pytest.mark.order(2)
    def test_request_post(self, user_data):
        res = request_logic.send_request_post(user_data)
        assert res.status_code == 200
        assert request_logic.send_request_get(res.text)['id'] == res.text
        request_logic.send_request_delete(res.text)

    @pytest.mark.order(3)
    def test_request_delete(self, user_data):
        res = request_logic.send_request_post(user_data)
        assert request_logic.send_request_delete(res.text).status_code == 200
