<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
// use Symfony\Component\Process\Process;
// use Symfony\Component\Process\Exception\ProcessFailedException;
class BCAController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
          return view('loginbank.bca');
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }
  public function cek(Request $request)
    {
        // $python_path=public_path().'/bca-scrapping-master/bca.py';
    $username = $request->username;
        $password = $request->password;
        // $process = escapeshellarg('python' .$python_path. .$username. $password);
        // $response = shell_exec($process);
        // echo $process;
        // $output = system("C:\\Python27\\python.exe" "C:\\xampp\\htdocs\\PANING\\public\\bca-scrapping-master\\bca.py"  . $username . $password);

 // $process = new Process(["ls"," /bca-scrapping-master/bca.py"]);
// $oExec = $WshShell->Run();
//         $process->run();
//         if (!$process->isSuccessful()) {
//     throw new ProcessFailedException($process);
// }

// echo $process->getOutput();
// $output = passthru("python /bca-scrapping-master/bca.py");
// echo($WshShell);

// passthru("/usr/bin/php /path/to/script.php ".$argv_parameter." >> /path/to/log_file.log 2>&1 &");


// $out=shell_exec('python -V');

// echo '<pre>'.$out.'</pre>';
// 'C:\Python27\python.exe C:\loginbank\bca-scrapping-master\bca.py'  . $username . $password

 // $my_command = escapeshellcmd('python C:/loginbank/bca-scrapping-master/bca.py');
 //    $command_output = shell_exec($my_command);
 //    echo $command_output;
// 'C:\Python27\python.exe C:\loginbank\bca-scrapping-master\bca.py'  . $username . $password
// echo shell_exec("python cekip.py 2>&1");
        echo shell_exec("python C:/xampp/htdocs/PANING/public/bca-scrapping-master/bca.py 2>&1 $username $password ");

// putenv("username=$username");
// putenv("password=$password");
// putenv("C:/loginbank/bca-scrapping-master/");
// echo shell_exec("C:/Python27/python.exe bca.py $username $password");

// chdir('C:/loginbank/bca-scrapping-master/') ; // python code dir
// $commandline="C:/Python27/python.exe bca.py ". $username . $password ;
// exec($commandline, $output, $error) ;
// echo $output ;
 // echo shell_exec('python -V');
}

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
  

        
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
