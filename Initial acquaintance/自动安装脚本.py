import os
libs = {"numpy","matplotlib","pillow","sklearn","requests","jieba","beautifulsoup4","wheel","networkx","sympy","pyinstaller","django","flask","werbot","pyQt5","pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("Successful")
except:
    print("Failed Somehow")
