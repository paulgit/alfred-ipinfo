<div align="center">
    <img src="./source/icon.png" width="200" height="200">
</div>

# alfred-ipinfo

![GitHub All Releases](https://img.shields.io/github/downloads/paulgit/alfred-ipinfo/total?color=blue&label=Downloads&logo=Github)
![GitHub](https://img.shields.io/github/license/paulgit/alfred-ipinfo?label=License)

ipinfo is an Alfred workflow for fetching information about an IP address. It achieves this by using the [ipinfo.io IP Geolocation API](https://ipinfo.io/products/ip-geolocation-api) which is free to register for and is free to use for 50,000 lookups per month.

## Dependencies
### Python3
This workflow is dependent on Python3 which you must have installed. Please see the [Python3 Installation Guide](https://github.com/paulgit/alfred-ipinfo/wiki/Python3-Installation-Guide).
### ipinfo.io
This workflow makes use of the [IP Geolocation API](https://ipinfo.io/products/ip-geolocation-api) provided by [ipinfo.io](https://ipinfo.io). You will need to register and obtain an API Token. This token value must be entered in the value field of the APITOKEN workflow environment variable.

## Credit & License

* This project is inspired by [tomy0000000/Coinc](https://github.com/tomy0000000/Coinc)
  I based ipinfo on the code structure from coinc as it made use of the [alfred-workflow library](https://github.com/deanishe/alfred-workflow) which I wanted to learn how to use.

* Core Library depends on the work-of-art-library [deanishe/alfred-workflow](https://github.com/deanishe/alfred-workflow)

* API provided by [ipinfo.io](https://ipinfo.io/)

* This site or product includes IP2Location™ Country Flags which available from https://www.ip2location.com.

* Any source code unmentioned above are released under the [MIT license](https://github.com/paulgit/alfred-ipfinfo/blob/master/LICENSE)
