[app]
title = Intermediate Topper
package.name = intermediatetopper
package.domain = org.siddharth
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.12,kivy==2.3.0,hostpython3==3.10.12

# ఇక్కడ ఐకాన్ ఫోల్డర్ లో ఉన్న ఫైల్ పేరు ఇవ్వాలి
icon.filename = icon.png

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
