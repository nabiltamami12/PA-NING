<?
     function index(Request $request)
  {
        // do stuff (will send data to database)
        $alternative_val = array(
    'username'=>$request->username,
    'password'=>$request->password,
 );
 $json_alter = json_encode($alternative_val);

// echo system('python cekip.py "' . $json_alter . '"');
echo shell_exec('ls');
 // echo $output;
    // C:/loginbank/bca-scrapping-master/cekip.py
}

