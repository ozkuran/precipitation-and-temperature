import netCDF4 as nc
fn = './data/3B-DAY-E.MS.MRG.3IMERG.20000601-S000000-E235959.V06.nc4.SUB.nc4'
ds = nc.Dataset(fn)

for var in ds.variables.values():
    print(var)
