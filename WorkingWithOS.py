import os

# Get all subdirectories
files = [f for f in os.listdir(os.getcwd()) if not os.path.isfile(f) and f[0]!="."]
for idx, file in enumerate(files):
    print(idx, ":", file)
    
import pkgutil

for mi in pkgutil.iter_modules():
    if mi.ispkg:
        print(mi.name)

pkgs = pkgutil.walk_packages([os.getcwd()])
for pkg in pkgs:
    if pkg.ispkg:
        print(pkg)