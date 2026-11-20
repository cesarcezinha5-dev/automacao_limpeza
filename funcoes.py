import os
import shutil
import ctypes
import tempfile

def limpar_temp():
    temp_dirs = [
        tempfile.gettempdir(),  
        r"C:\Windows\Temp"      
    ]
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            print(f"Limpando: {temp_dir}")
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except PermissionError:
                        pass
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
                    except PermissionError:
                        pass

def limpar_prefetch():
    prefetch_dir = r"C:\Windows\Prefetch"
    if os.path.exists(prefetch_dir):
        print(f"Limpando: {prefetch_dir}")
        try:
            for file in os.listdir(prefetch_dir):
                try:
                    os.remove(os.path.join(prefetch_dir, file))
                except PermissionError:
                    print(f"Sem permissão para apagar: {file}")
                except Exception as e:
                    print(f"Erro ao apagar {file}: {e}")
        except PermissionError:
            print("Sem permissão para acessar a pasta Prefetch. Execute como administrador.")

def esvaziar_lixeira():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000007)
        print("Lixeira esvaziada.")
    except Exception as e:
        print(f"Erro ao esvaziar lixeira: {e}")