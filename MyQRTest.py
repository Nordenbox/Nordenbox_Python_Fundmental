from MyQR import myqr
import os
version, level, qr_name = myqr.run(
    words='http://hardimage.pro',
    version=1,
    level='H',
    picture='myqrtest.gif',
    colorized=True,
    contrast=0.5,
    brightness=1.0,
    save_name=None,
    save_dir=os.getcwd()
)
