# export_to_telegraph

Library for export webpage to Telegraph.

## usage

```
import export_to_telegraph
export_to_telegraph.TOKEN = YOUR_TELEGRAPH_TOKEN
telegraph_url = export_to_telegraph.export(webpage_url)
```

If export failed, `telegraph_url` will be None.

## how to generate token

Token is not needed if you don't plan to edit the generated telegraph.

Example code:

```
from html_telegraph_poster import TelegraphPoster
p = TelegraphPoster()
r = p.create_api_token(shortname, longname)
token = r['access_token']
```

## how to install

`pip3 install export_to_telegraph`