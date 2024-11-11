# buildozer.spec

[app]
title = IMAD-213
package.name = imad213
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin
version = 0.1
requirements = python3,kivy
orientation = portrait
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 21b
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
