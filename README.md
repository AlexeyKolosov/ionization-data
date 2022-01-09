# Ionization data parsing from different measuring devices
These scripts parse data files into pandas.DataFrame objects and plot time-aligned graphs.

### Requirements (Checked with python 3.6.6)

`pip install requirements.txt`
  
add path/to/ionization_data into system variables PYTHONPATH

### Usage example

```
from ionization_data import *

particles = AerotrakDF("D:/workshop/Bezvodnoe22dec2021/aerotrak_22dec_second.xlsx", 0)
field = BoltekDF("D:/workshop/Bezvodnoe22dec2021/Data Source 1-12222021_second.efm", date=(22, 12, 2021))
ions = MAC01DF("D:/workshop/Bezvodnoe22dec2021/dev1_22dec_second.mwd", remove_zeros=True)

plots = {
    'negative ions, cm-3': (ions['date_time'], ions['value'], 50000),
    'electric field, V/m': (field['date_time'], field['value'], 100),
    'particles ø0.3μm, m-3': (particles['date_time'], particles['0.3'], 2000000),
    'particles ø0.5μm, m-3': (particles['date_time'], particles['0.5'], 200000),    
    'particles ø5.0μm, m-3': (particles['date_time'], particles['5.0'], 2000),
}

align_plots(plots, "T=21°C, RH=12%", 5, 1)
```

### Boltek Electric Field Meter EFM-100
[https://www.boltek.com/product/efm-100c-electric-field-monitor](https://www.boltek.com/product/efm-100c-electric-field-monitor)

Data file extension: .efm

### Aerotrak handheld particle counter 9303
[https://tsi.com/products/cleanroom-particle-counters/handheld-particle-counters/aerotrak-handheld-particle-counter-9303/](https://tsi.com/products/cleanroom-particle-counters/handheld-particle-counters/aerotrak-handheld-particle-counter-9303/)

Data file extension: .xlsx

### МАС-01 Счетчик аэроионов малогабаритный
[https://ntm.ru/products/70/7268](https://ntm.ru/products/70/7268)

Data file extension: .mwd
