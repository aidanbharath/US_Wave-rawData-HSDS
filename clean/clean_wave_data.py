"""
Clean up wave data
"""
import click
import h5py
import logging
import numpy as np
from rex import init_logger

logger = logging.getLogger(__name__)


def clean_dset(wave_h5, dset_name, fill_value=-9999):
    """
    Clean up dataset

    Parameters
    ----------
    wave_h5 : h5yp.File
        Open wave h5py.File instance
    dset_name : str
        Name of dataset to be cleaned
    fill_value : int
        Fill value that is to be replaced with np.nan
    """
    logger.info('Cleaning {}'.format(dset_name))
    ds = wave_h5[dset_name]
    data = ds[...]

    mask = data == fill_value
    mask |= np.isinf(data)
    if np.any(mask):
        logger.warning('- Replacing fill values and infs with np.nan')
        data[mask] = np.nan
        ds[...] = data


def clean_wave_h5(src, fill_value=-9999):
    """
    Cleanup wave .h5 file

    Parameters
    ----------
    src : path
        US wave .h5 file to cleanup
    fill_value : int
        Fill value that is to be replaced with np.nan
    """
    logger.info('Cleaning up data in {}'.format(src))

    with h5py.File(src, mode='a') as wave_h5:
        for dset_name in wave_h5:
            if dset_name not in ['meta', 'coordinates', 'time_index']:
                clean_dset(wave_h5, dset_name, fill_value=fill_value)


@click.command()
@click.option('--src', '-src', type=click.Path(exists=True), required=True,
              help='US wave .h5 file to cleanup')
@click.option('--fill_value', '-fill', type=int, default=-9999,
              show_default=True,
              help='Fill value that is to be replaced with np.nan')
@click.option('--verbose', '-v', is_flag=True,
              help='Flag to use debug logging')
def main(src, fill_value, verbose):
    if verbose:
        log_level = 'DEBUG'
    else:
        log_level = 'INFO'

    init_logger(__name__, log_level=log_level)
    clean_wave_h5(src, fill_value=fill_value)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.exception('Failed to clean US wave .h5 file!')
        raise
