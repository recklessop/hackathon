# Challenge #3 - List all sites in Zerto Analytics Account

## Overview

In this script we will leverage the Zerto Analytics API to get some data about our environment. We will be working with sites again, but this time we will be able to see ALL of the sites associated with your license key, not just the ones paired to a ZVM.

Zerto Analytics is a great resource if you want to get information from more than one ZVM. 

For this challege you should create a script that leverages the Zerto Analytics REST API to get a list of all sites on your account.


## Hints

[Zerto Analytics REST API Docs](https://docs.api.zerto.com/index.html)

If you have a self signed SSL certificate on your ZVM you will want to use "-SkipCertificateCheck" in your Invoke-WebRest (or Invoke-RESTMethod request) or the method [listed here](https://github.com/Zerto-TA-Public/Script-Templates/blob/master/TIP-PoSH-Ignore-Self-Signed-SSL.ps1). 

## Solution

[Solution](https://github.com/Zerto-TA-Public/Script-Templates/blob/master/Template-Zerto-Analytics-REST.ps1)
