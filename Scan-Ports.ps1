$ports=(81,444);
$ip="192.168.13.250";

foreach ($port in $ports) {try{$socket=New-Object System.Net.Sockets.TcpClient($ip, $port);}

catch{};

if ($socket -eq $null) {echo $ip":"$port" - Closed";} else {echo $ip":"$port" - Open";
$socket =- $null;}}