# python

Noen enkle Python koder som snakker med Twitter

Du må lage koder til bruk med twitter som legges inn i auth_xxxx.py filen. Kodene lages med din Twitterkonto på adressen https://apps.twitter.com/app/new

Du må installere TwitterAPI på din maskin. (I terminal på MAC: sudo pip install TwitterAPI) se også https://github.com/geduldig/TwitterAPI

# hente ut tweets fra ett bestemt område, eksempel fra Oslo

<pre>
r = api.request('statuses/filter', {'locations':'<b>-74,40,-73,41</b>'}) #NYC 
for item in r:
        print(item)
</pre>

Hvordan definere Oslo?

<img src="https://github.com/udirbetalab/python/blob/master/BBox_oslo.png" width=400>
http://boundingbox.klokantech.com/

Velg CSV format når du har definert din område firkant. Lim inn tallene som vist under i din kode.

<pre>
api.request('statuses/filter', {'locations':'<b>10.577063,59.831563,10.90116,59.994724</b>'})
</pre>
