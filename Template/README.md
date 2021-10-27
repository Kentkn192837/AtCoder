# 小数の丸め込みについて
#### 参考ページ(<a href="https://note.nkmk.me/python-round-decimal-quantize/" target="_blank">https://note.nkmk.me/python-round-decimal-quantize/ </a>)
### round()について
組み込み関数の`round`は一般的な四捨五入ではなく偶数への丸めなので注意。<br>

### deciaml.quantize()
標準ライブラリのdecimalモジュールを使うと正確な十進浮動小数点数を扱うことができる。<br>

`quantize()`メソッドの引数`rounding`に`ROUND_HALF_UP`を指定すると一般的な四捨五入、`ROUND_HALF_EVEN`を指定すると偶数への丸めとなる。<br>

#### 小数を任意の桁数で四捨五入・偶数への丸め
Decimal型のオブジェクトからquantize()を呼び出し、値を丸める。<br>
quantize()の第一引数に求めたい桁数と同じ桁数の数値を'0.1'や'0.01'のように文字列で指定する。<br>
さらに引数roundingに丸めモードを指定する。ROUND_HALF_UPを指定すると一般的な四捨五入となる。

```
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
```

```
from decimal import Decimal, ROUND_HALF_UP
f = 123.456

print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
# 123

print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
# 123.5

print(Decimal(str(f)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
# 123.46
```

#### 整数を任意の桁数で四捨五入・偶数への丸め
整数の桁に丸めたい場合、第一引数に'10'のように指定しても所望の結果は得られない。
```
i = 99518

print(Decimal(i).quantize(Decimal('10'), rounding=ROUND_HALF_UP))
# 99518
```

`E`を使った指数表記の文字列（例えば`'1E1'`）とすれば任意の指数を指定できる。指数`exponent`は`as_tuple`メソッドで確認できる。
```
print(Decimal('10').as_tuple())
# DecimalTuple(sign=0, digits=(1, 0), exponent=0)

print(Decimal('1E1').as_tuple())
# DecimalTuple(sign=0, digits=(1,), exponent=1)
```

そのままだと結果も`E`を使った指数表記になるので、通常の表記にしたい、あるいは、丸めたあとで整数`int`型と演算したい、といった場合は、`int()`で変換する。
```
print(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
# 9.952E+4

print(int(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
# 99520

print(int(Decimal(i).quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)))
# 99500

print(int(Decimal(i).quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)))
# 100000
```

# リスト中の各要素の要素数の数え上げについて
#### 参考ページ
(<a href="https://note.nkmk.me/python-collections-counter/" target="_blank">https://note.nkmk.me/python-collections-counter/ </a>)<br>
(<a href="https://docs.python.org/ja/3/library/collections.html" target="_blank">https://docs.python.org/ja/3/library/collections.html </a>)

```
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})

print(type(c))
# <class 'collections.Counter'>

print(issubclass(type(c), dict))
# True
```

キーとして要素を指定するとその個数を取得できる。要素として存在しない値を指定すると0を返す。
```
print(c['a'])
# 4

print(c['b'])
# 1

print(c['c'])
# 2

print(c['d'])
# 0
```

`keys()`, `values()`, `items()`などの辞書型のメソッドも使える。
```
print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])
```

#### 出現回数順に要素を取得: most_common()メソッド
出現回数が最も多いものは`[0]`、最も少ないものは`[-1]`のようにインデックスを指定して取得できる。要素だけ、出現回数だけを取得したい場合はさらにインデックスを指定すればOK
```
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]

print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a

print(c.most_common()[0][1])
# 4
```

出現回数の少ない順に並べ替えたい場合は増分を`-1`としたスライスを使う。
```
print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]
```

`most_common()`メソッドに引数`n`を指定すると、出現回数の多い`n`個の要素のみを返す。省略するとすべての要素。
```
print(c.most_common(2))
# [('a', 4), ('c', 2)]
```
