from distutils.core import setup
import py2exe

setup(windows=['bing_wallpaper.pyw'],
      options={
          'py2exe':{
              'packages': ['re', 'json','requests','urllib','ctypes','socket']
          }
      }
     )

