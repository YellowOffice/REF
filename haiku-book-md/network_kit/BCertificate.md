---
name: BCertificate
type: class
kit: network_kit
brief: "BCertificate is a class that represents a digital certificate used in encrypted network connections, such as X.509 certificates"
source: haiku-book
---

# BCertificate Class
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

[BCertificate](classBCertificate.md) is a class that represents a digital certificate used in encrypted network connections, such as X.509 certificates. 


It is aimed to retrieve information from a certificate, including the date of validity and of expiration, the issuer, subject and the signature algorithm. It also checks if the certificate is a Certificate Authority (CA) certificate as well as if the certificate is self-signed.



**Since:** Haiku R1

## Member List

### Public Member Functions

* [BCertificate](#a562aa5811ea6415507dd794c27e8a2fd) (const BCertificate &other) — Copy constructor.
* `time_t` [ExpirationDate](#ab07ad57d7409d7c77aa5dfcd94abe477) () const — Returns the certificate's notAfter field timestamp.
* `bool` [IsSelfSigned](#a16d50bda6786bc68ccdc933d9d12ebe7) () const — Checks if the certificate was self-signed.
* `BString` [Issuer](#ad20634595e49693f0a487ca4621132cf) () const — Returns the name of the Certificate Authority that issued the certificate.
* `bool` [IsValidAuthority](#a9076a330e829664a4a0fc8e7c7f0867a) () const — Checks if the certificate is a Certificate Authority certificate.
* `bool` [operator==](#a059ff0000aa107e618b40eb3d87c05db) (const BCertificate &other) const — Compares if this certificate is the same as other certificate.
* `BString` [SignatureAlgorithm](#a7c0103c69c76b9ade3788f9f591c0b4c) () const — Returns the name of the certificate's signature algorithm.
* `time_t` [StartDate](#a5c43e6c6b0ee4972010ef2e298522ca9) () const — Returns the certificate's notBefore field timestamp.
* `BString` [String](#a1464e7e915c2cfc8c0c318761a553944) () const — Returns the information contained in the certificate in a human-readable form.
* `BString` [Subject](#ae0bb56c7cdd5c262c568b4400fbd5ab3) () const — Returns the certificate's subject name.
* `int` [Version](#a2b19094b0e6648a6b51a58636322bf44) () const — Returns the numerical value of the certificate's version field.

## Detailed Member Documentation

### `BCertificate()`

```cpp
BCertificate::BCertificate(const BCertificate & other)
```

Copy constructor. 


It creates a deep copy of the certificate data.


Parameters

| Parameter | Description |
| :--- | :--- |
| `other` | The other [BCertificate](classBCertificate.md) object from where to initialize this [BCertificate](classBCertificate.md) instance. |





**Since:** Haiku R1

---

### `ExpirationDate()`

```cpp
time_t BCertificate::ExpirationDate()const
```

Returns the certificate's `notAfter` field timestamp. 


This is the date when the certificate is no longer valid, that is, its expiration date.



**Since:** Haiku R1

---

### `IsSelfSigned()`

```cpp
bool BCertificate::IsSelfSigned()const
```

Checks if the certificate was self-signed. 


A self-signed certificate is one where the CA certificate is the same as the certificated subject.



**Since:** Haiku R1

---

### `Issuer()`

```cpp
BString BCertificate::Issuer()const
```

Returns the name of the Certificate Authority that issued the certificate. 



**Since:** Haiku R1

---

### `IsValidAuthority()`

```cpp
bool BCertificate::IsValidAuthority()const
```

Checks if the certificate is a Certificate Authority certificate. 


CA certificates are those that can be used to sign other certificates.



**Since:** Haiku R1

---

### `operator==()`

```cpp
bool BCertificate::operator==(const BCertificate & other)const
```

Compares if this certificate is the same as *other* certificate. 


Return values

| Col 1 | Col 2 |
| :--- | :--- |
| true | Both [BCertificate](classBCertificate.md) objects refer to the same certificate. |
| false | The certificates are different. |





**Since:** Haiku R1

---

### `SignatureAlgorithm()`

```cpp
BString BCertificate::SignatureAlgorithm()const
```

Returns the name of the certificate's signature algorithm. 



**Since:** Haiku R1

---

### `StartDate()`

```cpp
time_t BCertificate::StartDate()const
```

Returns the certificate's `notBefore` field timestamp. 


This is the date when the certificate starts to be valid.



**Since:** Haiku R1

---

### `String()`

```cpp
BString BCertificate::String()const
```

Returns the information contained in the certificate in a human-readable form. 


This includes the certificate's version, the name of the signature algorithm, the issuer name, the validity period, the subject name, the public key and its algorithm, hexadecimal dump of any unique identifier of the issuer or the subject, any signature algorithm extensions, the signature dump and any non-standard data fields.



**Since:** Haiku R1

---

### `Subject()`

```cpp
BString BCertificate::Subject()const
```

Returns the certificate's subject name. 



**Since:** Haiku R1

---

### `Version()`

```cpp
int BCertificate::Version()const
```

Returns the numerical value of the certificate's version field. 



**Since:** Haiku R1

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/classBCertificate.html).
