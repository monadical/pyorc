PIV_ATTRS = {
    "v_x": {
        "standard_name": "sea_water_x_velocity",
        "long_name": "Flow element center velocity vector, x-component",
        "units": "m s-1",
        "coordinates": "lon lat",
    },
    "v_y": {
        "standard_name": "sea_water_x_velocity",
        "long_name": "Flow element center velocity vector, x-component",
        "units": "m s-1",
        "coordinates": "lon lat",
   },
    "s2n": {
        "standard_name": "ratio",
        "long_name": "signal to noise ratio",
        "units": "",
        "coordinates": "lon lat",
    },
    "corr": {
        "standard_name": "correlation_coefficient",
        "long_name": "correlation coefficient between frames",
        "units": "",
        "coordinates": "lon lat",
    }
}
GEOGRAPHICAL_ATTRS = {
    "xs": {
        "axis": "X",
        "long_name": "x-coordinate in Cartesian system",
        "units": "m",
    },
    "ys": {
        "axis": "Y",
        "long_name": "y-coordinate in Cartesian system",
        "units": "m",
    },
    "lon": {
        "long_name": "longitude",
        "units": "degrees_east",
    },
    "lat": {
        "long_name": "latitude",
        "units": "degrees_north",
    }
}

PERSPECTIVE_ATTRS = {
    "xp": {
        "axis": "X",
        "long_name": "column in camera perspective",
        "units": "-"
    },
    "yp": {
        "axis": "Y",
        "long_name": "row in camera perspective",
        "units": "-"
    },
}

VIDEO_ARGS = {
    "fps": 25,
    "extra_args": ["-vcodec", "libx264"],
    "dpi": 120,
}

