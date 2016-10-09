# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\desktop\\python\\bioinfo_excercise\\BioSuite\\BioSuite.py'],
             pathex=['D:\\desktop\\python\\bioinfo_excercise\\BioSuite\\exe\\10.6exe'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='BioSuite',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\desktop\\python\\bioinfo_excercise\\BioSuite\\src\\root.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='BioSuite')
