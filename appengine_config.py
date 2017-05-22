from google.appengine.ext import vendor
import os

# Third-party libraries are stored in "lib", vendoring will make
# sure that they are importable by the application.
if os.path.isdir(os.path.join(os.getcwd(), 'lib')):
    vendor.add('lib')
