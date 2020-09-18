@extends('layouts.master')
    @section('content')
<!-- MAIN -->
		<div class="main">
			<!-- MAIN CONTENT -->
			<div class="main-content">
				<div class="container-fluid">
					<!-- OVERVIEW -->
					<div class="panel panel-headline">

						<div class="panel-body">
									
						                <div style="padding: 150px;">
						                    <a href=" {{ url('loginbri') }}"><img src="bri.png" height= "160px" width="220" style="padding: 30px;"/></a>
						                     <a href="{{url ('loginbca')}}"><img src="bca.png" height= "160px" width="220" style="padding: 30px;"/></a>
						                     <a href="{{url ('loginbtn')}}"><img src="btn.png" height= "160px" width="220" style="padding: 30px;"/></a>
						            	</div>
						</div>
					</div>
				</div>
			</div>
			<!-- END MAIN CONTENT -->
		</div>
		<!-- END MAIN -->
		    @endsection