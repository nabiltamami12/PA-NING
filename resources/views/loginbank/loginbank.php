<?
if(isset($_POST['submit']){
  $username = $_POST['username'];
        $password =  $_POST['password'];

$command = escapeshellcmd('C:\Python27\python.exe C:\loginbank\bca-scrapping-master\bca.py'  . $username . $password);
$output = shell_exec($command);
return echo $output;
echo 'hello';
}
?>