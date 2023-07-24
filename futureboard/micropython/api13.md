# 未來板MicroPython編程13：I2C

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 13: I2C

### 初始化I2C

```
i2c = I2C(0)  # 使用預設的I2C接口
i2c = I2C(1, scl=Pin(5), sda=Pin(4), freq=400000) # 使用2支引腳作為I2C接口
```

### 掃描I2C模塊位置

```
i2c.scan()
```

### I2C讀取數據

```
i2c.readfrom(address,nbytes)
```

* address為I2C模塊的地址。
* nbytes為所讀取數據的長度。

### I2C讀取數據至列表

```
I2C.readfrom_into(addr, buf)
```

* address為I2C模塊的地址。
* 所讀取的數據會儲存到buf裡面，buf必須為bytearray。

### I2C寫入數據

```
i2c.writeto(address,buf)
```

* address為I2C模塊的地址。
* buf為寫入的數據，數據必須為byte或bytearray類型。

### I2C寫入向量

```
i2c.writevto(address,vector)
```

* address為I2C模塊的地址。
* vector為寫入的向量。

### I2C從記憶體讀取

```
I2C.readfrom_mem(address, memaddr, nbytes, *, addrsize=8)
```

* address為I2C模塊的地址。
* memaddr為記憶體的地址。
* nbytes為所讀取數據的長度。
* addrsize為記憶體的大小。

### I2C從記憶體讀取至列表

```
I2C.readfrom_mem_into(address, memaddr, buf, *, addrsize=8)
```

* address為I2C模塊的地址。
* memaddr為記憶體的地址。
* 所讀取的數據會儲存到buf裡面，buf必須為bytearray。
* addrsize為記憶體的大小。

### I2C寫入數據到記憶體

```
I2C.writeto_mem(address, memaddr, buf, *, addrsize=8)
```

* address為I2C模塊的地址。
* memaddr為記憶體的地址。
* buf為寫入的數據，數據必須為byte或bytearray類型。
* addrsize為記憶體的大小。
