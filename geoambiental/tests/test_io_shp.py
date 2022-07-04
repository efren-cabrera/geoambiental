from geoambiental import import_coast_line


def test_import_coast_line():
    file_path = "geoambiental/tests/data/linea_costa_isla_guadalupe.shp"
    import_coast_line(file_path)
