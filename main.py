import replicate
from tokenupdation import get_token as token
output = replicate.run(
    f"sczhou/codeformer:{token()}",
    input={"image": open("lofi.jpg", "rb")}
)
print(output)