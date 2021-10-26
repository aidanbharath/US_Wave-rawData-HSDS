"""
Compute wave means
"""
from rex import TemporalStats, MultiYearWaveResource, init_logger
from rex.temporal_stats.temporal_stats import circular_mean
import sys


def main(domain, dset):
    """
    Run longterm (32-year) monthly and annual means
    """
    res_path = f'/datasets/US_wave/v1.0.0/{domain}/{domain}_wave*.h5'
    out_path = f'/scratch/mrossol/US_wave/wave_means/{domain}_wave_{dset}.csv'
    if dset == 'maximum_energy_direction':
        kwargs = {'weights': ['omni-directional_wave_power',
                              'directionality_coefficient']}
        statistics = {'weighted_circular_mean': {'func': circular_mean,
                                                 'kwargs': kwargs}}
        max_workers = 16
    else:
        statistics = 'mean'
        max_workers = None

    TemporalStats.run(res_path, dset, statistics=statistics,
                      out_path=out_path, res_cls=MultiYearWaveResource,
                      month=True, combinations=True,
                      max_workers=max_workers, chunks_per_worker=1)


if __name__ == "__main__":
    dsets = ["significant_wave_height", "peak_period", "energy_period",
             "omni-directional_wave_power", "spectral_width",
             "maximum_energy_direction", "directionality_coefficient",
             "mean_zero_crossing_period", "mean_absolute_period"]

    init_logger('rex', log_level='DEBUG')
    domain = sys.argv[1]
    dset = sys.argv[2]
    main(domain, dset)
