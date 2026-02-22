import os
from src.utils import write_response
import requests
import json

headers = {
    "Host": "z-p42.graph.instagram.com",
    "Accept-Language": "en-US",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Priority": "u=5, i",
    "X-Fb-Client-Ip": "True",
    "X-Fb-Connection-Type": "WIFI",
    "X-Fb-Friendly-Name": "undefined:analytics",
    "X-Fb-Request-Analytics-Tags": json.dumps(
        {
            "network_tags": {
                "product": {},
                "surface": "undefined",
                "is_ad": "0",
                "request_category": "analytics",
                "purpose": "prefetch",
                "retry_attempt": "0",
            }
        }
    ),
    "X-Fb-Server-Cluster": "True",
    "X-Ig-App-Id": "567067343352427",
    "X-Ig-Capabilities": "3brTv10=",
    "X-Ig-Connection-Type": "WIFI",
    "X-Tigon-Is-Retry": "False",
    "X-Zero-Eh": "IG0e09d776530888418ab70f3822fbb4e1",
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Content-Length': '2259',
    "User-Agent": "Instagram 410.1.0.63.71 Android (31/12; 420dpi; 1080x2274; Google/google; sdk_gphone64_arm64; emulator64_arm64; ranchu; en_US; 846519343)",
    "X-Fb-Conn-Uuid-Client": "1fe53a462b93835b40bbeaad5e38c510",
    "X-Fb-Exp-Tag": "None,None,None",
    "X-Fb-Http-Engine": "Tigon/MNS/TCP",
    "Connection": "keep-alive",
}

data = {
    "access_token": "567067343352427|f249176f09e26ce54212b472dbab8fa8",  # jsut hardcoded app id and token
    "format": "json",
    "ffdb_token": "",
    "compressed": "1",
    "multi_batch": "1",
    "sent_time": "1767733471.945",
    "message": "eJztmktv4zYQgP+Lzpah9yO3HnaLoPsAul3soQgISqJlIhKpJSlnjSD/vTOk/Mg62STuNm1hXwKb5JDDmW9mSDq3XkVNvWTau/jz1jO8Z95FmGd5HsdJDh+CmUeHgfDGu/DSLA+yPE7iOI2SKPdc14op6EvCYB7Og3kWz/MQeqqRdw0RY+9dFEmWhiWIzbxaCs2EIdpQAwvB5A1b8Ro+erq5Ju2wlIJlCaGqzxKYRepp+jDyNmOdLgGrFg1o4idZBn+KkPlVSGM/zvKmSvKyjikFEc205lI4mc9vP/lhVNGsppUfl3nuJ01C/bJMYIYqKoMkjNM4b/zASn71LiK3xdEtiSpQQ62l2Dej4NOtdwM7UQvadW6NigZBkyShHxRh6idpxvwyoJFP45g1LC9YFOFW2LeBKTC2MCDD24SSjq6ZYg1pmOatILQ2fMXNmuyNnHmGaUNaJccBxNC+EuREO9KWEc06VhupYFg7vsRG4BRDuWCql83YoS92e+pkS7hAhTs6aFDPEZIU6RycB25UZmoK51tqoqx4E4Lp6lEp9PbBgDyN7YDhejKrAt2pZqReUiFYB62Dkg120IZLYtYDqvXl8u2l//nDbx8+fvkAfQNvGbhWMc3UClS7ZusbqRpo+DqCnaClg32Ieu1d+BGq+5gAbnJaou44asxWzt6PSVQtjDVqZN7dzHtcfDds5j1ghPxNOfMExXZgANSoaYf+lnpUKKJpP3RctETZaAlhEtpCoBZxUWRBeTfbwxDEyHaq5+KEQk/ThBFwROi9Flb7VJ2R2kdKcMOBKPRfR0dRL/e8fyxnj8Z0EZXWO/c9mmYhmmnRyRvQ6N3HX8kl2vkJDx+XU58FHB046cCYAEQcvjRTajkqLFZi7LrXRC3876FWxMkeai2DsiRl2zHINLUcYRZqDOsH89PwitMH8crRNEwpqTa7gCwGkPfcFn7vkL1nYfKPAHqG7WjY0h/DtqC8OyKXSRDB2ok6kIkTuu6X3oGHsVSt3MmVYbVcyp6RAQolppS6hlOmlcfTqsXOSeBCZNqoOznColCV4Tsm5i2worbWcbawZwHUAoxNm+/jiTVbVWpQsZVqbRFgC+745YJgxacdzminGaiiPZjg9u7UMcr3c1ZNqTPz/hSa8Pb/SZE7PdLRLM8onVH6WyjVnRzxNnBOS2eWfkJxO0P0KhBlPwmiK8To+7t1EiQn/RAYPv0Q2FN1zZRdIMrzMgrjYgZ3cNihmHQNgzgtSuybvMB2Ppi+bw79sXMx4I7ClZSGIOZxmqVBGedorxFkcUdCW/vhC8+0P/g2KeNAgul7ZpYSdVdUNLInGwjsTjYX4tx+meCzzhYcwYMoksYuplGVDnf7dYDkISCNQDQSYm9bgBS4dQERDhapcXkmaNVBVF9ArtHsbqPWDm1juHfigRsX0V7gws118WSMFg/HaFzGJx2jwdMxeuRTJgXI14bXel/Y3cu3jwg20luoRrsx+rDUPvOl4LQjIinvvWI+aNeXHIUexttO3HUuHcl+7p4U5pAfleTNfIAUBkeg3ahT90qx/7Y8WYnQ4Zrgj1LoiSNflB9TehtZl+3vzNVF/csmEN+7Thfx9uqLI5kgnz/hE5/blzYKdbCBB+U4LLMsy5NdbjqQ23PFrute+6I6lIJ9CN25YlyNooEyPtl3oXTtWYu3UA23x+dg2zRZ821l3tmGSzDbvfVWVHFXeSGRBbPgCnasGGnkjcATNJbXaZuQm7jeL7cnzmuaFcjr8yja5hrTkQ3aG3p6uIDYuvTStPO6YBfRGezTALvMTgrsc8Y+EbDzIj0psM8Z+2TA/jcy9tXd1dZ9hIuFRMINt/edntdKEvuff/b2/NAv7mVkHyZqqpQT+sN/LytulaylEJOb0C7u2ce9OtsHoHrJ6muNFy53S56adw/IK2Qf35AOe378VLF/w7+7+wu/w8TI",
    "request_debug_config": "1",
}

response = requests.post(
    "https://z-p42.graph.instagram.com/logging_client_events",
    headers=headers,
    data=data,
    verify=False,
)

write_response(response, os.path.dirname(__file__))
