import subprocess
import base64

u_c = "V3JpdGUtSG9zdCAnSGVsbG8sIEltIEBVbjlucGxheWVyISEhJyAtRm9yZWdyb3VuZENvbG9yIFJlZDsgcGF1c2U="
de_c = base64.b64decode(u_c).decode('utf-8')

subprocess.call(["powershell", "-Command", de_c])

