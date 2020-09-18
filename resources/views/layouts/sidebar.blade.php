
<div id="sidebar-nav" class="sidebar">
			<div class="sidebar-scroll">
				<nav>
					@if(Auth::user()->role=='admin')
					 <br \>
					 <br \>
					 <br \>

					<ul class="nav">
						<li>
							<a href="#" ><i class="lnr lnr-user"></i> 
								<span>{{ Auth::user()->role }} </span>
							</a>
						</li>
						<li>
							<a href="{{ url('pengguna') }}" class="{{ request()->is('pengguna') ? 'active' : '' }}"><i class="lnr lnr-home"></i> 
								<span>Pengguna</span>
							</a>
						</li>
						<li>
							<a href="{{ url('riwayat') }}" class="{{ request()->is('riwayat') ? 'active' : '' }}"><i class="lnr lnr-chart-bars"></i> 
								<span>Riwayat</span>
							</a>
						</li>
						<li>
							<a href="{{ route('logout') }}" ><i class="lnr lnr-arrow-left-circle"></i> 
								<span>Logout</span>
							</a>
						</li>
					</ul>
					@else
					 <br \>
					 <br \>
					 <br \>
					
						<ul class="nav">
						<li>
							<a href="#" class="active"><i class="lnr lnr-user"></i> 
								<span>{{ Auth::user()->role }} </span>
							</a>
						</li>

						<li>
							<a href="{{ url('dashboard') }}" class=""><i class="lnr lnr-home"></i> 
								<span>Beranda</span>
							</a>
						</li>
						<li>
							<a href="{{ url('cekmutasiku') }}" ><i class="lnr lnr-chart-bars"></i> 
								<span>Cek Mutasi</span>
							</a>
						</li>
						<li>
							<a href="{{ route('logout') }}" ><i class="lnr lnr-arrow-left-circle"></i> 
								<span>Logout</span>
							</a>
						</li>
					</ul>
					@endif
				</nav>
			</div>
		</div>