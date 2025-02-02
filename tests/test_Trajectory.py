from datetime import datetime
import unittest

from geoambiental import Trajectory


class TestTrajectory(unittest.TestCase):
    def setUp(self):
        """
        Crea el punto con la coordenada que se utilizará en la prueba
        """
        self.fechas = [datetime(2018, 2, 15), datetime(2018, 2, 16)]
        self.trajectory = Trajectory([23.05, 22.05], [-118.25, -117.22], self.fechas)

    def test_get_dates(self):
        self.assertTrue(self.trajectory.date[0] == self.fechas[0])

    def test_get_items_(self):
        self.assertTrue(self.trajectory[0].date == self.fechas[0])
        self.assertTrue(self.trajectory[0].lon == -118.25)
        self.assertTrue(self.trajectory[0].lat == 23.05)


if __name__ == "__main__":
    unittest.main()
