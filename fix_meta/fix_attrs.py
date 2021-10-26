"""
Fix India attributes
"""
import h5py
import sys

ATTRS = {'pressure': {'scale_factor': 0.1, 'units': 'Pa'},
         'temperature': {'scale_factor': 100, 'units': 'C'},
         'winddirection': {'scale_factor': 100, 'units': 'degree'},
         'windspeed': {'scale_factor': 100, 'units': 'm/s'}}


def fix_attrs(h5_file):
    with h5py.File(h5_file, mode='a') as f:
        for dset in f:
            prefix = dset.split('_')[0]
            if prefix in ATTRS:
                ds = f[dset]
                print('Updating attributes for {}'.format(dset))
                print('- Deleting existing attributes')
                for k in ds.attrs:
                    del ds.attrs[k]

                print('- Adding new attributres: {}'.format(ATTRS[prefix]))
                for k, v in ATTRS[prefix].items():
                    ds.attrs[k] = v


if __name__ == '__main__':
    h5_file = sys.argv[1]
    fix_attrs(h5_file)
