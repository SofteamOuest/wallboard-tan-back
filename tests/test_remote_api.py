from unittest import TestCase
from unittest.mock import patch

from widget_bus_back.bus_line import BusLine
from widget_bus_back.remote_api import RemoteApi


class TestTheoreticalScheduleResource(TestCase):

    @patch('os.getenv')
    def test_build_theoretical_schedule_url(self, mock_getenv):
        # arrange
        mock_getenv.return_value = 'http://dummy'
        api = RemoteApi()
        bus_line = BusLine('STOP', 'LINE', 42)

        # act
        url = api.build_theoretical_schedule_url(bus_line)

        # assert
        self.assertEquals(url, 'http://dummy/horairesarret.json/STOP/LINE/42')