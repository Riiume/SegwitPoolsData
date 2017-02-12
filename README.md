# SegwitPoolsData
Pull data regarding pools signaling support for SegWit

Written for Python 3.

#### Example usages:

```bash
> python PrintSegwitSupportingPoolsLast80.py

['BitFury', 'BTCC%20Pool', 'BitClub%20Network', 'shawnp0wers']
```

```bash
> python PrintSegwitPoolsBtcAddresses.py

[('BitFury', '1GbVUSW5WJmRCpaCJ4hanUny77oDaWW4to'), ('BTCC%20Pool', '152f1muMCNa7goXYhYAQC61hxEgGacmncB'), ('BitClub%20Network', '155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')]
```

#### Web Dependencies:
+ Blockchain.info
+ api.qbit.ninja
+ btc.blockr.io/api
