from nose.tools import *
from openpassword.agile_keychain import EncryptionKey
from openpassword.exceptions import InvalidPasswordException
from base64 import b64encode


class EncryptionKeySpec:
    def setUp(self):
        key = {
            "data": "U2FsdGVkX19CNF/5SazpsyC2/axBCsrpy1MBjTuulGu+hQgbMAT3COZgxGOfLUKG7VypKI/LpD3I5VxUP2NiIBqqLolwkTpQW79NJOUYlqv+3argoTwz4JL9j4wyay4BJbclVkZMY8xn+UXf8TlSffLMj3aWbXqfv10stbPI8S9DzAQ/0rYFCHP83E82NueF6t7RXk9PZcsprqFcQpxdU0lxTWT5fJZscwdYy/M88bVgnTHfIwI1V9RxxAKj0lDkUBppCrkGhN7pWP4mvCR1+iI9xTAxASH5WQxNp7v+9T5btNK0hpe3532fuVbhEJ6XVVTbRMEJRYAGNXp4TOc0q8yaW//eSPCs/S/eYw6Dnai4MA0IZqpdydj7viaPrQR/z18Dv3jKq0K+E0fh8wn/EHrrIvhQofdyaX6slqIVx7jI9Mi7BGNz6qKeIZXdQekXiY9F1vxTsaMXtzRCO79id3rI/UmuBtTVmQ7kV/RVErWfxU98oDFTbMqqS4J59PMqfhamlBFlv5nfsC/oKPZrROdxG69RT7upWSLiN02PS3eIjgfEWfdDNInppwWv9ig/QZ3eeiVVSAcWqr6+zlXpXLTKV0T9pBWe4Rq2cCTs32XQvz+3BphlKtSeUm50aL/ftiml1hv39Ks44JIwsZzFtXF3LhZVqwUFJsk+fdT3qDtxcEjuOuQ/TauPSUdD6duD0YjMBKroRefGAxyrFCZ1gWHRLdLxRTu0JQUmhxN+T8AHoDJSY4KvNjaCFsxFLPbGLqT3zds7RjrAdchC/swhwG9iOsOU8qpaI7Ew1YVQ8d0Ms+SdSz/JCzuoIiaKigsIXvH6/BOwoTdM46qZIe+KgqbsOJc7YOMsuZosEacYwvD1LQ5waklXP8h/0LnbVnw0sCLc/h3JX78sWNWBJjnvT29oCDrALzlNbFrsjtubn27IZWhVeIqnN7cxLlbDgunK2FZsNJr1r5ACxwGMiC/klT3uZWQyyNkLCZkReQ8N9utskSFrhs9pv+lFDvWcfUbQfPt8GeP/C8fSdxHAA3DLtzlVcajaNHXF2zdofetZfSOS9y9pvbt6IuFrcNmMqlZQu3f7Tvvga3rSmqK8v08UiV8/KTxIqJ9oVS+/tFPe+aYGL9dJG9I2f7Yo9H8OvgNLDqK1tfULTppAdWpq863XxVz/MV6AP+bIRXuy9jviKjRrT2h2KVPM1fx3Fy0efYro3FzLQlu86iVtQqn64zPGWP1Sfph2/IeRiCsFh+wKc6k/5X0TZEbsWpk0RRFN855SUYSUXgNwPqCHnS91zTm4f28CJ/mXqtdu9Y1wzwB/wTSilp4huyg5GkXyk+ZNuH7wqsOkdr8+Qg2Ckylh8hX18KVmP6DZ2EW+mykjzKkMXuLC6t4U89VtsUm4S8uX3rY5\u0000",  # nopep8
            "validation": "U2FsdGVkX19YMZ3cXoetbbnP+uMx6orlxhjYLIKtQxZnwqaN9A/NaF26+8gJPc/Ow7MubfnwX0ja0kgkRtrLVVonteZRYjoWhNi6ksg1YOWGUhO61PoUxHqJ7ZMPkn9XQw2dfNjfvi/CSVRcO4wUEBHzGGn+josnmknS2O8qQrUOysSYgsk3nSFByaFYEp4oKDTJePVeWUgiy9ytGynWPzaeye8SxXymwo7le9ufNSFjGiUqwaKmLoyzCBRQXe5PPbSHl9wqZ7AePCMA5gt8DRKXcC8MKrWHQqGZPmwfJlkP/0PWPrpam90JnnKOH8pWwoIR+zeDZSZxpENhuaLgxLoq9MVBs5t/nO1kMZFepTMu2JBOo4nguFFEJ+Br/H5m0ith88q80/Xeq2c3tUImKlE6GzFVCR2aFhiZnT/ZTbS8jt1ac/ygfXofuP1b2lNWK7WjwFz8GHtVMVT3NuSG6TN+LbpQwzVu9ofQ/ijXn9fe40OM4CDOm1fZrLK+NzdmmFKrD2wzcMultBp2bDJ0dL6xueNeVHDUjgLq1zjL1bHoi3aBqBrJuzyHBZ9VU4d5DT5ct78bT+df29kgbD3PA4wBsVEhCVbR+m/r21IVHv44BxCMV/eCIdLcsNSY4Nv7R/E9ppYlKx056hrfjOhkrlEIOOWqjzXFlJ1XVLjwv8JIb8QaovXNZ9B/6l1yCjtzeR5WXRtEG0d4aC61TKfHCGiasMZXbgzEg/UIk2cwecl8dhPqrPdysvlxLKKldX6kD7v8tISe/JwkfjiLZoiHUzN+P857KrNldWVBnL84cJAHQCs95fxK/d8G9VUr9SBcbuuz/qKdp9qM+ooi3yZZOrXSKxJIclXWGwwZmo9T9DDlRBi7D0kzjNvmxjoWk/8LD78tF6YcqSxuogQut+JSGisXut460iX8GPzhjSKtsieA7fMynWlrFnUdEkPtgkSwJidxkWF7RjhP48iyLFDWET4aGtIJN0VbNf6c74i4EIvQIeOmVIuPaSUhmHePm4jZiC/j0zxQ/kP9Q20aM+VJV2x3D/ege3l+OrpeE/Tom0OLNzdVNtLALW9lHD3hqFbYl+hSwNT8/KbRherIYhJJo+5fK5A4EuHf6KCuKliePIAGVLbk/mCkKSnBuRh9O6zfmnnzOlsrtnuLoFXJQgp12gJFzIIOV0jNiwnQB4slxhbzySzv7kaZZWbzWqRVEbRxxZJsxhsTOpN3nOuhRCO2iE7hiRQwO5zw2MJ5uoA2PUtsLoo0R5C3kNEwTgL5IZnEa08ca7ogP9SSj58umqen3TLj48VcYJeXL7n6av2eDLDeQQLQkZoYN+D5U14IpYE2+mUKoaocQffAYeRx7eDgccPE8fVfpvfg98xD+9UXSS8OS7WZeeZHOxoIOQVj/3xb\u0000",  # nopep8
            "level": "SL5",
            "identifier": "98EB2E946008403280A3A8D9261018A4",
            "iterations": 25000
        }
        self.encryption_key = EncryptionKey(key)
        self.decrypted_key = "vvvspiWrNzItmGcelM+MM8w28CQCNQYGtVCB5GbihDktjUETw7/mEfg+nnEo3DthKXisz3R+NhvQbvqoF+yBHK/Z4LvQvEx8x5KagvxLvcojYmYhtfS6bDmiUqLC+Mdc3KQo9AffqGOmbklcvfzy+Yyczt4Wy6MXDXZT2lan6tzY+RlL5gOvbqcWPq8gv9Yw2I2enhiv5R4MNzlb/4nf4TsMVqV50dzzc0L9NNfunhweoaxZ3z0G9gRn0qPsK0P5IzfGCPvycqgL1gqwUqVW1kTHJcEKWp1OE/xnwBwA3mNJmPWBYlOEX+8W6UT5RcHfdkM2rUe3ublPQ1UaLWNMwQoLlLWzqSOEdX4sf9rFeZ5UOjDtvapFkFV8U7Z8cSnZyDdKlQ9lGT2/Qv3rLavuxc6yAw0l9jEaCy11KNgAKKy2Wyc6ubCGw1CEfH72CUKOTlx7yrtuGsaytxtlWI3AitU5tLYXU+S3RyJYKKOYrMTW7joww4j5BKtBg66SNXWzkQRksnrqMCxgOZBYrxLvbBf6dO8UtmtzxNoNOYcRe9doA/hAlIvVsUjDSvtMdzcJ+A56Rb+tpGZClHRuLCBkao9b7OHaW2JjxJaNibE3mONk/UDo6xq6HiOoVqDC2USvgqE/X1XiOy1yU1qUV5wVtbV5+OYf8ubqpRlSOuSytK8lAWxCq8oTOIIPcDR77rkqj6Ou4dMfMyCWIcQ7wtwEdVCU2GzUgro3JdArmXfXwUbRmoX+c/qas6LM5MQs3fTuMooCch6qvikyHA1FrCCPC3wBrwEeyqXPQcmyGeihYWvtmyWmdJcY5c2BsxRDGVfiofcCL6t9ytH3KN33qiOkrllbLauTSNPjf1bRWqZ8G0mBp6hLMk+cg+v1Mw6LQj3wP0+vY1+bZt0MCECRIDhHfh9zS+k6F+K4eOjIO0ZkTEKNeY/rkyQSQNSpA9aOJgY0tQM0PwQMhM9PpEn5oWu2Z9e6G+AkFQg6vHM/d0I5XHVrrVNZlPHK2gPUQ8q9ZsjmbiS6oR8K7IXOfMd5K5UZXizpX3YUr5Et8NTzBy4vExFkEuLFYxyCOzwZYfU3bk3HGEMJYByK3zJWsa84r8QUWk4flU3omQSfA5Mdc/caw74atm/VfP8yMLpuFTiP6wPz4gDhq67r46dNgDDCKDMWCAsigXI1mIPJzDG79/d0w0GyO7oLLnGoptsrYLQxHbfZ+IgzJyGQ2iFxwnLjQKsnJ9vG+7A1w8jyAZij0cRV7hjDs/KaJNXxenCzE0Ofkf6IuMMtIVjbYfD0s8GXIuIAltierebQiA6I1yQtyR8WYfBziSPVTpvYf9SdxzsShlcGihSK33O03enbc6UmAWWtlRAQEBAQEBAQEBAQEBAQEBA="  # nopep8

    def it_returns_decripted_key_when_correct_password_given(self):
        decrypted_key = self.encryption_key.decrypt("masterpassword123")

        eq_(b64encode(decrypted_key).decode('utf8'), self.decrypted_key)

    @raises(InvalidPasswordException)
    def it_raises_an_invalidpasswordexception_with_incorrect_password(self):
        decrypted_key = self.encryption_key.decrypt("incorrectpassword")
