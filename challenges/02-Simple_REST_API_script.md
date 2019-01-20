# Challenge #2 - List paired sites with a PowerShell Script

## Overview

This script should do the same thing as challegne #1, the difference is this time you should use the Zerto REST API to complete the task. Remember, the challege is to login to Zerto and get a list of the sites that your ZVM is paired with.

## Hints

[Zerto REST API Online Documentation](http://s3.amazonaws.com/zertodownload_docs/Latest/Zerto%20Virtual%20Replication%20REST%20APIs%20Online%20Help/index.html)

If you have a self signed SSL certificate on your ZVM you will want to use "-SkipCertificateCheck" in your Invoke-WebRest (or Invoke-RESTMethod request) or the method [listed here](https://github.com/Zerto-TA-Public/Script-Templates/blob/master/TIP-PoSH-Ignore-Self-Signed-SSL.ps1). 

## Solution

[Solution](https://github.com/Zerto-TA-Public/Script-Templates/blob/master/Template-REST-From-PoSH.ps1)
