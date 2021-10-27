# 小数の丸め込みについて
#### 参考ページ(https://note.nkmk.me/python-round-decimal-quantize/ )
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
