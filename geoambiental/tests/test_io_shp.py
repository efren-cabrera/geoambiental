import geopandas as gp
from geoambiental import import_coast_line, multi2single


def test_import_coast_line():
    file_path = "geoambiental/tests/data/linea_costa_isla_guadalupe.shp"
    import_coast_line(file_path)


def test_multi2single():
    path = "geoambiental/tests/data/linea_costa_isla_guadalupe.shp"
    poligonos = gp.read_file(path)
    projection = "epsg:4484"
    poligonos.crs = {"init": projection}
    poligonos_geograficas = poligonos.to_crs({"init": "epsg:4326"})
    poligonos_geograficas = multi2single(poligonos_geograficas)
