# tls_patch.py
# patch to force TLSv1 protocol in python's ssl module
import functools
import ssl

ssl_init = ssl.SSLSocket.__init__
@functools.wraps(ssl_init)
def force_tls(self, *args, **kwargs):
  kwargs['ssl_version'] = ssl.PROTOCOL_TLSv1
  ssl_init(self, *args, **kwargs)

ssl.SSLSocket.__init__ = force_tls
