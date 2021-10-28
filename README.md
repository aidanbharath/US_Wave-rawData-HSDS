# US Wave Rechunking for HSDS

Scripts to prepare US Wave data for HSDS by rechunking to ~2-6MB chunks

All of this code uses the [rex package](https://nrel.github.io/rex/)

1) Extract datasets and their attributes from source .h5 file:

NOTE: this was a function/CLI call in a private repo (SORRY)
```
attrs_list = []
with h5py.File(h5_file, 'r') as f:
    datasets = list(f)
    for ds_name in datasets:
        ds = f[ds_name]
        try:
            attrs = {k: v for k, v in ds.attrs.items()}
            if not attrs:
                attrs = None
            ds_attrs = {'attrs': attrs,
                        'dtype': ds.dtype.name,
                        'chunks': ds.chunks
                        'shape': ds.shape}
            ds_attrs = pd.Series(ds_attrs)
            ds_attrs.name = ds_name
            attrs_list.append(ds_attrs.to_frame().T)
        except Exception:
            pass

ds_attrs = pd.concat(attrs_list)
ds_attrs.to_json(out_json, indent=4)
```

2) Have Evan create meta data from the coordinates in the source .h5 file, use notebooks to add water depth to the meta and clean it up.

3) Use above files and jupyter notebooks to create the hsds attributes.

4) Use the scripts to rechunk source .h5 files into /datasets/US_wave/ directory

NOTES for #3:
- The wave and buoy data have different datasets, namely the buoy data has extra datasets
- Make sure to remove any nan's in the jurisdiction column of the meta and replace with 'None' or else HSDS will barf
- The Buoy meta is created from the wave meta by mapping the buoy locations to the nearest wave location
- In the buoy data the largest dataset is `directional_wave_spectrum`. It is 4 dimensional
  ('time', 'frequency', 'direction', 'position'), it is often the only dataset that needs to be chunked in the buoy files but
  determining the chunk size is hand wavy. My process has been to using 8 week chunks for the time axis (8 * 7d * 24hr) and then reduce the 
  freq, dims, and pos axis evenly until i get ~ 2mb chunks. Example:
  
```

In [41]:

dset_arr = np.ones((8784, 29, 72, 24), dtype='float32')
dset_size = sys.getsizeof(dset_arr) * 10**-6
print('energy size = {:.3f} MB'.format(dset_size))

dset_arr = np.ones((8*7*24, 6, 12, 6), dtype='float32')
dset_size = sys.getsizeof(dset_arr) * 10**-6
print('energy size = {:.3f} MB'.format(dset_size))


energy size = 1760.735 MB
energy size = 2.323 MB
```
