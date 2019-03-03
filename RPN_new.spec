# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:/GitHub/RPC/RPN_new.py'],
             pathex=['D:/GitHub/RPC/Source.py', 'D:/GitHub/RPC/RPN_function.py', 'D:/GitHub/RPC/count_time.py', 'D:\\GitHub\\RPC'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='RPN_new',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='D:\\GitHub\\RPC\\image.ico')
