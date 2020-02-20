# Example of Basic Authemtication

```shell
echo "testuser:$(mkpasswd -m sha512crypt verybadpassword)" > passwords
faas-cli secret create passwords --from-file=passwords --gateway=http://127.0.0.1:8080/
```
