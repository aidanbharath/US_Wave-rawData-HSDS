"""
Clean up hindcast data
"""
import click
import h5py
import logging
import numpy as np
import os
from rex import init_logger

logger = logging.getLogger(__name__)


def clean_dset(f_in, f_out, dset_name, fill_value=-9999):
    """
    Clean up dataset

    Parameters
    ----------
    f_in : h5yp.File
        Open source h5py.File instance
    f_out : h5yp.File
        Open destination h5py.File instance
    dset_name : str
        Name of dataset to be cleaned
    fill_value : int
        Fill value that is to be replaced with np.nan
    """
    logger.info('Cleaning and transfering {}'.format(dset_name))
    ds_in = f_in[dset_name]
    data = ds_in[...]

    fix_shape = dset_name not in ['meta', 'coordinates', 'water_depth']
    fix_shape &= len(data) not in (2920, 2928)
    if fix_shape:
        time_steps = len(data)
        if time_steps > 2928:
            logger.debug('{} has {} timesteps! Will be reduced to 2928 '
                         'timesteps'.format(dset_name, time_steps))
            data = data[:2928]
        else:
            logger.debug('{} has {} timesteps! Will be reduced to 2920 '
                         'timesteps'.format(dset_name, time_steps))
            data = data[:2920]

    if dset_name not in ['meta', 'coordinates', 'time_index']:
        mask = data == fill_value
        mask |= np.isinf(data)
        if np.any(mask):
            logger.debug('Replacing fill values and infs with np.nan')
            data[mask] = np.nan

    ds_out = f_out.create_dataset(dset_name, shape=data.shape,
                                  dtype=data.dtype, chunks=ds_in.chunks,
                                  data=data)
    logger.debug('Transfering {} attributes'.format(dset_name))
    for k, v in ds_in.attrs.items():
        ds_out.attrs[k] = v


def clean_wave_h5(src, dst, replace=False, fill_value=-9999):
    """
    Cleanup src .h5 file and save as dst

    Parameters
    ----------
    src : path
        US wave .h5 file to cleanup
    dst : path
        Destination directory or destination file to save cleaned data into
    replace : bool
        Flag to replace existing dst file
    fill_value : int
        Fill value that is to be replaced with np.nan
    """
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))

    logger.info('Cleaning up data in {} and saving to {}'.format(src, dst))

    if os.path.exists(dst):
        if replace:
            logger.warning("{} already exists and will be replaced!"
                           .format(dst))
            os.remove(dst)
        else:
            msg = ('{} already exists, to replace it set replace=True!'
                   .format(dst))
            logger.error(msg)
            raise FileExistsError(msg)

    with h5py.File(src, mode='r') as f_in:
        with h5py.File(dst, mode='w-') as f_out:
            logger.debug('Transfering global attributres')
            for k, v in f_in.attrs.items():
                f_out.attrs[k] = v

            for dset_name in f_in:
                clean_dset(f_in, f_out, dset_name, fill_value=fill_value)


@click.command()
@click.option('--src', '-src', type=click.Path(exists=True), required=True,
              help='US wave .h5 file to cleanup')
@click.option('--dst', '-dst', type=click.Path(), required=True,
              help=('Destination directory or destination file to save '
                    'cleaned data into'))
@click.option('--fill_value', '-fill', type=int, default=-9999,
              show_default=True,
              help='Fill value that is to be replaced with np.nan')
@click.option('--replace', '-rm', is_flag=True,
              help='Flag to replace existing dst file')
@click.option('--verbose', '-v', is_flag=True,
              help='Flag to use debug logging')
def main(src, dst, fill_value, replace, verbose):
    if verbose:
        log_level = 'DEBUG'
    else:
        log_level = 'INFO'

    init_logger(__name__, log_level=log_level)
    clean_wave_h5(src, dst, fill_value=fill_value, replace=replace)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.exception('Failed to clean US wave .h5 file!')
        raise
