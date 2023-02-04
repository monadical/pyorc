from click.testing import CliRunner
from pyorc.cli.main import cli
from pyorc.cli.cli_elements import GcpSelect, AoiSelect
from pyorc.helpers import xyz_transform
import json

def test_cli_cam_config(cli_obj):
    result = cli_obj.invoke(
        cli, [
            'camera-config',
            '--help'
        ],
        echo=True
    )
    assert result.exit_code == 0


def test_cli_cam_config_video(cli_obj, vid_file, gcps_src, gcps_fn, lens_position, corners, cli_cam_config_output):
    result = cli_obj.invoke(
        cli, [
            'camera-config',
            '-V',
            vid_file,
            '--src',
            json.dumps(gcps_src),
            '--dst',
            json.dumps(gcps_dst),
            '--crs',
            '32735',
            '--z0',
            '1182.2',
            '--href',
            '0.0',
            '--lens_position',
            json.dumps(lens_position),
            '--resolution',
            '0.03',
            '--window_size',
            '25',
            '--corners',
            json.dumps(corners),
            '--shapefile',
            gcps_fn,
            '-vvv',
            cli_cam_config_output,

        ],
        echo=True
    )
    # assert result.exit_code == 0

def test_cli_velocimetry(cli_obj, vid_file, cam_config_fn, cli_recipe_fn, cli_output_dir):
    result = cli_obj.invoke(
        cli, [
            'velocimetry',
            '-V',
            vid_file,
            '-c',
            cam_config_fn,
            '-r',
            cli_recipe_fn,
            '-vvv',
            cli_output_dir,
            '-u'
        ],
        echo=True
    )
    assert result.exit_code == 0


def test_service_video(velocity_flow_processor):
    raise NotImplementedError


def test_gcps_interact(gcps_dst, frame_rgb):
    import matplotlib.pyplot as plt
    # convert dst to
    crs = 32735
    # crs = None
    if crs is not None:
        dst = xyz_transform(gcps_dst, crs_from=crs, crs_to=4326)
    else:
        dst = gcps_dst
    selector = GcpSelect(frame_rgb, dst, crs=crs)
    # uncomment below to test the interaction, not suitable for automated unit test
    # plt.show(block=True)


def test_aoi_interact(frame_rgb, cam_config_without_aoi):
    import matplotlib.pyplot as plt
    # convert dst to
    # del cam_config_without_aoi.crs
    src = cam_config_without_aoi.gcps["src"]
    if hasattr(cam_config_without_aoi, "crs"):
        dst = xyz_transform(cam_config_without_aoi.gcps["dst"], crs_from=cam_config_without_aoi.crs, crs_to=4326)
    else:
        dst = cam_config_without_aoi.gcps["dst"]
    selector = AoiSelect(frame_rgb, src, dst, cam_config_without_aoi)
    # uncomment below to test the interaction, not suitable for automated unit test
    # plt.show(block=True)
