---
name: BAffineTransform
type: class
kit: interface_kit
brief: "Undocumented class"
source: haiku-book
---

# BAffineTransform Class
**Kit/Group:** [Interface Kit](../interface_kit/group__interface.md) | [Main C++ library (libbe.so)](group__libbe.md)

## Description

Undocumented class. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BAffineTransform](#ad25069639f485a0565c3bcdc22f9e75e) () — Undocumented public method.
* [BAffineTransform](#a5a53a6fbc72aea554bf53fce207aefba) (const BAffineTransform &copyFrom) — Undocumented public method.
* [BAffineTransform](#aa3c9494e63680fe9cc692d16f907c392) (double sx, double shy, double shx, double sy, double tx, double ty) — Undocumented public method.
* `virtual` [~BAffineTransform](#a9af30520454fc48099b36850c5c1948d) () — Undocumented public method.
* `void` [Apply](#a1ea1c5d9cca7af61f3cf792140bdf34c) (BPoint *point) const — Undocumented public method.
* `void` [Apply](#ac766d07792d4d3d387203f8b66d18335) (BPoint *points, uint32 count) const — Undocumented public method.
* `BPoint` [Apply](#abb12f3465e5fce1dff2cf96a63da21c6) (const BPoint &point) const — Undocumented public method.
* `void` [Apply](#a25faa18c510133c835a8d403bfcd4e8d) (double *x, double *y) const — Undocumented public method.
* `void` [ApplyInverse](#ad1e4804e9c0dc94cbab2021bf7d1c6bf) (BPoint *point) const — Undocumented public method.
* `void` [ApplyInverse](#a7684ddcd84de76c1756a993bb93134a8) (BPoint *points, uint32 count) const — Undocumented public method.
* `BPoint` [ApplyInverse](#a476f8bc5509bcd03a0051f593db83a33) (const BPoint &point) const — Undocumented public method.
* `void` [ApplyInverse](#a57e6fd4979a2e72ee6edd6de34c88862) (double *x, double *y) const — Undocumented public method.
* `double` [Determinant](#ae53ecb58adc270f614dbc8aeb852ef61) () const — Undocumented public method.
* `virtual status_t` [Flatten](#a8e9004914c3d7ac7ddb16d866cab918e) (void *buffer, ssize_t size) const — Undocumented public method.
* `virtual ssize_t` [FlattenedSize](#a5ee0a422598727d1653c06d6769a26f9) () const — Undocumented public method.
* `const BAffineTransform &` [FlipX](#ade8105273168ef46f16c28cdbe3b8baf) () — Undocumented public method.
* `const BAffineTransform &` [FlipY](#ab9dff3a291e50ebc8262e1ebe2e57c03) () — Undocumented public method.
* `bool` [GetAffineParameters](#af2a621be6de8415725a86ba818830e1e) (double *translationX, double *translationY, double *rotation, double *scaleX, double *scaleY, double *shearX, double *shearY) const — Undocumented public method.
* `void` [GetScale](#aac76e19af9104c7dbfb6f22b1e491396) (double *sx, double *sy) const — Undocumented public method.
* `void` [GetScaleAbs](#a092dafbbb4e0a44ef5b6f34404cea8fd) (double *sx, double *sy) const — Undocumented public method.
* `void` [GetTranslation](#ac8259e1870d615df3aca0982df66e6c2) (double *tx, double *ty) const — Undocumented public method.
* `double` [InverseDeterminant](#ae1847cda27427323d6d4635f97c1d993) () const — Undocumented public method.
* `const BAffineTransform &` [Invert](#a314a95ed4eae3167e0f4e918bb602678) () — Undocumented public method.
* `bool` [IsDilation](#a68315d0bd302b6a2dc88eff1b3928264) (double epsilon=kDefaultEpsilon) const — Undocumented public method.
* `bool` [IsEqual](#ab2d8b9f353d23c2396f4d78a30f7f662) (const BAffineTransform &other, double epsilon=kDefaultEpsilon) const — Undocumented public method.
* `virtual bool` [IsFixedSize](#ac4b8ff09ab94c925d2f6e068b945bf4b) () const — Undocumented public method.
* `bool` [IsIdentity](#a037dddc4193a48ff8c27d1654b2325ec) (double epsilon=kDefaultEpsilon) const — Undocumented public method.
* `bool` [IsValid](#a43501ac1ea3dfddcbe3e0316583e3073) (double epsilon=kDefaultEpsilon) const — Undocumented public method.
* `const BAffineTransform &` [Multiply](#ab9c4342d106d131da6ae68bb0221e18e) (const BAffineTransform &other) — Undocumented public method.
* `const BAffineTransform &` [MultiplyInverse](#a9e9793223eda0ab6ff25c9d43aa004c2) (const BAffineTransform &other) — Undocumented public method.
* `bool` [operator!=](#a23a0ec59f04809146dfe9ffe34ce3edf) (const BAffineTransform &other) const — Undocumented public method.
* `BAffineTransform` [operator*](#a7c625a1d0e1920218240f5f04bab0f53) (const BAffineTransform &other) const — Undocumented public method.
* `const BAffineTransform &` [operator*=](#a042a08b8c104bcbd6c1a2aada58fcbd5) (const BAffineTransform &other) — Undocumented public method.
* `BAffineTransform` [operator/](#a1bb302fa4699269d0c544aea5a083f76) (const BAffineTransform &other) const — Undocumented public method.
* `const BAffineTransform &` [operator/=](#a6570653cc8f5af3ab47a500725635dd6) (const BAffineTransform &other) — Undocumented public method.
* `BAffineTransform &` [operator=](#a4c53dc8ffbf3959419ac838e1a7ab840) (const BAffineTransform &copyFrom) — Undocumented public method.
* `bool` [operator==](#ae52aa29f15e4525bf0000f01ba8731ac) (const BAffineTransform &other) const — Undocumented public method.
* `BAffineTransform` [operator~](#a2bddbfbfc45c2f182b5fddff87ea83e5) () const — Undocumented public method.
* `const BAffineTransform &` [PreMultiply](#a7ce88697f485af7b0ca7d6435d98489a) (const BAffineTransform &other) — Undocumented public method.
* `const BAffineTransform &` [PreMultiplyInverse](#abbb4eb0d6f98afe3f3549dfda385fb50) (const BAffineTransform &other) — Undocumented public method.
* `const BAffineTransform &` [PreRotateBy](#a0a0889c583b7b842e2825a6bcf341178) (double angleRadians) — Undocumented public method.
* `const BAffineTransform &` [PreScaleBy](#abccb7b3b9fcb18b013bb91e10b8fecb2) (double x, double y) — Undocumented public method.
* `const BAffineTransform &` [PreTranslateBy](#add03988f06209700da7b92b8e3b8d915) (double x, double y) — Undocumented public method.
* `const BAffineTransform &` [Reset](#a6379c31371e17a60efcdb1fcf4d0cd0c) () — Undocumented public method.
* `const BAffineTransform &` [RotateBy](#a6b5f38552384b104abbee55ca3fc64fb) (const BPoint &center, double angle) — Undocumented public method.
* `const BAffineTransform &` [RotateBy](#a789ff2d5272214339d0dd4b93208ebb8) (double angle) — Undocumented public method.
* `BAffineTransform` [RotateByCopy](#a66d5104f6e5d1115600ac87d32303ab2) (const BPoint &center, double angle) const — Undocumented public method.
* `BAffineTransform` [RotateByCopy](#a34718366aee4a6488e902085ce47fab2) (double angle) const — Undocumented public method.
* `double` [Rotation](#af0b8dde4fe97c5941ecaab2a9f6bf917) () const — Undocumented public method.
* `double` [Scale](#a8d5da80b595e51e4e038f3def93bbbb7) () const — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#abef04ce969c13794cdf06c76567a8c9a) (const BPoint &center, const BPoint &scale) — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#abb2b2e4909d63bea13fbb7aa835ab007) (const BPoint &center, double scale) — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#aa9653d485aea3db033c466d06cd4671a) (const BPoint &center, double x, double y) — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#abce1c40531fbdd408a1be256b73d034c) (const BPoint &scale) — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#adfa3e0a962a14bc69eb80c8737e61159) (double scale) — Undocumented public method.
* `const BAffineTransform &` [ScaleBy](#a3c1dce80ba28d91644fa749f2406a391) (double x, double y) — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#a712fd6053edeb1d293bc937f28e3729d) (const BPoint &center, const BPoint &scale) const — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#a5b8af3306ee95bba9e2025de3df61aaa) (const BPoint &center, double scale) const — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#a26c8cd7aae20955195ee7fe8324e6299) (const BPoint &center, double x, double y) const — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#a51fb9330cc2c3dd9a960582970bf888a) (const BPoint &scale) const — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#a44efc24c5735a09de5dd2c22fdf08928) (double scale) const — Undocumented public method.
* `BAffineTransform` [ScaleByCopy](#abd46e0e45070bce7242eb64e3b58befb) (double x, double y) const — Undocumented public method.
* `const BAffineTransform &` [SetScale](#a069399a3dafbce032c426d2ed69addad) (double scale) — Undocumented public method.
* `const BAffineTransform &` [SetScale](#a5b1e201787bb7df0fecaabe5b4872a5f) (double x, double y) — Undocumented public method.
* `const BAffineTransform &` [ShearBy](#a8db5e3f742c8b4c2c48d787aad712be8) (const BPoint &center, const BPoint &shear) — Undocumented public method.
* `const BAffineTransform &` [ShearBy](#a933508f009cedee118c716e754ee4821) (const BPoint &center, double x, double y) — Undocumented public method.
* `const BAffineTransform &` [ShearBy](#afc667d00cda4b82971d6b2e1e02a53fa) (const BPoint &shear) — Undocumented public method.
* `const BAffineTransform &` [ShearBy](#af2010ac85b19bd022b9167dacf5b3319) (double x, double y) — Undocumented public method.
* `BAffineTransform` [ShearByCopy](#a1f4dbcc27ab3b2d02dd90a0b42269ac0) (const BPoint &center, const BPoint &shear) const — Undocumented public method.
* `BAffineTransform` [ShearByCopy](#acbb1d202cb69593acdf1c005b1da0d08) (const BPoint &center, double x, double y) const — Undocumented public method.
* `BAffineTransform` [ShearByCopy](#a33431425e5060fac980351f79fbef2b0) (const BPoint &shear) const — Undocumented public method.
* `BAffineTransform` [ShearByCopy](#affd22f7f7545724642c5d80eddf87e56) (double x, double y) const — Undocumented public method.
* `const BAffineTransform &` [TranslateBy](#a6e8f17e42cf26c3c263ad6fa142952e7) (const BPoint &delta) — Undocumented public method.
* `const BAffineTransform &` [TranslateBy](#a472101df3b3a7e45d6393044949c2e54) (double x, double y) — Undocumented public method.
* `BAffineTransform` [TranslateByCopy](#a09e1278f7f8051f7d27b08da3a6f56f5) (const BPoint &delta) const — Undocumented public method.
* `BAffineTransform` [TranslateByCopy](#aa206f5321cb3f2be1b0a412d09fc42bc) (double x, double y) const — Undocumented public method.
* `virtual type_code` [TypeCode](#a8b6a0f6bc9f1999f1f4a4e5a17610958) () const — Undocumented public method.
* `virtual status_t` [Unflatten](#a00b1c34cc0b696e14fb233f3ad74212f) (type_code code, const void *buffer, ssize_t size) — Undocumented public method.
* `virtual` [~BFlattenable](#a884e130a5d27acc15b1e4e4c505157ff) () — Destructor. Does nothing.
* `virtual bool` [AllowsTypeCode](#a30165696bba76fed10e37508cc4f6925) (type_code code) const — Get whether or not the supplied type_code is supported.
* `virtual status_t` [Flatten](#ab934b64a8b218a4f9078ded191be6fbb) (void *buffer, ssize_t size) const =0 — Pure virtual that should flatten the object into the supplied buffer.
* `virtual ssize_t` [FlattenedSize](#a9b5885d4454326ca448438960ecff466) () const =0 — Pure virtual that should return the size of the flattened object in bytes.
* `virtual bool` [IsFixedSize](#ac019f502749a0cc78082f5ec7c8f5b56) () const =0 — Pure virtual that should return whether or not flattened objects of this type always have a fixed size.
* `virtual type_code` [TypeCode](#a819507fa1b0906f14299db15f6e990d1) () const =0 — Pure virtual that returns the type_code this class flattens to.
* `virtual status_t` [Unflatten](#a41e7168574912690be159991d2b07a97) (type_code code, const void *buffer, ssize_t size)=0 — Pure virtual that should unflatten the buffer and put the contents into the current object.

### Static Public Member Functions

* `static BAffineTransform` [AffineRotation](#a95f0f60c7a2fee4773ffdaeaf171ef4e) (double angle) — Undocumented public method.
* `static BAffineTransform` [AffineScaling](#afad1577545cf952d96e48a42ed22346e) (double scale) — Undocumented public method.
* `static BAffineTransform` [AffineScaling](#a355ff0769afed044f9d01652836534c7) (double x, double y) — Undocumented public method.
* `static BAffineTransform` [AffineShearing](#af8084f233f00df42bfbaeb59bc3a597d) (double x, double y) — Undocumented public method.
* `static BAffineTransform` [AffineTranslation](#a9bcad861f87068ae1bac663452507fea) (double x, double y) — Undocumented public method.

### Public Attributes

* `double` [shx](#ac0507ae12b487272cb2f6b8baec8f20f) — Undocumented public variable.
* `double` [shy](#a0383bca21bed077dc84747b57d46b333) — Undocumented public variable.
* `double` [sx](#a6f42e6d417bca34c5d9c4adc71544190) — Undocumented public variable.
* `double` [sy](#a4c03a79455e12d228e8d062e32dc6dc7) — Undocumented public variable.
* `double` [tx](#a2ea11bc896b815ffaa81abf9f1035e17) — Undocumented public variable.
* `double` [ty](#a13fe20ce5797799cc9dc3eaea5d18760) — Undocumented public variable.

### Static Public Attributes

* `static constexpr double` [kDefaultEpsilon](#a3c001ed01b4cf15e42832b5f10a088fc) = 1e-14 — Undocumented public variable.

## Detailed Member Documentation

### `BAffineTransform()`

```cpp
BAffineTransform::BAffineTransform()
```

Undocumented public method. 



**Since:** Haiku R1


Referenced by [operator*()](classBAffineTransform.md#a7c625a1d0e1920218240f5f04bab0f53), and [operator/()](classBAffineTransform.md#a1bb302fa4699269d0c544aea5a083f76).

---

### `BAffineTransform()`

```cpp
BAffineTransform::BAffineTransform(double sx, double shy, double shx, double sy, double tx, double ty)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `sx` | Undocumented |
| `shy` | Undocumented |
| `shx` | Undocumented |
| `sy` | Undocumented |
| `tx` | Undocumented |
| `ty` | Undocumented |





**Since:** Haiku R1

---

### `BAffineTransform()`

```cpp
BAffineTransform::BAffineTransform(const BAffineTransform & copyFrom)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `copyFrom` | Undocumented |





**Since:** Haiku R1

---

### `~BAffineTransform()`

```cpp
BAffineTransform::~BAffineTransform()
```

Undocumented public method. 



**Since:** Haiku R1

---

### `AffineRotation()`

```cpp
static static BAffineTransform BAffineTransform::AffineRotation(double angle)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `angle` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `AffineScaling()`

```cpp
static static BAffineTransform BAffineTransform::AffineScaling(double scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `AffineScaling()`

```cpp
static static BAffineTransform BAffineTransform::AffineScaling(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `AffineShearing()`

```cpp
static static BAffineTransform BAffineTransform::AffineShearing(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Referenced by [ShearBy()](classBAffineTransform.md#af2010ac85b19bd022b9167dacf5b3319).

---

### `AffineTranslation()`

```cpp
static static BAffineTransform BAffineTransform::AffineTranslation(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Apply()`

```cpp
void BAffineTransform::Apply(BPoint * point)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Undocumented |





**Since:** Haiku R1

---

### `Apply()`

```cpp
void BAffineTransform::Apply(BPoint * points, uint32 count)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `points` | Undocumented |
| `count` | Undocumented |





**Since:** Haiku R1

---

### `Apply()`

```cpp
BPoint BAffineTransform::Apply(const BPoint & point)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Apply()`

```cpp
void BAffineTransform::Apply(double * x, double * y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `ApplyInverse()`

```cpp
void BAffineTransform::ApplyInverse(BPoint * point)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Undocumented |





**Since:** Haiku R1

---

### `ApplyInverse()`

```cpp
void BAffineTransform::ApplyInverse(BPoint * points, uint32 count)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `points` | Undocumented |
| `count` | Undocumented |





**Since:** Haiku R1

---

### `ApplyInverse()`

```cpp
BPoint BAffineTransform::ApplyInverse(const BPoint & point)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `point` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ApplyInverse()`

```cpp
void BAffineTransform::ApplyInverse(double * x, double * y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Since:** Haiku R1


References [InverseDeterminant()](classBAffineTransform.md#ae1847cda27427323d6d4635f97c1d993), [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `Determinant()`

```cpp
double BAffineTransform::Determinant()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), and [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7).

---

### `Flatten()`

```cpp
status_t BAffineTransform::Flatten(void * buffer, ssize_t size)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#ab934b64a8b218a4f9078ded191be6fbb).

---

### `FlattenedSize()`

```cpp
ssize_t BAffineTransform::FlattenedSize()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a9b5885d4454326ca448438960ecff466).

---

### `FlipX()`

```cpp
const BAffineTransform & BAffineTransform::FlipX()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `FlipY()`

```cpp
const BAffineTransform & BAffineTransform::FlipY()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `GetAffineParameters()`

```cpp
bool BAffineTransform::GetAffineParameters(double * translationX, double * translationY, double * rotation, double * scaleX, double * scaleY, double * shearX, double * shearY)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `translationX` | Undocumented |
| `translationY` | Undocumented |
| `rotation` | Undocumented |
| `scaleX` | Undocumented |
| `scaleY` | Undocumented |
| `shearX` | Undocumented |
| `shearY` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `GetScale()`

```cpp
void BAffineTransform::GetScale(double * sx, double * sy)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `sx` | Undocumented |
| `sy` | Undocumented |





**Since:** Haiku R1

---

### `GetScaleAbs()`

```cpp
void BAffineTransform::GetScaleAbs(double * sx, double * sy)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `sx` | Undocumented |
| `sy` | Undocumented |





**Since:** Haiku R1

---

### `GetTranslation()`

```cpp
void BAffineTransform::GetTranslation(double * tx, double * ty)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `tx` | Undocumented |
| `ty` | Undocumented |





**Since:** Haiku R1

---

### `InverseDeterminant()`

```cpp
double BAffineTransform::InverseDeterminant()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), and [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7).


Referenced by [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862).

---

### `Invert()`

```cpp
const BAffineTransform & BAffineTransform::Invert()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Referenced by [MultiplyInverse()](classBAffineTransform.md#a9e9793223eda0ab6ff25c9d43aa004c2), [operator~()](classBAffineTransform.md#a2bddbfbfc45c2f182b5fddff87ea83e5), and [PreMultiplyInverse()](classBAffineTransform.md#abbb4eb0d6f98afe3f3549dfda385fb50).

---

### `IsDilation()`

```cpp
bool BAffineTransform::IsDilation(double epsilon = kDefaultEpsilon)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `epsilon` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsEqual()`

```cpp
bool BAffineTransform::IsEqual(const BAffineTransform & other, double epsilon = kDefaultEpsilon)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |
| `epsilon` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Referenced by [operator!=()](classBAffineTransform.md#a23a0ec59f04809146dfe9ffe34ce3edf), and [operator==()](classBAffineTransform.md#ae52aa29f15e4525bf0000f01ba8731ac).

---

### `IsFixedSize()`

```cpp
bool BAffineTransform::IsFixedSize()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#ac019f502749a0cc78082f5ec7c8f5b56).

---

### `IsIdentity()`

```cpp
bool BAffineTransform::IsIdentity(double epsilon = kDefaultEpsilon)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `epsilon` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `IsValid()`

```cpp
bool BAffineTransform::IsValid(double epsilon = kDefaultEpsilon)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `epsilon` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Multiply()`

```cpp
const BAffineTransform & BAffineTransform::Multiply(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [PreMultiply()](classBAffineTransform.md#a7ce88697f485af7b0ca7d6435d98489a).


Referenced by [MultiplyInverse()](classBAffineTransform.md#a9e9793223eda0ab6ff25c9d43aa004c2), [operator*=()](classBAffineTransform.md#a042a08b8c104bcbd6c1a2aada58fcbd5), and [PreMultiplyInverse()](classBAffineTransform.md#abbb4eb0d6f98afe3f3549dfda385fb50).

---

### `MultiplyInverse()`

```cpp
const BAffineTransform & BAffineTransform::MultiplyInverse(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [Invert()](classBAffineTransform.md#a314a95ed4eae3167e0f4e918bb602678), and [Multiply()](classBAffineTransform.md#ab9c4342d106d131da6ae68bb0221e18e).


Referenced by [operator/=()](classBAffineTransform.md#a6570653cc8f5af3ab47a500725635dd6).

---

### `operator!=()`

```cpp
bool BAffineTransform::operator!=(const BAffineTransform & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [IsEqual()](classBAffineTransform.md#ab2d8b9f353d23c2396f4d78a30f7f662).

---

### `operator*()`

```cpp
BAffineTransform BAffineTransform::operator*(const BAffineTransform & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [BAffineTransform()](classBAffineTransform.md#ad25069639f485a0565c3bcdc22f9e75e).

---

### `operator*=()`

```cpp
const BAffineTransform & BAffineTransform::operator*=(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [Multiply()](classBAffineTransform.md#ab9c4342d106d131da6ae68bb0221e18e).

---

### `operator/()`

```cpp
BAffineTransform BAffineTransform::operator/(const BAffineTransform & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [BAffineTransform()](classBAffineTransform.md#ad25069639f485a0565c3bcdc22f9e75e).

---

### `operator/=()`

```cpp
const BAffineTransform & BAffineTransform::operator/=(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [MultiplyInverse()](classBAffineTransform.md#a9e9793223eda0ab6ff25c9d43aa004c2).

---

### `operator=()`

```cpp
BAffineTransform & BAffineTransform::operator=(const BAffineTransform & copyFrom)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `copyFrom` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `operator==()`

```cpp
bool BAffineTransform::operator==(const BAffineTransform & other)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [IsEqual()](classBAffineTransform.md#ab2d8b9f353d23c2396f4d78a30f7f662).

---

### `operator~()`

```cpp
BAffineTransform BAffineTransform::operator~()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [Invert()](classBAffineTransform.md#a314a95ed4eae3167e0f4e918bb602678).

---

### `PreMultiply()`

```cpp
const BAffineTransform & BAffineTransform::PreMultiply(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Referenced by [Multiply()](classBAffineTransform.md#ab9c4342d106d131da6ae68bb0221e18e), and [ShearBy()](classBAffineTransform.md#af2010ac85b19bd022b9167dacf5b3319).

---

### `PreMultiplyInverse()`

```cpp
const BAffineTransform & BAffineTransform::PreMultiplyInverse(const BAffineTransform & other)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [Invert()](classBAffineTransform.md#a314a95ed4eae3167e0f4e918bb602678), and [Multiply()](classBAffineTransform.md#ab9c4342d106d131da6ae68bb0221e18e).

---

### `PreRotateBy()`

```cpp
const BAffineTransform & BAffineTransform::PreRotateBy(double angleRadians)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `angleRadians` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), and [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7).

---

### `PreScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::PreScaleBy(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), and [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7).

---

### `PreTranslateBy()`

```cpp
const BAffineTransform & BAffineTransform::PreTranslateBy(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `Reset()`

```cpp
const BAffineTransform & BAffineTransform::Reset()
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `RotateBy()`

```cpp
const BAffineTransform & BAffineTransform::RotateBy(const BPoint & center, double angle)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `angle` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `RotateBy()`

```cpp
const BAffineTransform & BAffineTransform::RotateBy(double angle)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `angle` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `RotateByCopy()`

```cpp
BAffineTransform BAffineTransform::RotateByCopy(const BPoint & center, double angle)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `angle` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `RotateByCopy()`

```cpp
BAffineTransform BAffineTransform::RotateByCopy(double angle)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `angle` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Rotation()`

```cpp
double BAffineTransform::Rotation()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `Scale()`

```cpp
double BAffineTransform::Scale()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(const BPoint & center, const BPoint & scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(const BPoint & center, double scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(const BPoint & center, double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(const BPoint & scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(double scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `ScaleBy()`

```cpp
const BAffineTransform & BAffineTransform::ScaleBy(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [shx](classBAffineTransform.md#ac0507ae12b487272cb2f6b8baec8f20f), [shy](classBAffineTransform.md#a0383bca21bed077dc84747b57d46b333), [sx](classBAffineTransform.md#a6f42e6d417bca34c5d9c4adc71544190), [sy](classBAffineTransform.md#a4c03a79455e12d228e8d062e32dc6dc7), [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(const BPoint & center, const BPoint & scale)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(const BPoint & center, double scale)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(const BPoint & center, double x, double y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(const BPoint & scale)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(double scale)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ScaleByCopy()`

```cpp
BAffineTransform BAffineTransform::ScaleByCopy(double x, double y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetScale()`

```cpp
const BAffineTransform & BAffineTransform::SetScale(double scale)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `scale` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `SetScale()`

```cpp
const BAffineTransform & BAffineTransform::SetScale(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearBy()`

```cpp
const BAffineTransform & BAffineTransform::ShearBy(const BPoint & center, const BPoint & shear)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `shear` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearBy()`

```cpp
const BAffineTransform & BAffineTransform::ShearBy(const BPoint & center, double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearBy()`

```cpp
const BAffineTransform & BAffineTransform::ShearBy(const BPoint & shear)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shear` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearBy()`

```cpp
const BAffineTransform & BAffineTransform::ShearBy(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [AffineShearing()](classBAffineTransform.md#af8084f233f00df42bfbaeb59bc3a597d), and [PreMultiply()](classBAffineTransform.md#a7ce88697f485af7b0ca7d6435d98489a).

---

### `ShearByCopy()`

```cpp
BAffineTransform BAffineTransform::ShearByCopy(const BPoint & center, const BPoint & shear)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `shear` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearByCopy()`

```cpp
BAffineTransform BAffineTransform::ShearByCopy(const BPoint & center, double x, double y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `center` | Undocumented |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearByCopy()`

```cpp
BAffineTransform BAffineTransform::ShearByCopy(const BPoint & shear)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `shear` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `ShearByCopy()`

```cpp
BAffineTransform BAffineTransform::ShearByCopy(double x, double y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `TranslateBy()`

```cpp
const BAffineTransform & BAffineTransform::TranslateBy(const BPoint & delta)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `delta` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `TranslateBy()`

```cpp
const BAffineTransform & BAffineTransform::TranslateBy(double x, double y)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


References [tx](classBAffineTransform.md#a2ea11bc896b815ffaa81abf9f1035e17), and [ty](classBAffineTransform.md#a13fe20ce5797799cc9dc3eaea5d18760).

---

### `TranslateByCopy()`

```cpp
BAffineTransform BAffineTransform::TranslateByCopy(const BPoint & delta)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `delta` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `TranslateByCopy()`

```cpp
BAffineTransform BAffineTransform::TranslateByCopy(double x, double y)const
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `x` | Undocumented |
| `y` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1

---

### `TypeCode()`

```cpp
type_code BAffineTransform::TypeCode()const
```

Undocumented public method. 



**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a819507fa1b0906f14299db15f6e990d1).

---

### `Unflatten()`

```cpp
status_t BAffineTransform::Unflatten(type_code code, const void * buffer, ssize_t size)
```

Undocumented public method. 


Parameters

| Parameter | Description |
| :--- | :--- |
| `code` | Undocumented |
| `buffer` | Undocumented |
| `size` | Undocumented |





**Returns:** Undocumented


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| <value> | Undocumented |





**Since:** Haiku R1


Implements [BFlattenable](../support_kit/classBFlattenable.md#a41e7168574912690be159991d2b07a97).

---

### `kDefaultEpsilon`

```cpp
const double BAffineTransform::kDefaultEpsilon = 1e-14
```

Undocumented public variable. 



**Since:** Haiku R1

---

### `shx`

```cpp
double BAffineTransform::shx
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [Determinant()](classBAffineTransform.md#ae53ecb58adc270f614dbc8aeb852ef61), [InverseDeterminant()](classBAffineTransform.md#ae1847cda27427323d6d4635f97c1d993), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreRotateBy()](classBAffineTransform.md#a0a0889c583b7b842e2825a6bcf341178), [PreScaleBy()](classBAffineTransform.md#abccb7b3b9fcb18b013bb91e10b8fecb2), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), and [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391).

---

### `shy`

```cpp
double BAffineTransform::shy
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [Determinant()](classBAffineTransform.md#ae53ecb58adc270f614dbc8aeb852ef61), [InverseDeterminant()](classBAffineTransform.md#ae1847cda27427323d6d4635f97c1d993), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreRotateBy()](classBAffineTransform.md#a0a0889c583b7b842e2825a6bcf341178), [PreScaleBy()](classBAffineTransform.md#abccb7b3b9fcb18b013bb91e10b8fecb2), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), and [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391).

---

### `sx`

```cpp
double BAffineTransform::sx
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [Determinant()](classBAffineTransform.md#ae53ecb58adc270f614dbc8aeb852ef61), [InverseDeterminant()](classBAffineTransform.md#ae1847cda27427323d6d4635f97c1d993), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreRotateBy()](classBAffineTransform.md#a0a0889c583b7b842e2825a6bcf341178), [PreScaleBy()](classBAffineTransform.md#abccb7b3b9fcb18b013bb91e10b8fecb2), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), and [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391).

---

### `sy`

```cpp
double BAffineTransform::sy
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [Determinant()](classBAffineTransform.md#ae53ecb58adc270f614dbc8aeb852ef61), [InverseDeterminant()](classBAffineTransform.md#ae1847cda27427323d6d4635f97c1d993), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreRotateBy()](classBAffineTransform.md#a0a0889c583b7b842e2825a6bcf341178), [PreScaleBy()](classBAffineTransform.md#abccb7b3b9fcb18b013bb91e10b8fecb2), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), and [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391).

---

### `tx`

```cpp
double BAffineTransform::tx
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391), and [TranslateBy()](classBAffineTransform.md#a472101df3b3a7e45d6393044949c2e54).

---

### `ty`

```cpp
double BAffineTransform::ty
```

Undocumented public variable. 



**Since:** Haiku R1


Referenced by [Apply()](classBAffineTransform.md#a25faa18c510133c835a8d403bfcd4e8d), [ApplyInverse()](classBAffineTransform.md#a57e6fd4979a2e72ee6edd6de34c88862), [operator=()](classBAffineTransform.md#a4c53dc8ffbf3959419ac838e1a7ab840), [PreTranslateBy()](classBAffineTransform.md#add03988f06209700da7b92b8e3b8d915), [RotateBy()](classBAffineTransform.md#a789ff2d5272214339d0dd4b93208ebb8), [ScaleBy()](classBAffineTransform.md#a3c1dce80ba28d91644fa749f2406a391), and [TranslateBy()](classBAffineTransform.md#a472101df3b3a7e45d6393044949c2e54).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBAffineTransform.html).
