<!DOCTYPE html>
<html>
<head>
	<title>hasil cek mutasi</title>
	<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">

  <style>
  	body {
       background: -moz-linear-gradient(bottom, #00FFFF, #0000FF);
       background-repeat: no-repeat;
	}
  	#card {
        background: #fbfbfb;
        border-radius: 8px;
        box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.65);
        height: 320px;
        margin: 6rem auto 8.1rem auto;
        width: 329px;
	}
	#card-content {
      padding: 12px 44px;
	}
	#card-title {
      	font-family: "Raleway Thin", sans-serif;
      	letter-spacing: 4px;
      	padding-bottom: 23px;
      	padding-top: 13px;
      	text-align: center;
	}
	.underline-title {
      background: -moz-linear-gradient(right, #00FFFF, #0000FF);
      height: 2px;
      margin: -1.1rem auto 0 auto;
      width: 185px;
	}

  </style>

</head>
<body>
@extends('layouts.master')
    @section('content')
<!-- MAIN -->
		<div class="main">
			<!-- MAIN CONTENT --> 
			<div class="main-content">
				<div class="container-fluid">
					<!-- OVERVIEW -->
					<div class="panel panel-headline">
						<div class="panel-body text-center" >
							<div id="card"> 

								<div id="card-title">
								    <h2>Cek Mutasi</h2>
								    <div class="underline-title"></div>
								</div>	

							    <form id="card-title">
									
										<input type="radio" name="jenis_bank" value="bri" /> BRI <br>
										<input type="radio" name="jenis_bank" value="bca" /> BCA <br>
										<input type="radio" name="jenis_bank" value="btn" /> BTN <br>
									

										<p>
											Waktu:
											<select>
											     <option>Sekarang</option>
											     <option>Kemarin</option>
											</select>
										</p>

										<p>
										<input type="submit" value="Mulai Proses!" >
										</p>
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
			<!-- END MAIN CONTENT -->
		    @endsection
</body>
</html>


							