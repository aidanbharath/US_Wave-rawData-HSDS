"""
Fix meta data
"""
import click
import h5py
import logging
import numpy as np

from rex.utilities import init_logger

logger = logging.getLogger(__name__)


def fix_meta(h5_path, meta_path, chunks=None):
    logger.info('Updating meta in {}'.format(h5_path))
    meta = np.load(meta_path)
    with h5py.File(h5_path, 'a') as f:
        if chunks is None and 'meta' in f:
            chunks = f['meta'].chunks
        elif isinstance(chunks, int):
            chunks = (chunks, )

        if 'meta' in f:
            del f['meta']
            logger.debug('original meta deleted')

        ds = f.create_dataset('meta', shape=meta.shape, dtype=meta.dtype,
                              chunks=chunks, data=meta)
        ds.attrs["dimensions"] = ["position"]
        logger.debug('New meta loaded with chunks {}'.format(chunks))


@click.command()
@click.option('--h5_path', '-h5', type=click.Path(exists=True), required=True,
              help='.h5 file to fix meta in')
@click.option('--meta_path', '-meta', type=click.Path(exists=True),
              required=True, help='path to meta data to load')
@click.option('--chunks', '-c', default=None, type=int,
              help='meta data chunk size')
@click.option('--log_file', '-log', default=None, type=click.Path(),
              help='Log file (will overwrite if exists)')
@click.option('--verbose', '-v', is_flag=True,
              help='Flag to use verbose (DEBUG) logging')
def main(h5_path, meta_path, chunks, log_file, verbose):
    if verbose:
        log_level = 'DEBUG'
    else:
        log_level = 'INFO'

    if chunks == 0:
        chunks = None

    logger = init_logger(__name__, log_level=log_level, log_file=log_file)
    logger.debug('Logging level = %r', log_level)
    logger.debug('Log to file = %r', log_file)

    fix_meta(h5_path, meta_path, chunks=chunks)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logger.exception('Error updating meta data')
        raise
