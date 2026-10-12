---
name: wireless_network
type: struct
kit: network_kit
brief: "Describes a wireless network"
source: haiku-book
---

# wireless_network Struct
**Kit/Group:** [Network Kit](../network_kit/group__network.md)

## Description

Describes a wireless network. 



**Since:** Haiku R1

## Member List

### Public Member Functions

* `bool` [operator==](#a4d3e4a965e8ca664b42da1dfd2d1817a) (const wireless_network &other) — Checks if other is the same wireless network as this.

### Public Attributes

* `BNetworkAddress` [address](#a00e502a4500864758cb5c000a5afc14b) — The basic service set identifier (BSSID) of the wireless network.
* `uint32` [authentication_mode](#a2c48991252617611710ef36954c65311) — The authentication mode of the wireless network.
* `uint32` [cipher](#ad2125e81ae0218e9d8482f15215c3d1f) — The cipher algorithm of the wireless network.
* `uint32` [flags](#a8af2e6dece2a0937d6b21c46a4f6cf99) — Configuration flags of the wireless_network object.
* `uint32` [group_cipher](#a2b9f6d4823d13eec807bd88b160e0e15) — This field could be defined with one of the values described in wireless_network::cipher.
* `uint32` [key_mode](#a446f87030636c24bfc372b0ad3a7d1b4) — The key negotiation mode.
* `char` [name](#a1d2d44774df8c730fc8fdcffdf38fd1a) [32] — The service set identifier (SSID) of the wireless network.
* `uint8` [noise_level](#ae39bfe7e3761d2e299cb5a458bd039cc) — The noise level of the wireless network.
* `uint8` [signal_strength](#a664db443ae6bbce51fe45e7f62141141) — The signal strength of the wireless network.

## Detailed Member Documentation

### `operator==()`

```cpp
bool wireless_network::operator==(const wireless_network & other)
```

Checks if *other* is the same wireless network as this. 


The check ignores the address difference between *address* and *other.address*.



**Returns:** `true` if both [wireless_network](structwireless__network.md) objects represent the same wireless network, or `false` otherwise.



**Since:** Haiku R1


References [authentication_mode](structwireless__network.md#a2c48991252617611710ef36954c65311), [cipher](structwireless__network.md#ad2125e81ae0218e9d8482f15215c3d1f), [flags](structwireless__network.md#a8af2e6dece2a0937d6b21c46a4f6cf99), [group_cipher](structwireless__network.md#a2b9f6d4823d13eec807bd88b160e0e15), [key_mode](structwireless__network.md#a446f87030636c24bfc372b0ad3a7d1b4), [name](structwireless__network.md#a1d2d44774df8c730fc8fdcffdf38fd1a), [noise_level](structwireless__network.md#ae39bfe7e3761d2e299cb5a458bd039cc), and [signal_strength](structwireless__network.md#a664db443ae6bbce51fe45e7f62141141).

---

### `address`

```cpp
wireless_network::address
```

The basic service set identifier (BSSID) of the wireless network. 



**Since:** Haiku R1

---

### `authentication_mode`

```cpp
wireless_network::authentication_mode
```

The authentication mode of the wireless network. 


The authentication modes are described in this enumeration: 


```cpp
// authentication modes
enum {
 B_NETWORK_AUTHENTICATION_NONE       = 0,
 B_NETWORK_AUTHENTICATION_WEP        = 1,
 B_NETWORK_AUTHENTICATION_WPA        = 2,
 B_NETWORK_AUTHENTICATION_WPA2       = 3,
 B_NETWORK_AUTHENTICATION_EAP        = 4
};
```


**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `cipher`

```cpp
wireless_network::cipher
```

The cipher algorithm of the wireless network. 


The cipher algorithms are described in this enumeration: 


```cpp
// cipher algorithms
enum {
 B_NETWORK_CIPHER_NONE               = 0x01,
 B_NETWORK_CIPHER_WEP_40             = 0x02,
 B_NETWORK_CIPHER_WEP_104            = 0x04,
 B_NETWORK_CIPHER_TKIP               = 0x08,
 B_NETWORK_CIPHER_CCMP               = 0x10,
 B_NETWORK_CIPHER_AES_128_CMAC       = 0x20
};
```


**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `flags`

```cpp
wireless_network::flags
```

Configuration flags of the [wireless_network](structwireless__network.md) object. 


Valid values are:


* [B_NETWORK_IS_ENCRYPTED](NetworkDevice_8h.md#a64c7a78cc741f6cff2a9477c83a8a68b)

* [B_NETWORK_IS_PERSISTENT](NetworkDevice_8h.md#acdfefa588ab2d36835fc5a1db6cc4709)




**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `group_cipher`

```cpp
wireless_network::group_cipher
```

This field could be defined with one of the values described in [wireless_network::cipher](structwireless__network.md#ad2125e81ae0218e9d8482f15215c3d1f). 



**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `key_mode`

```cpp
wireless_network::key_mode
```

The key negotiation mode. 


The key modes are described in this enumeration: 


```cpp
// key modes
enum {
 B_KEY_MODE_IEEE802_1X               = 0x0001,
 B_KEY_MODE_PSK                      = 0x0002,
 B_KEY_MODE_NONE                     = 0x0004,
 B_KEY_MODE_FT_IEEE802_1X            = 0x0020,
 B_KEY_MODE_FT_PSK                   = 0x0040,
 B_KEY_MODE_IEEE802_1X_SHA256        = 0x0080,
 B_KEY_MODE_PSK_SHA256               = 0x0100,
 B_KEY_MODE_WPS                      = 0x0200
};
```


**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `name`

```cpp
wireless_network::name
```

The service set identifier (SSID) of the wireless network. 



**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `noise_level`

```cpp
wireless_network::noise_level
```

The noise level of the wireless network. 



**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

### `signal_strength`

```cpp
wireless_network::signal_strength
```

The signal strength of the wireless network. 



**Since:** Haiku R1


Referenced by [operator==()](structwireless__network.md#a4d3e4a965e8ca664b42da1dfd2d1817a).

---

Generated from the [Haiku Book API docs](https://www.haiku-os.org/docs/api/structwireless__network.html).
